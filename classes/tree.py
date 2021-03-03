# -- coding: UTF-8 --

""" Implement a tree and store its information in the class """

import argparse
import logging
import logging.config
import json

__author__ = 'saranya@gyandata.com'

LOGGER = logging.getLogger('root')
LOGGER_CONFIG_PATH = 'config/logging.json'


class Tree:
    """Class Description: To implement tree data structure using classes"""
    def __init__(self, name):
        self.parent = None
        self.child = []
        self.name = name

    def add_children(self, c_obj):
        """
        Method Description: To assign the parent to the class instance
        :param c_obj: Child object
        :type c_obj: list
        """
        for child in c_obj:
            self.child.append(child)
            child.parent = self.name

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.name) + "\n"
        for child in self.child:
            ret += child.__str__(level + 1)
        return ret


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
    """Main Function"""
    setup_logging()
    obj_1 = Tree('Parent')
    print(obj_1.name)

    children = [Tree("child1"), Tree("child2"), Tree("child3")]
    obj_1.add_children(children)
    print(obj_1.child[0].parent)

    g_child = [Tree("newborn1"), Tree("newborn2")]
    children[0].add_children(g_child)

    g_child_1 = [Tree("newbie2")]
    children[1].add_children(g_child_1)
    print(obj_1)


if __name__ == "__main__":
    main()
