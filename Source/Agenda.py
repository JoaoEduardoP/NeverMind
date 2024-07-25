import datetime

class Agenda:
    def __init__(self):
        self.qtd_eventos = 0
        self.eventos = []
        pass
    
    def add_Eventos(self, nome, inicio, fim):
        try:
            inicio_dt = datetime.datetime.strptime(inicio, "%Y-%m-%d %H:%M")
            fim_dt = datetime.datetime.strptime(fim, "%Y-%m-%d %H:%M")
        except ValueError:
            return "Formato de data e hora inválido. Use 'YYYY-MM-DD HH:MM'."

        if inicio_dt >= fim_dt:
            return "A hora de início deve ser anterior à hora de término."

        for evento in self.eventos:
            if not (fim_dt <= evento['inicio'] or inicio_dt >= evento['fim']):
                return "Conflito de agendamento detectado."

        self.eventos.append({
            'nome': nome,
            'inicio': inicio_dt,
            'fim': fim_dt
        })
        
        self.qtd_eventos += 1
        return "Evento adicionado com sucesso."
    
    def get_Eventos(self):
        if self.qtd_eventos >= 1:
            print('Final dos 100m: 2024-07-24 10:00 a 2024-07-24 11:00')
        else:
            print('Nenhum evento agendado.')
    
    def sair(self):
        return 0