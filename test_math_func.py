import math_func
import pytest
import sys

# @pytest.mark.skipif(sys.version_info>(3,3),reason="just like that")
def test_add():
    assert math_func.add(6,4)==10
    assert math_func.add(2,2)==4

# @pytest.mark.num
# def test_mul():
#     assert math_func.mul(4,4)==16
#     assert math_func.mul(5,2) == 10
#
# @pytest.mark.string
# def test_add_string():
#     result=math_func.add("Hello ","World")
#     assert result=="Hello World"
#     assert "Hello" in result
#
# @pytest.mark.string
# def test_mul_string():
#     assert math_func.mul("Hello ",2)=="Hello Hello "
#     print("Yay")
#
# @pytest.mark.parametrize("a,b,result",
#                          [(2,3,5),("Hello ","World","Hello World"),(4.4,1.6,6)]
#                          )
#
# def test_add(a,b,result):
#     assert math_func.add(a,b)==result