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
		print "Expression stub"
	def expressionz(self):
		print "Expressionz Stub"
	def assignment_expression(self):
		if self.Lexical.getToken().lexem == 'this':
			self.Lexical.GetNextToken()
			return
		elif self.Lexical.getToken().lexem == 'new':
			self.Lexical.GetNextToken()
			try:
				self.isType()
				self.Lexical.GetNextToken()
				self.new_declaration()
			except Exception as e:
				self.HandleException(e)
		elif self.Lexical.getToken().lexem == 'atoi':
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != '('):
				self.HandleException(TossError(self,'('))
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ')'):
				self.HandleException(TossError(self,')'))
		elif(self.Lexical.getToken().lexem == 'itoa'):
						self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != '('):
				self.HandleException(TossError(self,'('))
			self.Lexical.GetNextToken()
			try:
				self.Expression()
			except Exception as e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ')'):
				self.HandleException(TossError(self,')'))
		else:

			try: 
				self.Expression()
			except Exception as e:
				raise e			

			
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
				self.Lexical.GetNextToken()
			except Exception as e:
				break
		self.Lexical.GetNextToken()
		if(self.Lexical.getToken().lexem != "}"):
			raise Exception(TossError(self,"}"))

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
				return
			except Exception as e:
				print str(e)+"or Modifier Expected"
				raise Exception()
		self.Lexical.GetNextToken()
		print "modifier"
		try:
			self.isType()
			print "isType"
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().myType != 'Identifier'):
				raise Exception(TossError(self,'Identifier'))
			print "Is Identifier"
			self.Lexical.GetNextToken()
			self.field_declaration()
		except Exception as e:
			print "Exception 2"
			self.HandleException(e)
	def isType(self):
		token  = self.Lexical.getToken()
		if(self.FirstPass):
			print token.myType
			if token.myType == 'type' or token.myType == 'Identifier':				
				print "Returning is Type"
				return
			else:
				raise Exception(TossError(self,'Type'))
		else:
			if token.myType == 'Type':
				return
			else:
				try: 
					self.class_name()
				except Exception as e:
					self.HandleException(e)
			
	def isModifier(self):
		token = self.Lexical.getToken()
		if( token.lexem == "public"):
			print "Returning from IsModifier"
			return
		elif(token.lexem == 'private'):
			return
		else:
			print "Exception Modifier"
			raise Exception()
	def field_declaration(self):
		print "Stub field_Declaration"
		token = self.Lexical.getToken()
		if(token.lexem == '('):
			self.Lexical.GetNextToken()
			try:
				self.parameter_list()
				self.Lexical.GetNextToken()
			except Exception as e:
				print "No Parameters"
			if(self.Lexical.getToken() !=  ')'):
				raise Exception(TossError(self,')'))
			try:
				self.Lexical.GetNextToken()
				self.method_body()
			except Exception as e:
				self.HandleException(e)
			


		else:
			if token.lexem == '[':
				self.Lexical.GetNextToken()
				if(self.Lexical.getToken().lexem != ']'):
					raise Exception(TossError(self,']'))
				self.Lexical.GetNextToken()
			elif(token.lexem == '='):
				try:
					self.Lexical.GetNextToken()
					self.assignment_expression()
					self.Lexical.GetNextToken()
				except Exception as e:
					self.HandleException(e)
			if(self.Lexical.getToken().lexem != ';'):
				raise Exception(TossError(self,';'))
	def constructor_declaration(self):
		try:
			self.class_name()
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != '('):
				raise Exception(TossError(self,'('))
			self.Lexical.GetNextToken()
			if(self.parameter_list() ):
				self.Lexical.GetNextToken()
			if (self.Lexical.getToken().lexem != ')'):
				raise Exception(TossError(self,')'))
			self.Lexical.GetNextToken()
			self.method_body()			
		except Exception as e:
			raise e

		
	def method_body(self):
		print "Stub Method)_body"
		if(self.Lexical.getToken().lexem != '{'):
			raise Exception(TossError(self,'{'))
		self.Lexical.GetNextToken()
		while(True):
			try:
				self.variable_declaration()
				self.Lexical.GetNextToken()
			except Exception as e:
				break
		while(True):
			try:
				self.statement()
				self.Lexical.GetNextToken()
			except:
				break
		if(self.Lexical.getToken() != '}'):
			raise Exception(TossError(self,'}'))
		
	def variable_declaration(self):
		try:
			self.isType()
		except Exception as e:
			raise e
		self.Lexical.GetNextToken()
		if(self.Lexical.getToken().myType != 'Identifier'):
			self.handleException(Exception(TossError(self,'Identifier')))
		self.Lexical.GetNextToken()
		if(self.Lexical.getToken().lexem == '['):
				self.Lexical.GetNextToken()
				if(self.Lexical.getToken().lexem != ']'):
						self.HandleException(Exception(TossError(self,']')))
				self.Lexical.GetNextToken()
		if(self.Lexical.getToken().lexem == '='):
			self.Lexical.GetNextToken()
			try:
				self.assignment_expression()
				self.Lexical.GetNextToken()
			except Exception as e:
				self.HandleException(e)
		if(self.Lexical.getToken().lexem != ';'):
			self.HandleException(Exception(TossError(self,';')))
	def statement(self):
		print "Stub Statement"
		raise(Exception("In Statement Stub"))
	def parameter_list(self):
		return False
		print "Stub parameter_list"
	def parameter(self):
		print "Parameter stub"
tmp = Syntax(Lexical.LexAnalyzer("test.re","test.kxi"))

tmp.run()
