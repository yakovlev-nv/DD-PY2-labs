# TODO Написать 3 класса с документацией и аннотацией типов
import doctest
from typing import Union


class MoneyBank:
    """ Класс "копилка" c двумя атрибутами: вместимость и кол-во монет внутри
    >>> bank = MoneyBank(120,0)
    """
    
    def __init__(self, capacity:int, coins_inside:int):
        # capacity - вместимость копилки, coins_inside - кол-во монет внутри
        if not  isinstance(capacity,int):
            raise TypeError
        if not isinstance(coins_inside,int):
            raise TypeError
        self.capacity = capacity
        self.coins_inside = coins_inside

    def add(self, coins:int):
        # Добавить монет в копилку, если достаточно места
        if not isinstance(coins,int):
            raise TypeError
        if not (self.capacity - self.coins_inside) >= coins:
            raise ValueError
        else:
            self.coins_inside += coins

    def get(self, coins:int):
        # Достать указанное количество монет из копилки, если внутри есть такое количество
        if not isinstance(coins, int):
            raise TypeError
        if not self.coins_inside > coins:
            raise ValueError
        else:
            self.coins_inside -= self.coins


class ElectricKettle:
    """ Класс электрический чайник с тремя атрибутамии - емкость, включен или нет и объем воды внутри
    >>> kettle = ElectricKettle(2, 0.5)
    """
    
    def __init__(self, max_volume: Union[int, float],water_inside: Union[int, float]):
        self.max_volume = max_volume
        self.water_inside = water_inside
        if not isinstance(max_volume, (int, float)):
            raise TypeError
        if not isinstance(water_inside, (int, float)):
            raise TypeError
            
    def add_water(self, water:Union[int, float]):
        # налить воды в чайник
        if not isinstance(water, (int, float)):
            raise TypeError
        if (water + self.water_inside) > self.max_volume:
            raise ValueError
        else:
            self.water_inside += water
            
    def pour_water(self, water:Union[int, float]):
        # вылить воду из чайника
        if not isinstance(water, (int, float)):
            raise TypeError
        if water > self.water_inside:
            raise ValueError
        else:
            self.water_inside -= water
            
            
class TV:
    """Класс телевизор с двумя аттрибутами - длина диагонали разрешение экрана
    >>> tv = TV(55,'FullHD')
    """
    
    def __init__(self, diagonal:Union[int, float], resolution:str):
        self.diagonal = diagonal
        self.resolution = resolution
        if not isinstance(diagonal, (int, float)):
            raise TypeError
        if not isinstance(resolution, str):
            raise TypeError
            
    def turn_on(self):
        # включить телевизор
        ...
        
    def switch_channel(self):
        # проверка если теелвизор включен, то переключить канал
        ...
        
        
if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
