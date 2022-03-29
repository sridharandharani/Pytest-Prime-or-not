import primeornot
import pytest

@pytest.mark.parametrize("a,res",[(13,True),(4,False),(7,True),(8,True)])
def test_Prime(a,res):
    result = primeornot.primeornot(a)
    assert result == res