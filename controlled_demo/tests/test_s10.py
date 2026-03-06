from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_oracle_stress_sequence():

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

    prices = [
        102, 105, 103, 108, 110,
        107, 109, 111, 108, 106,
        104, 101, 103, 105, 107
    ]

    for p in prices:
        e = Event(type=EventType.ORACLE_UPDATE, payload={"P": p})
        s = delta(s, e)

    assert s.P == 107
