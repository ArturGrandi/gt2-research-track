from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_containment_blocks_oracle_updates():

    s = State(
        P=100.0,
        M_VAL=10.0,
        F_stab=50.0,
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=True,
        epoch=0,
    )

    e = Event(type=EventType.ORACLE_UPDATE, payload={"P": 200})

    s2 = delta(s, e)

    assert s2.P == s.P
