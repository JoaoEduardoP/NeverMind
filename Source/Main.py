from Agenda import Agenda

def exibir_menu():
    print("\nDigite a ação (adicionar, remover, mostrar, sair):")

def main():
    agenda = Agenda()
    while agenda.running:
        exibir_menu()
        escolha = input("Digite o comando: ").lower()

        if escolha == 'adicionar':
            nome = input("Digite o nome do evento: ")
            inicio = input("Digite a hora de início (YYYY-MM-DD HH:MM): ")
            fim = input("Digite a hora de término (YYYY-MM-DD HH:MM): ")
            agenda.add_Eventos(nome, inicio, fim)
        elif escolha == 'mostrar':
            agenda.get_Eventos()
        elif escolha == 'remover':
            nome = input("Digite o nome do evento para remover: ")
            agenda.remove_Evento(nome)
        elif escolha == 'sair':
            agenda.sair()
            print("Saindo...")
        else:
            print("Comando inválido! Tente novamente.")

if __name__ == "__main__":
    main()
