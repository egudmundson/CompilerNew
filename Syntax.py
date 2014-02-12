import SymbolTable
import Lexical

def TossError(Syntax,Expected):
	return "Recevied %s on line %d Expected %s "%(Syntax.Lexical.GetNextToken().lexem,Syntax.Lexical.GetNextToken().line,Expected)
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
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ")"):
				raise Exception(TossError(self,")"));	
			self.Lexical.GetNextToken()
			try:
				self.expressionz()
			except Exception e:
				self.HandleException(e)
	def expressionz(self):
		if(self.Lexical.getToken.lexem == "="):
			self.Lexical.GetNextToken()
			try:
				self.assignment_expression()
			except Exception e:
				raise Exception("%s"%e.message)
		elif(self.Lexical.getToken.lexem =="&&"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="||"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="=="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="!="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="<="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem ==">="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="<"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)

		elif(self.Lexical.getToken.lexem ==">"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="+"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="-"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="*"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="/"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				self.HandleException(e)
		else:
			raise Exception(TossError(self,"expressionz Expected"))

	def assignment_expression(self):
		self.Lexical.GetNextToken()
		try: 
			self.Expression()
		except Exception e:
			if(self.Lexical.getToken().lexem =="this"):
				return
			if(self.Lexical.getToken().lexem == "new"):
				try:
					self.Lexical.GetNextToken()
					self.type()
					self.Lexical.GetNextToken()
					self.new_declaration()

				except Exception e:
					self.HandleException(e)

			if(self.Lexical.getToken().lexem == "atoi"|| self.Lexical.getToken().lexem =="itoa"):
				self.lexical.GetNextToken()
				try:
					self.Expression()
				except Exception e: 
					self.HandleException(e)
			
	def type(self):
		if(self.Lexical.GetToken().lexem == "int" || self.Lexical.GetToken().lexem == "char" ||self.Lexical.GetToken().lexem == "bool" || self.Lexical.GetToken().lexem == "void" || self.ClassNameExists()):
			return
		else 
			raise Exception(TossError(self,"Type")
	def ClassNameExists(self):
		return self.SymbolTable.Exists(self.Lexical.GetToken().lexem)	
	def new_declaration(self):
		if(self.Lexical.GetToken().lexem == "("):
			self.Lexical.GetNextToken()
			try:
				self.argument_list()
			except Exception e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.GetToken().lexem != ")"):
				raise Exception(TossError(self,")"))
		if(self.Lexical.GetToken().lexem == "["):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception e:
				 self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.GetToken().lexem != "]"):
				raise Exception(TossError(self,"]"))
	def argument_list(self):
		print "STUB"

tmp = Syntax(Lexical.LexAnalyzer("test.re","test.kxi"))

tmp.run()
