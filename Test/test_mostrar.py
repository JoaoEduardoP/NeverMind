import pytest
from Source.Agenda import Agenda

@pytest.fixture
def agenda():
    return Agenda()

def test_mostrar_sem_Evento(agenda, capsys):
    agenda.get_Eventos()
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 0
    assert out.strip() == "Nenhum evento agendado."

def test_mostrar_um_Evento(agenda, capsys):
    agenda.add_Eventos("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    agenda.get_Eventos()
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 1
    assert out.strip() == "Final dos 100m: 2024-07-24 10:00 a 2024-07-24 11:00"

def test_mostrar_dois_ou_mais_Eventos(agenda, capsys):
    agenda.add_Eventos("Final dos 100m", "2024-07-24 10:00", "2024-07-24 11:00")
    out, _ = capsys.readouterr()
    agenda.add_Eventos("Final dos 200m", "2024-07-24 11:30", "2024-07-24 12:30")
    out, _ = capsys.readouterr()
    assert len(agenda.eventos) == 2
    agenda.get_Eventos()
    out, _ = capsys.readouterr()
    assert out.strip() == "Final dos 100m: 2024-07-24 10:00 a 2024-07-24 11:00\nFinal dos 200m: 2024-07-24 11:30 a 2024-07-24 12:30"