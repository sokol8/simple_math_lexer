import logging

from tokens import TokenType
from nodes import *

logging.basicConfig(level=logging.DEBUG, format='[%(levelname)s] %(funcName)s: %(message)s',)

class Parser:
	def __init__(self, tokens):
		self.tokens = iter(tokens)
		self.advance()

	def raise_error(self, msg='error'):
		raise Exception("Invalid Syntax: " + msg)

	def advance(self):
		try:
			self.current_token = next(self.tokens)
		except StopIteration:
			self.current_token = None

	def parse(self):
		logging.debug('parsing starts')
		if self.current_token == None:
			return None

		result = self.expr()

		if self.current_token != None:
			self.raise_error("Somethin went wrong")

		return result

	def expr(self):
		result = self.term()

		while self.current_token != None and self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
			if self.current_token.type == TokenType.PLUS:
				self.advance()
				result = AddNode(result, self.term())
			elif self.current_token.type == TokenType.MINUS:
				self.advance()
				result = SubstractNode(result, self.term())

		return result

	def term(self):
		result = self.factor()

		while self.current_token != None and self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
			if self.current_token.type == TokenType.MULTIPLY:
				self.advance()
				result = MultiplyNode(result, self.factor())
			elif self.current_token.type == TokenType.DIVIDE:
				self.advance()
				result = DivideNode(result, self.factor())

		return result

	def factor(self):
		token = self.current_token

		if token.type == TokenType.LPAREN:
			self.advance()
			result = self.expr()

			if self.current_token == None or self.current_token.type != TokenType.RPAREN:
				self.raise_error("No Right Parethesis in place")

			self.advance()  # RPAREN found
			return result

		if token.type == TokenType.NUMBER:
			self.advance()
			return NumberNode(token.value)
		elif token.type == TokenType.PLUS:
			self.advance()
			return PlusNode(self.factor())
		elif token.type == TokenType.MINUS:
			self.advance()
			return MinusNode(self.factor())
		elif token.type == TokenType.SQRT:
			self.advance()
			return SqrtNode(self.factor())

		self.raise_error("Factor not found")


