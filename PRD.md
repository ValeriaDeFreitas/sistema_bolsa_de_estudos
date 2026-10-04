# PRD - Sistema de Análise de Elegibilidade para Bolsa de Estudos

## 1. Visão Geral
O módulo `app/scholarship_approval.py` avalia a concessão de bolsas de estudos ou descontos nas mensalidades para alunos do ensino superior com base em renda familiar, desempenho acadêmico (CR) e engajamento em atividades de extensão/pesquisa.

## 2. Regras de Negócio e Parâmetros
1. **Idade Mínima (`idade`)**: Deve ser maior ou igual a 16 anos e menor que 100.
2. **Renda Familiar per Capita (`renda_per_capita`)**:
   - `renda_per_capita <= 1500.00`: Elegível para Bolsa Integral (100%).
   - `1500.00 < renda_per_capita <= 3000.00`: Elegível para Bolsa Parcial (50%).
   - `renda_per_capita > 3000.00`: Elegível apenas para Desconto Acadêmico por Mérito (20%).
3. **Coeficiente de Rendimento / Média (`cr`)**:
   - Para Bolsa Integral: `cr >= 8.5`.
   - Para Bolsa Parcial: `cr >= 7.5`.
   - Para Desconto Mérito: `cr >= 9.0`.
   - `cr` deve estar strictly no intervalo de `0.0` a `10.0`.
4. **Horas de Extensão / Iniciação Científica (`horas_extensao`)**:
   - Alunos com `horas_extensao >= 100` recebem um bônus adicional de 10% no desconto final (até o limite de 100%).
5. **Restrição por Inadimplência (`tem_inadimplencia: bool`)**:
   - Se `tem_inadimplencia == True`, o pedido é sumariamente reprovado.

## 3. Saída da Função
Retorna um dicionário contendo:
- `status`: `"APROVADO"` ou `"REPROVADO"`.
- `porcentagem_bolsa`: Valor numérico (`0.0` a `100.0`).
- `motivo`: Descrição clara da decisão.