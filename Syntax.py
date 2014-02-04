import SymbolTable
import Lexical

class Syntax():
	def __init__(self,lexicalAnalysis):
		self.Lexical = lexicalAnalysis
		self.SymbolTable = SymbolTable.SymbolTable()
		self.FirstPass = None

	def run(self,firstPass =True):
		if(firstPass):	
			self.Lexical.Run()
		else:
			self.Lexical.reset();
		self.FirstPass = firstPass
		self.Expression()
		print "First Run"
	def Expression(self):
		if(self.Lexical.getToken().lexem == "("):
			self.Lexical.GetNextToken()
			self.Expression()
			self.getNextToken()
			if(self.Lexical.getToken()   

tmp = Syntax(Lexical.LexAnalyzer("test.re","test.kxi"))

tmp.run()
