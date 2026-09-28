"""

Calculadora de IVA

Este módulo calcula o valor do IVA
e o preço total com base no valor base inserido pelo utilizador.

"""

print("=== Calculadora de IVA ===")

preco = float(input("Preço sem IVA (€): "))
taxa = 0.23

valor_iva = preco * taxa
total = preco + valor_iva

print(f"IVA (23%): {valor_iva: .2f}")
print(f"Total com IVA: {total: .2f}")