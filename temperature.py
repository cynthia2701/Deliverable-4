#Task 1: Temperatures
class Temperature: 

    tolerance = 1e-9


    def __init__(self, value: float | int, unit: str = 'C') -> None:
        """
        Temperature is initialized with value and unit. Unit is case-insensitive. 
        ValueError returned if unit is not valid, or if temperature is below
        absolute zero. 

        Args: 
        value (float|int): Magnitiude of temperature. 
        unit: str: Unit of temperature. 

        Return: Value and unit of temperature. 
        """
        unit_upper = unit.upper()
        valid_unit = ['C', 'F', 'K']
        if unit_upper not in valid_unit:
            raise ValueError("Unit must be 'C', 'F', or 'K'.")

        self._value = float(value)
        self._unit = unit_upper

        if self.to_kelvin() < -self.tolerance:
            raise ValueError("Temperature in Kelvin cannot be negative")


    @property
    def value(self) -> float:
        """Returns temperature value as read only."""
        return self._value


    @property
    def unit(self) -> str:
        """Returns temperature unit as read only."""
        return self._unit


    # Conversion methods: 


    def to_celsius(self) -> float:
        """
        Calculate and returns the temperature in Celsius. 
        """
        if self.unit == 'C':
            return self.value
        elif self.unit == 'K':
            return self.value - 273.15
        elif self.unit == 'F':
            return (self.value - 32) * 5 / 9

    
    def to_fahrenheit(self) -> float:
        """
        Calculates and returns the temperature in Fahrenheit.
        """
        if self.unit == 'C':
            return (self.value * 9 / 5) + 32
        elif self.unit == 'K':
            return (self.value - 273.15) * 9 / 5 + 32
        elif self.unit == 'F':
            return self.value


    def to_kelvin(self) -> float:
        """
        Calculates and returns the temperature in Kelvin.
        """
        if self.unit == 'C':
            return self.value + 273.15
        elif self.unit == 'K':
            return self.value
        elif self.unit == 'F':
            return (self.value - 32) * 5 / 9 + 273.15


    def convert_to(self, target_unit: str) -> 'Temperature':
        """
        A new temperature is returned and converted to the target unit. 

        Args: 
        target_unit (str): Target temperature unit. C, F, or K. 
        Returns: Temperature with updated unit and value. 
        """
        target_unit = target_unit.upper()
        valid_unit = ['C', 'F', 'K']
        if target_unit not in valid_unit:
            raise ValueError("Invalid unit. Must be 'C', 'F', or 'K'.")

        if target_unit == self.unit:
            return Temperature(self.value, self.unit) # if already in wanted unit
        if target_unit == 'C':
            return Temperature(self.to_celsius(), 'C')
        elif target_unit == 'F':
            return Temperature(self.to_fahrenheit(), 'F')
        elif target_unit == 'K':
            return Temperature(self.to_kelvin(), 'K')


# String representations 


    def __repr__(self) -> str:
        """
        Returns a string with temperature value and unit.
        """
        return f"Temperature({self.value}, '{self.unit}')"


    def __str__(self) -> str:
        """
        Returns a human-readable string with temperature value and unit.
        Formatted to two decimal places.
        """
        if self.unit == "K":
            return f"{self.value:.2f} K"
        return f"{self.value:.2f} °{self.unit}"

    
# Comparisons. Comparing temperature across units.


    def _equal_temp(self, other: "Temperature") -> bool:
        """
        Converts two temperature instances to Kelvin and checks
        if their difference is less or equal to the tolerance value. 
        If they are, they are seen as the same value.
        """
        return abs(self.to_kelvin() - other.to_kelvin()) <= self.tolerance


    def __eq__(self, other: object) -> bool:
        """
        Handles == (equal).
        Stops if other is not a Temperature object.
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return self._equal_temp(other) #calls _equal_temp to check if they are the same.


    def __ne__(self, other: object) -> bool: 
        """
        Handles != (not equal).
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return not self._equal_temp(other)


    def __lt__(self, other: object) -> bool: 
        """
        Handles < (less than).
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        #other has to be bigger than self by more than tolerance value.
        return (other.to_kelvin() - self.to_kelvin()) > self.tolerance


    def __le__(self, other: object) -> bool:
        """
        Handles <= (less than or equal to).
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        # if self or other are withhin the tolerance , or self is lower than other. 
        return self._equal_temp(other) or (self.to_kelvin()) < other.to_kelvin()


    def __gt__(self, other: object) -> bool:
        """
        Handles > (greater than).
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        return (self.to_kelvin() - self.tolerance) > other.to_kelvin()


    def __ge__(self, other: object) -> bool: 
        """
        Handles >= (greater than or equal to).
        """
        if not isinstance(other, Temperature):
            return NotImplemented
        # if self or other are within the tolerance, or self is higher than other. 
        return self._equal_temp(other) or (self.to_kelvin() > other.to_kelvin())
    