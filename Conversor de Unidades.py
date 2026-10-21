#Conversor de Unidades

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def km_para_milhas(km):
    return km * 0.621371
def milhas_para_km(milhas):
    return milhas / 0.621371
def metros_para_pes(metros):
    return metros * 3.28084
def pes_para_metros(pes):
    return pes / 3.28084

def menu():
    print("\n=== CONVERSOR DE UNIDADES ===")
    print("1. Celsius para Fahrenheit")
    print("2. Fahrenheit para Celsius")
    print("3. Km para Milhas")
    print("4. Milhas para Km")
    print("5. Metros para Pés")
    print("6. Pés para Metros")
    print("0. Sair")
def ler_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Por favor, insira um número válido.")
def main():
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            celsius = ler_numero("Digite a temperatura em Celsius: ")
            print(f"{celsius}°C = {celsius_para_fahrenheit(celsius)}°F")
        elif opcao == "2":
            fahrenheit = ler_numero("Digite a temperatura em Fahrenheit: ")
            print(f"{fahrenheit}°F = {fahrenheit_para_celsius(fahrenheit)}°C")
        elif opcao == "3":
            km = ler_numero("Digite a distância em Km: ")
            print(f"{km} Km = {km_para_milhas(km)} Milhas")
        elif opcao == "4":
            milhas = ler_numero("Digite a distância em Milhas: ")
            print(f"{milhas} Milhas = {milhas_para_km(milhas)} Km")
        elif opcao == "5":
            metros = ler_numero("Digite a distância em Metros: ")
            print(f"{metros} Metros = {metros_para_pes(metros)} Pés")
        elif opcao == "6":
            pes = ler_numero("Digite a distância em Pés: ")
            print(f"{pes} Pés = {pes_para_metros(pes)} Metros")
        else:
            if opcao == "0":
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")