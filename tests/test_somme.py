from somme.add import addition
import pytest
def test_add():
    assert addition(2,1) == 3
    
@pytest.mark.xfail()
def test_add_expect_to_fail():
    assert addition(2,1) == 4



