# from ast import Num
import unittest

from tokens import Token, TokenType
from parser_ import Parser
from nodes import *
from lexer import Lexer

class TestParser(unittest.TestCase):

    def test_empty(self):
        tokens = []
        node = Parser(tokens).parse()
        self.assertEqual(node, None)

    def test_numbers(self):
        tokens = [Token(TokenType.NUMBER, 51.2)]
        node = Parser(tokens).parse()
        self.assertEqual(node, NumberNode(51.2))

    def test_individual_operations(self):
        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SubstractNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MultiplyNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, DivideNode(NumberNode(27), NumberNode(14)))

        tokens = [
            Token(TokenType.MINUS),
            Token(TokenType.NUMBER, 14),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, MinusNode(NumberNode(14)))

        tokens = [
            Token(TokenType.SQRT),
            Token(TokenType.NUMBER, 256),
        ]
        node = Parser(tokens).parse()
        self.assertEqual(node, SqrtNode(NumberNode(256)))

    def test_full_expression(self):
        tokens = list(Lexer("27 + (43 / 36 - sqrt(48) ) * .51").generate_tokens())
        self.assertEqual(tokens, [
            Token(TokenType.NUMBER, 27),
            Token(TokenType.PLUS),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 43),
            Token(TokenType.DIVIDE),
            Token(TokenType.NUMBER, 36),
            Token(TokenType.MINUS),
            Token(TokenType.SQRT),
            Token(TokenType.LPAREN),
            Token(TokenType.NUMBER, 48),
            Token(TokenType.RPAREN),
            Token(TokenType.RPAREN),
            Token(TokenType.MULTIPLY),
            Token(TokenType.NUMBER, 0.51),
        ])

        node = Parser(tokens).parse()
        self.assertEqual(node, AddNode(
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
        ))





