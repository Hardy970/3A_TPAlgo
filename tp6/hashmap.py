from dataclasses import dataclass


@dataclass
class Item:
    # TODO: add your attributes here
    k : str
    v: int


@dataclass
class HashMap:
    # TODO: add your attributes here
    table: list[Item]



def hm_size(aa: HashMap) -> int:
    return len(aa.table)

def hm_is_empty(aa: HashMap) -> bool:
    raise NotImplementedError("hm_is_empty function not implemented yet")


# TODO: complete hm_new parameters
def hm_new() -> HashMap:
    raise NotImplementedError("hm_new function not implemented yet")


def hm_get(aa: HashMap, k: str) -> int | None:
    raise NotImplementedError("hm_get function not implemented yet")


def hm_put(aa: HashMap, v: int, k: str) -> None:
    raise NotImplementedError("hm_put function not implemented yet")


def hm_delete(aa: HashMap, k: str) -> None:
    raise NotImplementedError("hm_delete function not implemented yet")


def hm_str(aa: HashMap) -> str:
    raise NotImplementedError("hm_str function not implemented yet")
