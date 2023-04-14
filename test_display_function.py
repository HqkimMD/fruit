from function import display_fruit_price
import pytest


@pytest.mark.display #pytest -m display
@pytest.mark.parametrize('fruit_type,weight,expected_result', [
    ("orange",1,75),("orange",1.5,112.5),("orange",0.5,37.5),
    ("mango",1,80),("mango",2.5,200),("mango",0.25,20),
    ("watermelon",1,50),("watermelon",2,100),("watermelon",0.75,37.5),
    ("coconut",0.75,"Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0"),
    ("banana",0.75,"Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0" ),
    ("watermelon",-1,"Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0"),
    ("watermelon",-100,"Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0"),
    ("watermelon",0.2500,12.5)


])
def test_display(fruit_type,weight, expected_result):
    actual_result = display_fruit_price(fruit_type,weight)
    assert expected_result == actual_result