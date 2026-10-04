"""Módulo de validação de elegibilidade para bolsas de estudo."""

from typing import Dict, Union


def avaliar_elegibilidade_bolsa(
    idade: int,
    renda_per_capita: float,
    cr: float,
    horas_extensao: int,
    tem_inadimplencia: bool,
) -> Dict[str, Union[str, float]]:
    """Avalia a concessão de bolsa ou desconto acadêmico com base no perfil do aluno."""
    if not isinstance(idade, int) or isinstance(idade, bool):
        raise TypeError("O parâmetro 'idade' deve ser um número inteiro.")
    if not isinstance(renda_per_capita, (int, float)) or isinstance(renda_per_capita, bool):
        raise TypeError("O parâmetro 'renda_per_capita' deve ser um número real.")
    if not isinstance(cr, (int, float)) or isinstance(cr, bool):
        raise TypeError("O parâmetro 'cr' deve ser um número real.")
    if not isinstance(horas_extensao, int) or isinstance(horas_extensao, bool):
        raise TypeError("O parâmetro 'horas_extensao' deve ser um número inteiro.")
    if not isinstance(tem_inadimplencia, bool):
        raise TypeError("O parâmetro 'tem_inadimplencia' deve ser um booleano.")

    if idade < 16 or idade >= 100:
        raise ValueError("A idade deve estar entre 16 e 99 anos.")
    if renda_per_capita < 0.0:
        raise ValueError("A renda per capita não pode ser negativa.")
    if cr < 0.0 or cr > 10.0:
        raise ValueError("O CR deve estar entre 0.0 e 10.0.")
    if horas_extensao < 0:
        raise ValueError("As horas de extensão não podem ser negativas.")

    if tem_inadimplencia:
        return {
            "status": "REPROVADO",
            "porcentagem_bolsa": 0.0,
            "motivo": "Reprovado devido a pendências financeiras/inadimplência.",
        }

    bolsa_base = 0.0

    if renda_per_capita <= 1500.00:
        if cr >= 8.5:
            bolsa_base = 100.0
        else:
            return {
                "status": "REPROVADO",
                "porcentagem_bolsa": 0.0,
                "motivo": "CR insuficiente para Bolsa Integral na faixa de renda até R$ 1500,00.",
            }
    elif renda_per_capita <= 3000.00:
        if cr >= 7.5:
            bolsa_base = 50.0
        else:
            return {
                "status": "REPROVADO",
                "porcentagem_bolsa": 0.0,
                "motivo": "CR insuficiente para Bolsa Parcial na faixa de renda até R$ 3000,00.",
            }
    else:
        if cr >= 9.0:
            bolsa_base = 20.0
        else:
            return {
                "status": "REPROVADO",
                "porcentagem_bolsa": 0.0,
                "motivo": "Renda acima do limite social e CR insuficiente para Desconto de Mérito.",
            }

    # Bônus por Extensão
    if horas_extensao >= 100 and bolsa_base < 100.0:
        bolsa_base += 10.0

    return {
        "status": "APROVADO",
        "porcentagem_bolsa": float(bolsa_base),
        "motivo": "Solicitação aprovada com sucesso.",
    }