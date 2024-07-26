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