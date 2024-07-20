from abc import ABC, abstractmethod
from decimal import Decimal

class CampingType(ABC):
    @abstractmethod
    def get_weight(self):
        pass
    

class ElectricCamping(CampingType):
    def get_weight(self):
        return Decimal(2/3)
    

class PrimitiveCamping(CampingType):
    def get_weight(self):
        return Decimal(1/3)