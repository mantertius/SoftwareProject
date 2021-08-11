# Folha de Pagamento - Projeto de Software
Programa criado com o intuito de construir um sistema de folha de pagamento. 

A folha de pagamento deve rodar todos os dias e deve pagar o salário daqueles cujos salários vencem naquele dia. O sistema receberá a data limite de cálculo e calculará o quanto deve receber.
## Tipos de empregados
- Horista: Recebem por hora. As horas são marcadas por cartões de ponto. Oito horas por dias. Se trabalharem mais do que oito horas, a taxa deve ser acrescida em 50%. Pagos na sexta-feira
- Comissionados: Recebem um percentual do valor de suas vendas. São pagos a cada duas sextas. Recebem o equivalente a 2 semanas de salário fixo e as comissões.
- Assalariados: Recebem um valor fixo mensal. Pagos no último dia útil do mês.

## Sindicato
- Pode cobrar taxa mensal que varia entre empregados;
- Pode cobrar taxa de serviço adicional mensal;
- Tem um ID único para cada sindicalizado.

### Método de Pagamento

Cada empregado pode escolher um método de pagamento diferente:

- Cheque pelos Correios;
- Cheque em mãos;
- Depósito em conta bancária.

#### Atributos dos Empregados:
-   self.name = name
-   self.address = address
-   self.type = type 
-   companyID = uuid.uuid4()
-   self.unionID = uuid.uuid4()
-   self.hourWage = hourWage
-	self.salary = salary
-	self.unionStatus = False
-	self.unionTax = 0
-	self.commission = commission