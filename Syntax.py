import SymbolTable


class Syntax():
	def __init__(self,lexicalAnalysis):
		self.Lexical = lexicalAnalysis
		self.SymbolTable = SymbolTable.SymbolTable()

	def run(self,firstPass =True):
		if(firstPass):
			print "FirstPass"
