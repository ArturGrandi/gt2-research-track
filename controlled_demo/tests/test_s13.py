from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_mint_sequence_growth():

    s = State(
        P=10.0,
        M_VAL=1.0,
        F_stab=1000.0,
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    for _ in range(20):
        e = Event(type=EventType.MINT_TRIGGER, payload={"amount": 1})
        s = delta(s, e)

    assert s.Supply == 20
