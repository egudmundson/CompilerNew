import SymbolTable
import Lexical

def TossError(Syntax,Expected):
	return "Recevied %s on line %d Expected %s "%(Syntax.Lexical.getToken().lexem,Syntax.Lexical.getToken().line,Expected)
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
		self.Compilation_Unit()
		print "First Run"
	def HandleException(self, exception):
		print str(exception)
		exit(0)
	def Expression(self):
		if(self.Lexical.getToken().lexem == "("):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ")"):
				raise Exception(TossError(self,")"));	
			self.Lexical.GetNextToken()
			try:
				self.expressionz()
			except Exception as e:
				self.HandleException(e)
	def expressionz(self):
		if(self.Lexical.getToken.lexem == "="):
			self.Lexical.GetNextToken()
			try:
				self.assignment_expression()
			except Exception as e:
				raise Exception("%s"%e.message)
		elif(self.Lexical.getToken.lexem =="&&"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="||"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="=="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="!="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="<="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem ==">="):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="<"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)

		elif(self.Lexical.getToken.lexem ==">"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="+"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="-"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="*"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken.lexem =="/"):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
		else:
			raise Exception(TossError(self,"expressionz Expected"))

	def assignment_expression(self):
		self.Lexical.GetNextToken()
		try: 
			self.Expression()
		except Exception as e:
			if(self.Lexical.getToken().lexem =="this"):
				return
			if(self.Lexical.getToken().lexem == "new"):
				try:
					self.Lexical.GetNextToken()
					self.type()
					self.Lexical.GetNextToken()
					self.new_declaration()

				except Exception as e:
					self.HandleException(e)

			if(self.Lexical.getToken().lexem == "atoi"or self.Lexical.getToken().lexem =="itoa"):
				self.lexical.GetNextToken()
				try:
					self.Expression()
				except Exception as e: 
					self.HandleException(e)
			
	def type(self):
		if(self.Lexical.getToken().lexem == "int" or self.Lexical.getToken().lexem == "char" or self.Lexical.getToken().lexem == "bool" or self.Lexical.getToken().lexem == "void" or self.ClassNameExists()):
			return True
		else: 
			raise Exception(TossError(self,"Type"))
	def ClassNameExists(self):
		return self.SymbolTable.Exists(self.Lexical.getToken().lexem)	
	def new_declaration(self):
		if(self.Lexical.getToken().lexem == "("):
			self.Lexical.GetNextToken()
			try:
				self.argument_list()
			except Exception as e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ")"):
				raise Exception(TossError(self,")"))
		if(self.Lexical.getToken().lexem == "["):
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				 self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "]"):
				raise Exception(TossError(self,"]"))
	def argument_list(self):
		print "STUB"

	def Compilation_Unit(self):
		try:
			self.Class_declaration()
		except Exception as e:
			self.HandleException(e)
		if( self.Lexical.getToken().lexem != "void"):
			raise Exception(TossError(self,"void"))
		else:
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "main"):
				raise Exception(TossError(self,'main'))
			else:
				self.Lexical.GetNextToken()
				if(self.Lexical.getToken().lexem != "("):
					raise Exception(TossError(self, '('))
				else: 
					self.Lexical.GetNextToken()
					if self.Lexical.getToken().lexem != ')':
						raise Exception(TossError(self,')'))
					else:
						try:
							self.method_body()
						except Exception as e:
							self.HandleException(e)

	def Class_declaration(self):
		if(self.Lexical.getToken().lexem != "class"):
			raise Exception(TossError(self,"class"))
		try:
			self.Lexical.GetNextToken()
			self.class_name()
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "{"):
				raise Exception(TossError(self,"{"))
			
		except Exception as e:
			self.HandleException(e)
		self.Lexical.GetNextToken()
		while(True):
			try:
				self.class_member_declaration()
			except Exception as e:
				break
	def class_name(self):
		if(self.Lexical.getToken().myType != "Identifier"):
			print self.Lexical.getToken().myType
			raise Exception(TossError(self,"Identifier"))
		if(self.FirstPass):
			symId = self.SymbolTable. getSymID("Class")

	def class_member_declaration(self):
		try:
			self.isModifier()
		except:
			try:
				self.constructor_declaration()
			except Exception as e:
				print str(e)+"or Modifier Expected"
				raise Exception()

		raise Exception(TossError(self,"Class_Member Declaration"))
	def isModifier(self):
		token = self.Lexical.getToken()
		if( token.lexem == "public"  or token.lexem == "private"):
			return
		else:
			raise Exception()
	def field_declaration(self):
		print "Stub field_Declaration"
	def constructor_declaration(self):
		print "Stub Constructor_Declaration"
		
	def method_body(self):
		print "Stub Method)_body"
	def variable_declaration(self):
		print "Stub variable_declaration"

	def parameter_list(self):
		print "Stub parameter_list"
	def parameter(self):
		print "Parameter stub"
tmp = Syntax(Lexical.LexAnalyzer("test.re","test.kxi"))

tmp.run()
