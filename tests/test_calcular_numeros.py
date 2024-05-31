import allure
from calcular_numeros import calcular_promedio


@allure.description("Test donde se promedia")
@allure.feature("Promedio")
@allure.epic("Promedio")

def test_calcular_promedio():
    numeros = [1,2,3,4,5]
    resultado = calcular_promedio(numeros)
    assert resultado == 3
