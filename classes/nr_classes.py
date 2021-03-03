# -- coding: UTF-8 --

""" Reimplement the newton raphson method using classes. The objective is that
the class will store the function value, gradient value, iteration number and
value of the root. When print is invoked on this class instance it has to print all
the information of the class
"""

import logging
import logging.config
import argparse
import json

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class NewtonRaphson:
    """
    Class Description: To implement newton raphson method to find the roots of polynomial
    """
    def __init__(self, poly, x, flag):     # initial value of x
        """ Constructor """
        self.poly = poly
        self.x = x
        self.flag = flag
        self.derivative = 0
        self.count = 0
        self.flag_root = True
        self.residual = 0.001
        self.save_values = {}

    def deriv(self):
        """
        Function Description: To find the derivative of the polynomial
        :return: Derivative value
        :rtype: float
        """
        total = 0
        for i in range(len(self.poly) - 1):
            total = total + self.poly[i] * (len(self.poly) - i - 1) * self.x ** (len(self.poly) - i - 2)

        return total

    def func_value(self):
        """
        Function Description: To find the value of the polynomial
        :return: Polynomial value
        :rtype: float
        """
        order = len(self.poly)
        tot = 0
        for i in range(order):
            tot = tot * self.x + self.poly[i]
        return tot

    @property
    def find_root(self):
        """
        Function Description: To find the root of the polynomial using newton raphson
        :return: Value of root and the boolean value if root is present
        :rtype: Union['float', 'bool']
        """

        try:
            self.residual = self.func_value() / self.deriv()
        except ZeroDivisionError:
            LOGGER.error("Tried to divide by zero")
            self.x += 10e-15
            self.residual += 0.001

        while abs(self.residual) >= 0.00001:  # make it user defined(optional)
            self.residual = self.func_value() / self.deriv()

            # x(i+1) = x(i) - f(x) / f'(x)
            self.x = self.x - self.residual
            self.count = self.count + 1
            if self.count > 100:  # make it user defined
                self.flag_root = False
                break
            self.save_values.__setitem__(self.count, [self.x, self.residual, self.func_value(), self.deriv()] )
        return self.x, self.flag_root

    def __str__(self):
        return "Root: %f, Iteration no: %f, Function value: %f,Gradient value: %f" % (self.x, self.count,
                                                                                      self.func_value(), self.deriv())

    def print(self):
        LOGGER.info("The function, gradient values and root and residual error for each iteration are:")
        for key, value in self.save_values.items():
            LOGGER.info("Iteration number: %f, Root: %f, Residual error: %f, Function value: %f, Derivative value: %f" % (key, value[0],value[1], value[2], value[3]))


def arg_parse():
    """
    Function Description: To parse command line arguments

    :return: command line arguments passed
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', nargs="+", type=float)
    parser.add_argument('-x', help="Initial value of x", type=float)
    parser.add_argument("-v", "--verbose", help="print extra values", default=0,
                        action="store_true")
    return parser.parse_args()


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
    """ Main function """
    setup_logging()
    args = arg_parse()
    polynomial = args.p
    x = args.x
    flag = args.verbose
    obj = NewtonRaphson(polynomial, x, flag)
    root, flag_root = obj.find_root
    obj.print()            # should be obj.print()

    print(obj.save_values)


if __name__ == "__main__":
    main()
