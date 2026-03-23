#  Consumo de energia

# Entrada de dados
aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência (em watts): "))
horas_dia = float(input("Digite o uso médio diário (em horas): "))

# Cálculo do consumo mensal
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo do custo (opcional)
valor_kwh = 0.75
custo = consumo_mensal * valor_kwh

# Saída formatada
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo:.2f}")
if consumo_mensal > 100:
    print("⚠️ Alto consumo de energia!")
else:
    print("✅ Consumo dentro do normal")
