from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_mint_above_gate_increases_supply():

    s = State(
        P=10.0,
        M_VAL=1.0,
        F_stab=100.0,  # sufficient coverage
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    e = Event(type=EventType.MINT_TRIGGER, payload={"amount": 1})

    s2 = delta(s, e)

    assert s2.Supply > s.Supply
