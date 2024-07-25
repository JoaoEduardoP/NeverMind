import pytest
from datetime import datetime
from Source.Agenda import Agenda

@pytest.fixture
def agenda():
    return Agenda()

def test_add_Eventos_sucesso(agenda,capsys):
    agenda.add_Eventos("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == 'Evento adicionado com sucesso.'
    assert len(agenda.eventos) == 1
    assert agenda.eventos[0]['nome'] == "Final dos 100m"
    assert agenda.eventos[0]['inicio'] == datetime(2024, 7, 24, 10, 0)
    assert agenda.eventos[0]['fim'] == datetime(2024, 7, 24, 11, 0)

def test_add_Eventos_data_invalida(agenda,capsys):
    agenda.add_Eventos("Final dos 100m", "2024-13-35 11:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "Formato de data e hora invalido. Use 'YYYY-MM-DD HH:MM'."
    assert len(agenda.eventos) == 0

def test_add_Eventos_hora_inicio_maior_que_fim(agenda,capsys):
    agenda.add_Eventos("Final dos 100m", "2024-07-24 12:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    assert out.strip() == "A hora de inicio deve ser anterior a hora de termino."
    assert len(agenda.eventos) == 0