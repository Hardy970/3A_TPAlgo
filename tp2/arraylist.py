# content of tp2/arraylist.py
from dataclasses import dataclass

from tp2.util import StaticArray,alloc


@dataclass
class ArrayList:
    """User-defined type for List ADT implemented with static arrays."""
    max_size: int
    t: StaticArray
    util_size: int


def al_new(m: int = 10, l: list[int] | None = None) -> ArrayList:
    l = l if l is not None else []
    assert m >= len(l), f"capacité {m} trop faible"

    tab: StaticArray = alloc(m)

    for i in range(len(l)):
       tab[i] = l[i]

    return ArrayList(t=tab, max_size=m, util_size=len(l))


def al_len(tab: ArrayList) -> int:
    return tab.util_size

def al_is_empty(tab: ArrayList) -> bool:
    return tab.util_size==0

def al_str(tab: ArrayList) -> str:
    raise NotImplementedError("ArrayList al_str function not implemented yet")


def al_get(tab: ArrayList, i: int) -> int:
    raise NotImplementedError("ArrayList al_get function not implemented yet")


def al_set(tab: ArrayList, i: int, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_set function not implemented yet")


def al_lookup(tab: ArrayList, item: int) -> int | None:
    raise NotImplementedError("ArrayList al_lookup function not implemented yet")


def al_remove(tab: ArrayList, i: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_remove function not implemented yet")


def al_insert(tab: ArrayList, i: int, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_insert function not implemented yet")


def al_prepend(tab: ArrayList, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_prepend function not implemented yet")


def al_append(tab: ArrayList, item: int) -> ArrayList:
    raise NotImplementedError("ArrayList al_append function not implemented yet")


def al_extend(tab1: ArrayList, tab2: ArrayList) -> ArrayList:
    raise NotImplementedError("ArrayList al_extend function not implemented yet")