# content of tp3/stack.py
from array import ArrayType
from dataclasses import dataclass
from xml.dom.minicompat import StringTypes

from tp3.deque import Deque, d_new, d_len, d_is_empty, d_str, d_push_front, d_pop_front, d_front
from tp3.linkedlist import ll_str, ll_is_empty, ll_iter


@dataclass
class Stack:
    d: Deque


def s_new(n: int = 10) -> Stack:
    assert n >=0
    return Stack(d_new())

def s_size(s: Stack) -> int:
    return d_len(s.d)

def s_is_empty(s: Stack) -> bool:
    return d_is_empty(s.d)

def s_str(st: Stack) -> str:
    if ll_is_empty(st.d.ll):
        s = '[]'
    else:
        s = '['
        for c in ll_iter(st.d.ll,True):
            s += f'{c.item}'
            s += ', '
        s = s[:-2]
        s += ']'
    return s


def s_push(s: Stack, item: int) -> Stack:
    d_push_front(s.d,item)
    return s

def s_pop(s: Stack) -> Stack:
    d_pop_front(s.d)
    return s

def s_top(s: Stack) -> int:
    return d_front(s.d)