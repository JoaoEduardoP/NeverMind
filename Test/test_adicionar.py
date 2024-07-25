import pytest
from datetime import datetime
from Source.Agenda import Agenda

@pytest.fixture
def agenda():
    return Agenda()

def test_add_Eventos_sucesso(agenda):
    resultado = agenda.add_Eventos("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    assert resultado == "Evento adicionado com sucesso."
    assert len(agenda.eventos) == 1
    assert agenda.eventos[0]['nome'] == "Final dos 100m"
    assert agenda.eventos[0]['inicio'] == datetime(2024, 7, 24, 10, 0)
    assert agenda.eventos[0]['fim'] == datetime(2024, 7, 24, 11, 0)

def test_add_Eventos_data_invalida(agenda):
    resultado = agenda.add_Eventos("Final dos 100m", "data_invalida", "2024-07-24 11:00")
    assert resultado == "Formato de data e hora inválido. Use 'YYYY-MM-DD HH:MM'."
    assert len(agenda.eventos) == 0

def test_add_Eventos_hora_inicio_maior_que_fim(agenda):
    resultado = agenda.add_Eventos("Final dos 100m", "2024-07-24 12:00", "2024-07-24 11:00")
    assert resultado == "A hora de início deve ser anterior à hora de término."
    assert len(agenda.eventos) == 0

def test_add_Eventos_conflito(agenda):
    agenda.add_Eventos("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    resultado = agenda.add_Eventos("Final dos 200m", "2024-07-24 10:30", "2024-07-24 11:30")
    assert resultado == "Conflito de agendamento detectado."
    assert len(agenda.eventos) == 1

def test_add_Eventos_sem_conflito(agenda):
    agenda.add_Eventos("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    resultado = agenda.add_Eventos("Final dos 200m", "2024-07-24 11:30", "2024-07-24 12:30")
    assert resultado == "Evento adicionado com sucesso."
    assert len(agenda.eventos) == 2