from controlled_demo.model.state import State
from controlled_demo.model.transition import delta

def test_initial_state_valid():
    s = State(
        P=1.0,
        M_VAL=1.0,
        F_stab=100.0,
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    s.validate_non_negative() 

  
def test_epoch_advance():
    s = State(
        P=1.0,
        M_VAL=1.0,
        F_stab=100.0,
        F_liq=0.0,
        F_sys=0.0,
        TimeCapital_total=0.0,
        TimeCapital_active=0.0,
        Supply=0.0,
        paused=False,
        epoch=0,
    )

    from controlled_demo.model.events import Event, EventType
    from controlled_demo.model.transition import delta

    e = Event(type=EventType.EPOCH_ADVANCE)

    s2 = delta(s, e)

    assert s2.epoch == 1
    assert s.epoch == 0