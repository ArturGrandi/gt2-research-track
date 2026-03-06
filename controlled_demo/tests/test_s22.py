from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_protocol_invariant_under_stress():

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

    for i in range(100):

        s = delta(s, Event(type=EventType.EPOCH_ADVANCE))

        if i % 5 == 0:
            s = delta(s, Event(type=EventType.ORACLE_UPDATE, payload={"P":10+(i%3)}))

        s = delta(s, Event(type=EventType.MINT_TRIGGER, payload={"amount":1}))

    assert s.epoch == 100
