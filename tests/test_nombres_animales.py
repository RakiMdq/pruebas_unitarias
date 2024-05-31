import allure
from animales import obtener_nombres_animales



@allure.description("Test donde se genera una lista de animales")
@allure.feature("Animales")
@allure.epic("Lista de animales")

def test_obtener_nombre():
    nombres = obtener_nombres_animales()
    assert isinstance(nombres,list)
