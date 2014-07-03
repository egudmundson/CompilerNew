from SymbolTable import *
import Lexical
import os


class Syntax():
	def __init__(self,lexicalAnalysis):
		self.Lexical = lexicalAnalysis
		self.SymbolTable = SymbolTable()
		self.FirstPass = None

	def run(self,firstPass =True):
		if(firstPass):	
			self.Lexical.Run()
		else:
			self.Lexical.reset();
		self.FirstPass = firstPass
		try:
			self.Compilation_Unit()
		except SyntaxException as e:
			print e.msg
			exit(0)
	def TossError(self,ExpectedValue):
		retStr = ""
		token = lexical.getToken()
		retStr += "Was Expecting %s Received %s on line %d" ( ExpectedValue, lexical.lexem, lexem.line ) 
		return retStr
	def Compilation_Unit(self):
		while(ClassDeclaration()):
			self.Lexical.GetNextToken()
		if(self.Lexical.getToken() == "void"):
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem == "main"):

			else:
				raise Exception(self.TossError("main"))

		else:
			raise Exception(self.TossError("void"))

	def ClassDeclaration(self):
		if(self.Lexical.getToken().lexical != "class"):
			return False
		
		if(self.FirstPass):

		else:
			
