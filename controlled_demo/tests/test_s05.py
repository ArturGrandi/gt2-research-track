from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_oracle_oscillation():

    s = State(
        P=100.0,
        M_VAL=50.0,
        F_stab=150.0,
        F_liq=10.0,
        F_sys=5.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    prices = [105, 98, 102, 97, 101]

    for p in prices:
        e = Event(type=EventType.ORACLE_UPDATE, payload={"P": p})
        s = delta(s, e)

    assert s.P == 101
