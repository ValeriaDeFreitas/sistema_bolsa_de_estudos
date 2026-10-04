"""Suíte de testes unitários com Pytest (EP, BVA e Error Guessing)."""

import pytest
from app.scholarship_approval import avaliar_elegibilidade_bolsa


@pytest.mark.unit
@pytest.mark.parametrize(
    "idade, renda, cr, horas, inadimplente, status_esperado, bolsa_esperada",
    [
        (20, 1500.00, 8.5, 0, False, "APROVADO", 100.0),
        (20, 1000.00, 9.0, 50, False, "APROVADO", 100.0),
        (20, 1500.00, 8.4, 0, False, "REPROVADO", 0.0),
        
        (22, 1500.01, 7.5, 0, False, "APROVADO", 50.0),
        (22, 3000.00, 7.5, 0, False, "APROVADO", 50.0),
        (22, 2000.00, 7.4, 0, False, "REPROVADO", 0.0),
        
        (22, 2000.00, 8.0, 100, False, "APROVADO", 60.0),
        (20, 1000.00, 9.0, 120, False, "APROVADO", 100.0), # Teto em 100%
        
        (25, 3000.01, 9.0, 0, False, "APROVADO", 20.0),
        (25, 5000.00, 8.9, 0, False, "REPROVADO", 0.0),
        (25, 5000.00, 9.5, 150, False, "APROVADO", 30.0), # Mérito + Extensão
        
        (20, 1000.00, 9.5, 100, True, "REPROVADO", 0.0),
    ],
)
def test_avaliar_elegibilidade_sucesso_e_reprovacoes(
    idade, renda, cr, horas, inadimplente, status_esperado, bolsa_esperada
):
    """Testa fluxos felizes e de reprovação determinística (AAA)."""
    resultado = avaliar_elegibilidade_bolsa(idade, renda, cr, horas, inadimplente)

    assert resultado["status"] == status_esperado
    assert resultado["porcentagem_bolsa"] == bolsa_esperada


@pytest.mark.unit
@pytest.mark.parametrize(
    "idade, renda, cr, horas, inadimplente, excecao, mensagem",
    [
        (15, 1000.0, 8.0, 0, False, ValueError, "A idade deve estar entre 16 e 99 anos."),
        (100, 1000.0, 8.0, 0, False, ValueError, "A idade deve estar entre 16 e 99 anos."),
        (20, -1.0, 8.0, 0, False, ValueError, "A renda per capita não pode ser negativa."),
        (20, 1000.0, -0.1, 0, False, ValueError, "O CR deve estar entre 0.0 e 10.0."),
        (20, 1000.0, 10.1, 0, False, ValueError, "O CR deve estar entre 0.0 e 10.0."),
        (20, 1000.0, 8.0, -1, False, ValueError, "As horas de extensão não podem ser negativas."),
        
        ("20", 1000.0, 8.0, 0, False, TypeError, "O parâmetro 'idade' deve ser um número inteiro."),
        (True, 1000.0, 8.0, 0, False, TypeError, "O parâmetro 'idade' deve ser um número inteiro."),
        (20, "1000", 8.0, 0, False, TypeError, "O parâmetro 'renda_per_capita' deve ser um número real."),
        (20, 1000.0, "8.0", 0, False, TypeError, "O parâmetro 'cr' deve ser um número real."),
        (20, 1000.0, 8.0, "0", False, TypeError, "O parâmetro 'horas_extensao' deve ser um número inteiro."),
        (20, 1000.0, 8.0, 0, "False", TypeError, "O parâmetro 'tem_inadimplencia' deve ser um booleano."),
    ],
)
def test_avaliar_elegibilidade_excecoes(
    idade, renda, cr, horas, inadimplente, excecao, mensagem
):
    """Testa entradas inválidas e lançamento defensivo de exceções (AAA)."""
    with pytest.raises(excecao) as exc_info:
        avaliar_elegibilidade_bolsa(idade, renda, cr, horas, inadimplente)

    assert mensagem in str(exc_info.value)