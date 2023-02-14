from typing import Union
class Kettle:
    """класс Чайник"""
    def __init__(self, volume: Union[int, float], water_inside: Union[int, float]):
        """
        @param volume: объем чайника
        @type volume: Union[int,float]
        @param water_inside: объем воды в чайнике
        @type water_inside: Union[int,float]
        """
        self.volume = volume
        self.water_inside = water_inside
        if volume < water_inside:
            raise ValueError
    def pour_water(self, water:Union[int,float]):
        """Надить воды в чайник"""
        if water + self.water_inside < self.volume:
            self.water_inside += water
        else:
            raise ValueError
    def use_kettle(self):
        """Поставить чайник на огонь"""
        ...
    def __str__(self):
        return f"Чайник объемом {self.volume}, объем воды внутри: {self.water_inside}"
    def __repr__(self):
        return f"{self.__class__.__name__}(volume = {self.volume}, water_inside = {self.water_inside})"
class ElectricKettle(Kettle):
    """Класс Электрический чайник"""
    def __init__(self, volume: Union[int, float], water_inside: Union[int, float]):
        """
        @param volume: объем чайника
        @type volume: Union[int,float]
        @param water_inside: объем воды в чайнике
        @type water_inside: Union[int,float]
        """
        super().__init__(volume, water_inside)
    def pour_water(self, water: Union[int, float]):
        """Надить воды в чайник"""
        if water + self.water_inside < self.volume:
            self.water_inside += water
        else:
            raise ValueError
    def use_kettle(self):
        """ Включить чайник, перегруженный метод, причина перегрузки - другой принцип работы."""
        ...

    def __str__(self):
        return f"Электрический чайник объемом {self.volume}, объем воды внутри: {self.water_inside}"
    def __repr__(self):
        return f"{self.__class__.__name__}(volume = {self.volume}, water_inside = {self.water_inside})"



if __name__ == "__main__":
    
    pass
