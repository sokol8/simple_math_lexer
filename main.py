from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
	try: 
		text = input("calc > ")

		lexer = Lexer(text)
		tokens = lexer.generate_tokens()

		# print(list(tokens))
		# continue

		parser = Parser(tokens)
		tree = parser.parse()

		# print(tree)
		# continue

		if not tree: continue

		interpreter = Interpreter()
		value = interpreter.visit(tree)

		print(value)
	except Exception as e:
		print(e)