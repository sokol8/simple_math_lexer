from ast import Num
import unittest
from unittest import result
from nodes import *
from interpreter import Interpreter
from values import Number

class TestInterpreter(unittest.TestCase):

    def test_numbers(self):
        value = Interpreter().visit(NumberNode(51.2))
        self.assertEqual(value, Number(51.2))

    def test_individual_operations(self):
        value = Interpreter().visit(AddNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(value, Number(41))

        value = Interpreter().visit(SubstractNode(NumberNode(27), NumberNode(14)))
        self.assertEqual(value, Number(13))

        value = Interpreter().visit(MultiplyNode(NumberNode(10), NumberNode(12)))
        self.assertEqual(value, Number(120))

        value = Interpreter().visit(DivideNode(NumberNode(120), NumberNode(12)))
        self.assertEqual(value, Number(10))

        value = Interpreter().visit(SqrtNode(NumberNode(256)))
        self.assertEqual(value, Number(16))

        with self.assertRaises(Exception):
            Interpreter().visit(DivideNode(NumberNode(27), NumberNode(0)))

    def test_full_expression(self):
        # "27 + (43 / 36 - sqrt(48) ) * .51"
        tree = AddNode(
            NumberNode(27),
            MultiplyNode(
                SubstractNode(
                    DivideNode(
                        NumberNode(43),
                        NumberNode(36)
                    ),
                    SqrtNode(
                        NumberNode(48)
                    )
                ),
                NumberNode(0.51)
            )
        )

        result = Interpreter().visit(tree) 
        self.assertAlmostEqual(result.value, 24.07578, 5)
        


