from controlled_demo.model.state import State
from controlled_demo.model.events import Event, EventType
from controlled_demo.model.transition import delta


def test_long_protocol_run():

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

        # epoch progresses
        s = delta(s, Event(type=EventType.EPOCH_ADVANCE))

        # oracle small variation
        new_price = 10 + (i % 3)
        s = delta(s, Event(type=EventType.ORACLE_UPDATE, payload={"P": new_price}))

        # mint attempt
        s = delta(s, Event(type=EventType.MINT_TRIGGER, payload={"amount": 1}))

    assert s.epoch == 100
    assert s.Supply > 0
