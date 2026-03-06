from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_long_oracle_oscillation():

    s = State(
        P=100.0,
        M_VAL=10.0,
        F_stab=1000.0,
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    prices = [101,99,102,98,103,97,104,96]

    for p in prices:
        s = delta(s, Event(type=EventType.ORACLE_UPDATE, payload={"P": p}))

    assert s.P == 96
