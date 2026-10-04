# Relatório de Transparência e Uso de Inteligência Artificial

## 1. Ferramentas Utilizadas
- **Claude / ChatGPT / Cursor**: Utilizado como assistente de codificação para geração inicial de casos de teste e refatoração de regras de negócio.

## 2. Como a IA Foi Empregada
- **Geração do PRD**: Formulação das regras de transição de status para concessão de bolsas acadêmicas.
- **Suíte de Testes**: Sugestão de valores limítrofes (BVA) e partição de equivalência (EP).

## 3. Processo de Auditoria Humana
- Todo código gerado foi auditado manualmente para validar o tratamento defensivo de exceções e refatorado para atender às exigências de 100% de cobertura de branch via `pytest-cov`.