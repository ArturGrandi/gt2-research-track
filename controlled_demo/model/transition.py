from __future__ import annotations

from dataclasses import replace

from model.events import Event, EventType
from model.state import State


def _get_mint_amount(state: State, event: Event) -> float:
    return float(getattr(state, "M_VAL"))


def delta(state: State, event: Event) -> State:

    if not hasattr(event, "type"):
        raise TypeError("Event must have 'type'")

    et = event.type.name

    # paused containment
    if state.paused and et not in ("EPOCH_ADVANCE", "EMERGENCY_TRIGGER"):
        return state

    # EPOCH ADVANCE
    if et == "EPOCH_ADVANCE":
        return replace(state, epoch=int(state.epoch) + 1)

    # EMERGENCY
    if et == "EMERGENCY_TRIGGER":
        return replace(state, paused=True)

    # ORACLE UPDATE
    if et == "ORACLE_UPDATE":

        ns = state
        payload = getattr(event, "payload", None) or {}

        if "P" in payload:
            newP = float(payload["P"])
            oldP = float(state.P)

            if abs(newP - oldP) / oldP > 0.2:
                raise ValueError("Oracle step exceeds 20% bound")

            ns = replace(ns, P=newP)

        if "F_stab" in payload:
            ns = replace(ns, F_stab=float(payload["F_stab"]))

        if "F_liq" in payload:
            ns = replace(ns, F_liq=float(payload["F_liq"]))

        if "F_sys" in payload:
            ns = replace(ns, F_sys=float(payload["F_sys"]))

        return ns

    # MINT
    if et == "MINT_TRIGGER":

        m = _get_mint_amount(state, event)

        if m < 0:
            raise ValueError("Mint amount must be >= 0")

        P = float(state.P)
        F_stab = float(state.F_stab)

        gate = P * float(m)

        if F_stab >= gate:
            new_supply = float(state.Supply) + float(m)
            return replace(state, Supply=new_supply)

        return replace(state, paused=True)

    raise ValueError(f"Unhandled event type: {et}")
