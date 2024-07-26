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
            for evento in self.eventos:
                if not (fim_dt <= evento['inicio'] or inicio_dt >= evento['fim']):
                    print("Conflito de agendamento detectado.")
                    erro = 1
                    break
            if erro == 0:
                if inicio_dt >= fim_dt:
                        print("A hora de inicio deve ser anterior a hora de termino.")
                        erro = 1
                else:
                    self.eventos.append({
                    'nome': nome,
                    'inicio': inicio_dt,
                    'fim': fim_dt
                    })
                    self.qtd_eventos += 1
                    print("Evento adicionado com sucesso.")   
    
    def get_Eventos(self):
        formato = "%Y-%m-%d %H:%M"
        if len(self.eventos) >= 1:
            for evento in self.eventos:
                print(f"{evento['nome']}: {evento['inicio'].strftime(formato)} a {evento['fim'].strftime(formato)}")
        else:
            print("Nenhum evento agendado.")

        return

    def remove_Evento(self, nome):
        if len(self.eventos) <= 0:
            print("Não existem eventos cadastrados")
            return
        
        try:
            self.eventos.remove(next(evento for evento in self.eventos if evento['nome'] == nome))
            print("Evento removido com sucesso.")
        except ValueError:
            print(f"Evento '{nome}' não encontrado na lista.")
            return

        return

    
    def sair(self):
        return 0