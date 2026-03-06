from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_containment_cascade():

    s = State(
        P=100.0,
        M_VAL=10.0,
        F_stab=50.0,
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    s = delta(s, Event(type=EventType.MINT_TRIGGER, payload={"amount":1}))

    assert s.paused is True
