# Sistema de Análise de Elegibilidade para Bolsa de Estudos e Desconto Acadêmico

Este repositório contém a implementação do módulo de verificação determinística de elegibilidade para concessão de bolsas de estudos e descontos acadêmicos, acompanhado por uma suíte abrangente de testes unitários desenvolvida com Pytest.

Atividade individual desenvolvida para a disciplina de **Qualidade e Teste de Software (QTS)**.

---

## 🛠️ Tecnologias e Ferramentas

- **Linguagem**: Python 3.12+
- **Gerenciador de Pacotes e Ambientes**: `uv`
- **Framework de Testes**: `pytest`
- **Ferramenta de Cobertura de Código**: `pytest-cov`

---

## 📁 Estrutura do Repositório

```text
sistema_bolsa_de_estudos/
├── app/
│   ├── __init__.py
│   └── scholarship_approval.py
├── tests/
│   ├── __init__.py
│   └── test_scholarship_approval.py
├── .cursorrules
├── AGENTS.md
├── AI_USAGE.md
├── PRD.md
├── README.md
├── pyproject.toml
└── uv.lock