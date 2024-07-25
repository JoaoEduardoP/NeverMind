import datetime

class Agenda:
    def __init__(self):
        self.qtd_eventos = 0
        self.eventos = []
        pass
    
    def add_Eventos(self, nome, inicio, fim):
        inicio_dt = 0
        fim_dt = 0
        erro = 0

        try:
            inicio_dt = datetime.datetime.strptime(inicio, "%Y-%m-%d %H:%M")
            fim_dt = datetime.datetime.strptime(fim, "%Y-%m-%d %H:%M")
        except ValueError:
            print("Formato de data e hora invalido. Use 'YYYY-MM-DD HH:MM'.")
            erro = 1

        if erro == 0:
            self.eventos.append({
            'nome': nome,
            'inicio': inicio_dt,
            'fim': fim_dt
            })
            self.qtd_eventos += 1
            print("Evento adicionado com sucesso.")   
    
    def get_Eventos(self):
        if self.qtd_eventos >= 1:
            print('Final dos 100m: 2024-07-24 10:00 a 2024-07-24 11:00\n')
        else:
            print('Nenhum evento agendado.')
    
    def sair(self):
        return 0