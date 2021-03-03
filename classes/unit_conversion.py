# -- coding: UTF-8 --

""" Construct classes which will allow you to store units and perform direct unit
conversion
"""

import argparse
import logging
import logging.config
import json

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class Quantities:
    def __init__(self, name, units):
        self.name = name
        self.units = units


class Units:
    value = 10
    millimeter = 'mm'
    centimeter = 'cm'
    decimeter = 'decimeter'
    meter = 'm'
    dekameter = 'dekameter'
    hectometer = 'hectometer'
    kilometer = 'kilometer'
    foot = 'ft'
    mile = 'mile'
    inch = 'in'
    second = 'sec'
    minute = 'minute'
    hour = 'hr'
    day = 'day'
    bar = 'bar'
    pascal = 'pascal'
    atm = 'atm'
    psi = 'pounds_per_sq_inch'
    torr = 'torr'
    milligrams = 'mg'
    grams = 'g'
    ton = 'ton'
    lb = 'lb'
    ounces = 'oz'
    kelvin = 'kelvin'
    celcius = 'celsius'
    fahrenheit = 'fahrenheit'


class UnitConversionData:
    def __init__(self, data):
        self.__dict__ = data

    def __repr__(self):
        return "%s" % self.__dict__


class UnitConversion:
    def __init__(self, value, unit_1, unit_2, conversion_data):
        self.unit_1 = unit_1
        self.unit_2 = unit_2
        self.value = value
        self.conversion_data = conversion_data

    def convert(self):

        if self.unit_2 == self.unit_1:
            return self.value

        if self.unit_1 == 'celsius' and self.value > 0:
            if self.value > -273.15:
                if self.unit_2 == 'fahrenheit':
                    return (self.value*9/5) + 32
                elif self.unit_2 == 'kelvin':
                    return self.value + 273.15
            else:
                raise ValueError("Celsius value cant be lesser than -273.15")

        if self.unit_1 == 'fahrenheit':
            if self.value>-459.67:
                if self.unit_2 == 'celsius':
                    return (self.value - 32)*5/9
                elif self.unit_2 == 'kelvin':
                    return (self.value - 32)*5/9 + 273.15
            else:
                raise ValueError("Fahrenheit value cant be lesser than -459.67")

        if self.unit_1 == 'kelvin':
            if self.value>0:
                if self.unit_2 == 'fahrenheit':
                    return (self.value - 273.15)*9/5 + 32
                elif self.unit_2 == 'celsius':
                    return self.value - 273
            else:
                raise ValueError("Kelvin value cant be negative")

        else:
            if self.value>0:
                return self.value * self.conversion_data.Values[self.unit_1][self.unit_2]
            else:
                raise ValueError("The value cant be negative")


def setup_logging(default_path=LOGGER_CONFIG_PATH):
    """
    Function Description: To setup logging using the json file
    :param default_path: Path of the configuration file
    :type default_path: str
    """
    with open(default_path, 'rt') as file:
        config = json.load(file)
    logging.config.dictConfig(config)


def main():
    """Main function"""
    setup_logging()

    with open('conversions.json') as file:
        data = json.load(file)
    obj = UnitConversionData(data)

    inp_value = 20

    unit_1 = Units.fahrenheit
    unit_2 = Units.milligrams

    try:
        obj = UnitConversion(inp_value, unit_1, unit_2, obj)
        final_value = obj.convert()
        LOGGER.info(final_value)
    except KeyError:
        LOGGER.info("Enter the units of same quantity")


if __name__ == "__main__":
    main()
