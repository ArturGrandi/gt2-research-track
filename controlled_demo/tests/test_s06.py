from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_mint_below_gate_triggers_pause():

    s = State(
        P=100.0,
        M_VAL=10.0,
        F_stab=100.0,   # coverage insufficient (100 < 100*10)
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    e = Event(type=EventType.MINT_TRIGGER, payload={"amount": 10})

    s2 = delta(s, e)

    assert s2.paused is True
