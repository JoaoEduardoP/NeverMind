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