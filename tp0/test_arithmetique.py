
import tp0.arithmetique as a
import pytest

def test_val_absolute():
    assert a.ValAbsolue(-100)==100
    assert a.ValAbsolue(-1)==1
    assert a.ValAbsolue(-0.5)==0.5

@pytest.mark.parametrize("arg,expected", [(3, True), (5, True), (10, False),(0.5,True),(-3,True)])
def test_imp(arg, expected):
    assert a.nImpair(arg) == expected


@pytest.fixture
def forty_two() -> int:
    return 42

@pytest.mark.parametrize("k", [0,1,2,3,4,5,6,7,8,9])
def test_prod_mod(k,forty_two:int):
        assert a.prodMod(forty_two*k,63,forty_two) ==0