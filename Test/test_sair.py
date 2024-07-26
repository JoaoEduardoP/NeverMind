from Source.Agenda import Agenda

def test_sair():
    agenda = Agenda()
    assert agenda.running is True
    agenda.sair()
    assert agenda.running is False