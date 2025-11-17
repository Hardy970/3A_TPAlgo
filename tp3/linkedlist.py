# content of tp3/linkedlist.py
from __future__ import annotations
from dataclasses import dataclass
from collections.abc import Iterator
from typing import Any



@dataclass
class LinkedList:
    sentinelle: Cell
    size : int

@dataclass(eq=False)
class Cell:
    item: int
    next : Cell | None
    previous:Cell | None


def ll_new(initial_l: list[int] | None = None) -> LinkedList:
    s = Cell(-1,None,None)
    s.next=s
    s.previous=s
    l=LinkedList(s,0)
    if initial_l:
        for i in range(len(initial_l)):
            ll_append(l,initial_l[i])
    return l


def ll_is_empty(l: LinkedList) -> bool:
    return l.size==0

def ll_head(l: LinkedList) -> Cell:
    if l.size==0:
        raise IndexError
    return l.sentinelle.next

def ll_tail(l: LinkedList) -> Cell:
    if l.size==0:
        raise IndexError
    return l.sentinelle.previous

def ll_append(l: LinkedList, item: int) -> Cell:
    newCell= Cell(item,l.sentinelle,l.sentinelle.previous)
    l.sentinelle.previous.next = newCell
    l.sentinelle.previous= newCell
    l.size = l.size +1
    return newCell

def ll_iter(l: LinkedList, reverse: bool=False) -> Iterator[Cell]:
    current: Cell = l.sentinelle  # initialise la variable current à la tête de liste
    if reverse:                             # parcourt la liste en sens inverse
        while (current := current.previous) is not l.sentinelle:     # tant qu'il y a des maillons
            yield current
                    # "return" le maillon courant et gèle l'exécution
    else:                                   # idem, dans le sens de la liste
        while (current := current.next) is not l.sentinelle:
            yield current


def ll_len(l: LinkedList) -> int:
    return l.size

def ll_str(l: LinkedList) -> str:
    """if ll_is_empty(l):
        s='[]'
    else:
        s='['
        head= l.sentinelle.next
        while head.item!=-1:
            if head.next is l.sentinelle:
                s+=f'${head.item}]'
            else:
                s+=f'${head.item}, '
            head=head.next
    return s"""
    if ll_is_empty(l):
        s='[]'
    else:
        s='['
        for c in ll_iter(l):
            s+=f'{c.item}'
            s+=', '
        s=s[:-2]
        s+=']'
    return s




def ll_lookup(l: LinkedList, item: int) -> Cell | None:
    try:
        head= ll_head(l)
    except IndexError:
        return None
    while head is  not l.sentinelle:
        if head.item==item:
            return head
        head=head.next
    return None
def ll_cell_at(l: LinkedList, i: int) -> Cell:
    head = ll_head(l)
    c=0
    while c != i and head is not l.sentinelle:
        head = head.next
        c+=1
    if head==l.sentinelle:
        raise IndexError
    return head
def ll_prepend(l: LinkedList, item: int) -> Cell:
    newCell= Cell(item,l.sentinelle.next,l.sentinelle)
    l.sentinelle.next.previous= newCell
    l.sentinelle.next= newCell
    l.size+=1
    return newCell

def ll_insert(l: LinkedList, item: int, next_to: Cell) -> Cell:
    newCell= Cell(item,next_to.next,next_to)
    next_to.next.previous = newCell
    next_to.next= newCell
    l.size +=1
    return newCell


def ll_remove(l: LinkedList, cell: Cell) -> int:
    cell.previous.next= cell.next
    cell.next.previous= cell.previous
    l.size-=1
    return cell.item

def ll_extend(l1: LinkedList, l2: LinkedList) -> None:
    raise NotImplementedError("LinkedList ll_extend function not yet implemented")


if __name__ == '__main__':
    l = ll_new([1,2,3,4])
    for c in ll_iter(l):
        print(c.item)