from function import calculate_fruit_price, validate_input
import pytest

#test-case 9 test case
@pytest.mark.code #pytest -m code
def test_orenge_1kg():
    weight = 1
    fruit = 'orange'
    expected_result = 75
    actual_result = calculate_fruit_price(fruit,weight)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_orenge_1dot5kg():
    weight = 1.5
    fruit = 'orange'
    expected_result = 112.5
    actual_result = calculate_fruit_price(fruit,weight)
    print(actual_result)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_orenge_0dot5kg():
    weight = 0.5
    fruit = 'orange'
    expected_result = 37.5
    actual_result = calculate_fruit_price(fruit,weight)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_mango_1kg():
    weight = 1
    fruit = 'mango'
    expected_result = 80
    actual_result = calculate_fruit_price(fruit,weight)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_mango_2dot5kg():
    weight = 2.5
    fruit = 'mango'
    expected_result = 200
    actual_result = calculate_fruit_price(fruit,weight)
    print(actual_result)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_mango_0dot25kg():
    weight = 0.25
    fruit = 'mango'
    expected_result = 20
    actual_result = calculate_fruit_price(fruit,weight)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_watermelon_1kg():
    weight = 1
    fruit = 'watermelon'
    expected_result = 50
    actual_result = calculate_fruit_price(fruit,weight)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_watermelon_2kg():
    weight = 2
    fruit = 'watermelon'
    expected_result = 100
    actual_result = calculate_fruit_price(fruit,weight)
    print(actual_result)
    assert expected_result == actual_result

@pytest.mark.code #pytest -m code
def test_watermelon_0dot75kg():
    weight = 0.75
    fruit = 'watermelon'
    expected_result = 37.5
    actual_result = calculate_fruit_price(fruit,weight)
    assert expected_result == actual_result

#validate 5 validate
@pytest.mark.validate #pytest -m validate
def test_banana():
    weight = 0.75
    fruit = 'banana'
    expected_result = "Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0" 
    actual_result = validate_input(fruit,weight)
    assert expected_result == actual_result 

@pytest.mark.validate #pytest -m validate
def test_coconut():
    weight = 0.75
    fruit = 'coconut'
    expected_result = "Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0" 
    actual_result =  validate_input(fruit,weight)
    assert expected_result == actual_result 

@pytest.mark.validate #pytest -m validate
def test_weight_minus1():
    weight = -1
    fruit = 'watermelon'
    expected_result = "Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0" 
    actual_result = validate_input(fruit,weight)
    assert expected_result == actual_result 

@pytest.mark.validate #pytest -m validate
def test_weight_minus100():
    weight = -100
    fruit = 'watermelon'
    expected_result = "Invalid fruit type. Must be one of 'orange', 'mango', or 'watermelon' and Weight must be greater than 0" 
    actual_result = validate_input(fruit,weight)
    assert expected_result == actual_result 

@pytest.mark.validate #pytest -m validate
def test_weight_0dot365665():
    weight = 0.2500
    fruit = 'watermelon'
    expected_result = 12.5
    actual_result = validate_input(fruit,weight)
    assert expected_result == actual_result 