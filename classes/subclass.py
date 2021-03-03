# -- coding: UTF-8 --

"""
Given classes A and B, B being a subclass of A, show how you will construct
an instance of A given an instance of B. Can you construct an instance of B
given an instance of A? If yes, show.
"""

import logging
import logging.config
import json

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class SuperClass:
    """
    Class Description: This is going to be our superclass for which sub classes can be created
    """

    def meth_a(self):
        """
        Function Description: To show that the derived instance is able to call the method

        """
        LOGGER.info("Accessed using object of Super Class: %s", {type(self)})


class SubClass(SuperClass):
    """
    Class Description: This is going to be our subclass
    """

    def print_base(self):
        for base in self.__class__.__bases__:
            print(base.__name__)

    def meth_b(self):
        """
        Function Description: To show that the derived instance is able to call the method

        """
        LOGGER.info("Accessed using object of Sub Class %s", {type(self)})

    def change_class(cls):
        print(super().__class__)
        return cls


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
    """ Main Function """
    setup_logging()

    # Creating instance of subclass using superclass instance
    a_1 = SuperClass()
    b_1 = a_1.__class__.__subclasses__()[0]()
    LOGGER.info("Type of b1 is: %s", type(b_1))

    b_2 = SubClass()
    # b_2.__class__ = SuperClass
    # b_2.meth_a()
    a_2 = b_2.__class__.__base__()
    LOGGER.info("Type of a2 is: %s", type(a_2))


if __name__ == '__main__':
    main()
