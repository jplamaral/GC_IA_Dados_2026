import random 
cardapio = {
    "chocolate": 5.00,
    "baunilha": 4.50,
    "morango": 3.50,
    "flocos": 9.00,
}

brindes = ["Canudo", "Copo", "Gelo", "Badge"]

def mostrar_cardapio():
    print("-- Cardápio --")
    for sabor, preco in cardapio.items():
        print(f"{sabor.title()}: R${preco:.2f}")

def pedir_sorvete():
            total = 0
            pedido = []
            while True:
                sabor = input("\nDigite o sabor : (digite 'fechar'para sair)")
                if sabor == "fechar":
                    break
                elif sabor in cardapio:
                    total += cardapio[sabor]
                    pedido.append(sabor)
                    print(f"{sabor} adicionado ao pedido.")
                else:
                    print("Sabor não esta no cardapio.")
            return pedido, total

mostrar_cardapio()
pedido, total = pedir_sorvete()

print(f"\n Seu pedido: {pedido}")
print(f"Total: R${total:.2f}")
if total > 20:
    brinde = random.choice(brindes)
    print(f"Parabéns! Você ganhou um brinde: {brinde}")
