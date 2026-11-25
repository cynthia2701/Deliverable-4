#Task 1: Temperatures

class Temperature: 

    tolerance = 1e-9


    def __init__(self, value: float | int, unit: str = 'C') -> None:
        #upper case the unit, else ValueError, or if temp is below 0K
        unit_upper = unit.upper()
        if unit_upper not in ['C', 'F', 'K']:
            raise ValueError(f"Invalid unit: {unit}. Must be 'C', 'F', or 'K'.")

        self._value = float(value)
        self._unit = unit_upper

        if self.to_kelvin() < -self.tolerance:
            raise ValueError(f"Temperature in Kelvin cannot be negative: {value}")


    @property
    def value(self) -> float:
        """Returns temperature value as read only."""
        return self._value


    @property
    def unit(self) -> str:
        """Returns temperature unit as read only."""
        return self._unit


    #conversion methods: 


    def to_celsius(self) -> float:
        if self.unit == 'C':
            return self.value
        elif self.unit == 'K':
            return self.value - 273.15
        elif self.unit == 'F':
            return (self.value - 32) * 5 / 9

    
    def to_fahrenheit(self) -> float:
        if self.unit == 'C':
            return (self.value * 9 / 5) + 32
        elif self.unit == 'K':
            return (self.value - 273.15) * 9 / 5 + 32
        elif self.unit == 'F':
            return self.value


    def to_kelvin(self) -> float:
        if self.unit == 'C':
            return self.value + 273.15
        elif self.unit == 'K':
            return self.value
        elif self.unit == 'F':
            return (self.value - 32) * 5 / 9 + 273.15


    def convert_to(self, target_unit: str) -> Temperature:
        target_unit = target_unit.upper()
        if target_unit not in ['C', 'F', 'K']:
            raise ValueError(f"Invalid unit: {target_unit}. Must be 'C', 'F', or 'K'.")

        if target_unit == self.unit:
            return Temperature(self.value, self.unit)
        if target_unit == 'C':
            return Temperature(self.to_celsius(), 'C')
        elif target_unit == 'F':
            return Temperature(self.to_fahrenheit(), 'F')
        elif target_unit == 'K':
            return Temperature(self.to_kelvin(), 'K')


#string representations 


    def __repr__(self) -> str:
        """Returns a string with temperature value and unit."""
        return f"Temperature({self.value}, '{self.unit}')"


    def __str__(self) -> str:
        """Returns a human-readable string with temperature value and unit."""
        if self.unit == "K":
            return f"{self.value:.2f} K"
        return f"{self.value:.2f} °{self.unit}"
    
#cross-unit comparisons


    def _equal_temp(self, other: Temperature) -> bool:
        return abs(self.to_kelvin() - other.to_kelvin()) <= self.tolerance


    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._equal_temp(other)


    def __ne__(self, other: object) -> bool: 
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self._equal_temp(other)


    def __lt__(self, other: object) -> bool: 
        if not isinstance(other, Temperature):
            return NotImplemented
        return (other.to_kelvin() - self.to_kelvin()) > self.tolerance


    def __le__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._equal_temp(other) or (self.to_kelvin()) < other.to_kelvin()


    def __gt__(self, other: object) -> bool:
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin() - self.tolerance) > other.to_kelvin()


    def __ge__(self, other: object) -> bool: 
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._equal_temp(other) or (self.to_kelvin() > other.to_kelvin())
    