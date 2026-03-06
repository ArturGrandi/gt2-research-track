from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_oracle_epoch_interaction():

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

    events = [
        Event(type=EventType.EPOCH_ADVANCE),
        Event(type=EventType.ORACLE_UPDATE, payload={"P": 102}),
        Event(type=EventType.EPOCH_ADVANCE),
        Event(type=EventType.ORACLE_UPDATE, payload={"P": 105}),
        Event(type=EventType.EPOCH_ADVANCE),
    ]

    for e in events:
        s = delta(s, e)

    assert s.epoch == 3
    assert s.P == 105
