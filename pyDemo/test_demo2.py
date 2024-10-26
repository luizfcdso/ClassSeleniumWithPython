# Any pytest file should start with test_
# pytest method names should start with test as well
import pytest

def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed becuase strings do not match"

def testSecoundCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Addition do not match"

    

