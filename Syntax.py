from SymbolTable import *
import Lexical
import os

def TossError(Syntax,Expected):
	return "Recevied %s on line %d Expected %s "%(Syntax.Lexical.getToken().lexem,Syntax.Lexical.getToken().line,Expected)
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
		self.Compilation_Unit()
	def HandleException(self, exception):
		print str(exception)
		os._exit(0)
	def expression(self):
		
		if(self.Lexical.getToken().lexem == "("):
			try:
				self.Lexical.GetNextToken()
				self.expression()
			except Exception as e:
				raise e
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ")"):
				raise Exception(TossError(self,")"))
			self.Lexical.GetNextToken()
			try:
				self.expressionz()
			except Exception as e:
				self.HandleException(e)
		elif(self.Lexical.getToken().lexem == "true" or self.Lexical.getToken().lexem == "false" or self.Lexical.getToken().lexem == "null" or self.Lexical.getToken().myType == "number" or self.Lexical.getToken().myType == "char" ):
			try:
				self.Lexical.GetNextToken()
				ret = self.expressionz()
			except Exception as e:
				self.HandleException(e)
	
		elif(self.Lexical.getToken().myType  == "Identifier"):
			try:
				self.Lexical.GetNextToken()
				ret = self.fn_arr_member()
				if (ret != None):
					self.Lexical.GetNextToken()
				ret = self.member_refz()
				print self.Lexical.getToken().lexem
				if (ret != None):
					self.Lexical.GetNextToken()
				print self.Lexical.getToken().lexem
				ret = self.expressionz()
			except Exception as e:
				self.HandleException(e)
		else:
			raise Exception()
	def expressionz(self):
		token = self.Lexical.getToken()
		if(token.lexem == '='):
			self.Lexical.GetNextToken()
			self.assignment_expression()
		elif(token.lexem == "&&" or token.lexem == '||'):
			self.Lexical.GetNextToken()
			self.expression()
		elif(token.lexem == "==" or token.lexem == "!=" or token.lexem == '<=' or token.lexem == '>=' or token.lexem == '<' or token.lexem == '>'):
			self.Lexical.GetNextToken()
			self.expression()
		elif(token.myType == 'math'):
			self.Lexical.GetNextToken()
			self.expression()
		return 1 
	def fn_arr_member(self):
		if(self.Lexical.getToken().lexem == "("):
			self.Lexical.GetNextToken()
			try:
				self.argument_list()
			except Exception as e:
				if e.msg != "NoneExistant":
					self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ")"):
				raise Exception(TossError(self,")"));
			return 1
		elif( self.Lexical.getToken().lexem == "["):
			
			self.Lexical.GetNextToken()
			try:
				self.expression()
			except Exception as e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "]"):
				raise Exception(TossError(self,"]"))
			return 1
		else:
			return None
	
	def member_refz(self):
		if(self.Lexical.getToken().lexem != "."):
			return
		self.Lexical.GetNextToken()
		if(self.Lexical.getToken().myType != "Identifier"):
			raise Exception(TossError(self,"Identifier"))
		try:
			self.Lexical.GetNextToken()
			ret = self.fn_arr_member()
			if( ret != None):
				self.Lexical.GetNextToken()
			ret = self.member_refz()
			if(ret != None):
				self.Lexical.GetNextToken()
		except Exception as e:
			self.HandleException(e)
		return 1
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
				self.expression()
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
				self.expression()
			except Exception as e:
				self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ')'):
				self.HandleException(TossError(self,')'))
		else:

			try: 
				self.expression()
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
				self.expression()
			except Exception as e:
				 self.HandleException(e)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "]"):
				raise Exception(TossError(self,"]"))
	def argument_list(self):
		try:
			self.expression()
		except Exception as e:
			raise e
		while(self.Lexical.Peek.lexem != ","):
		
			self.Lexical.GetNextToken()
			try:
				self.Lexical.GetNextToken()
				self.expression()
			except Exception as e:
				raise Exception(TossError(self,"Exception"))

	def Compilation_Unit(self):
		ret = -1
		while ret != 0:
			try:
				ret =self.Class_declaration()
			except Exception as e:
				self.HandleException(e)
		if( self.Lexical.getToken().lexem != "void"):
			raise Exception(TossError(self,"void"))
		else:
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem == "main"):
				if(not self.SymbolTable.Exists("main")):
					symid = self.SymbolTable.getSymID("method")
					self.SymbolTable.addNode(SymbolNode(self.SymbolTable.getScope(),symid,"main","method",{"Return Type":"void"}))
				self.SymbolTable.startScope("main")
				self.Lexical.GetNextToken()
				if(self.Lexical.getToken().lexem != "("):
					raise Exception(TossError(self, '('))
				else: 
					self.Lexical.GetNextToken()
					if self.Lexical.getToken().lexem != ')':
						raise Exception(TossError(self,')'))
					else:
						self.Lexical.GetNextToken()
						try:
							self.method_body()
						except Exception as e:
							self.HandleException(e)
					self.SymbolTable.endScope()
			else:
				raise Exception(TossError(self,"Main"))
			

	def Class_declaration(self):
		if(self.Lexical.getToken().lexem != "class"):
			return 0
		try:
			self.Lexical.GetNextToken()
			ret =self.class_name()
			if(ret == 0):
				raise Exception(TossError(self,"ClassName"))
			self.SymbolTable.startScope(self.Lexical.getToken().lexem)
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "{"):
				raise Exception(TossError(self,"{"))
			
		except Exception as e:
			self.HandleException(e)
		self.Lexical.GetNextToken()
		count =0
		while(True):
			try:
				self.class_member_declaration()
				self.Lexical.GetNextToken()
			except Exception as e:
				break
		if(self.Lexical.getToken().lexem != "}"):
			raise Exception(TossError(self,"}"))
		else:
			self.Lexical.GetNextToken()
		self.SymbolTable.endScope()

	def class_name(self):
		if(self.Lexical.getToken().myType != "Identifier"):
			return 0
		if(self.FirstPass):
			if (self.SymbolTable.Exists(self.Lexical.getToken().lexem)):
				return 1
			else:
				
				symId = self.SymbolTable.getSymID("Class")
				node = self.Lexical.getToken() 
				self.SymbolTable.addNode(SymbolNode(self.SymbolTable.getScope(),symId,node.lexem,"Class",None))
				return 1
		else:
			if (self.SymbolTable.Exists(self.Lexical.getToken().lexem)):
				return 1
			else:
				return 0



	def class_member_declaration(self):
		try:
			self.isModifier()
		except:
			try:
				self.constructor_declaration()
				return
			except Exception as e:
				raise Exception()
		modifier = self.Lexical.getToken().lexem
		self.Lexical.GetNextToken()
		try:
			myType =self.isType()
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().myType != 'Identifier'):
				raise Exception(TossError(self,'Identifier'))
			if(not self.SymbolTable.Exists(self.Lexical.getToken().lexem)):
				if(self.Lexical.Peek().lexem != "("):
					symId = self.SymbolTable.getSymID("Variable")
					node = self.Lexical.getToken()
					self.SymbolTable.addNode(SymbolNode(self.SymbolTable.getScope(),symId,node.lexem,"ivar", {"Type":myType, "modifier":modifier}))
				else:
					symId = self.SymbolTable.getSymID("method")
					node = self.Lexical.getToken()
					self.SymbolTable.addNode(SymbolNode(self.SymbolTable.getScope(),symId,node.lexem,"method", {"return Type":myType, "modifier":modifier}))

			self.Lexical.GetNextToken()
			self.field_declaration()
		except Exception as e:
			self.HandleException(e)
	def isType(self):
		token  = self.Lexical.getToken()
		if(self.FirstPass):
			if token.myType == 'type':				
				return token.lexem
			else:
				ret = self.ClassNameExists()
				if(ret == 0):
					raise Exception("TESTING")
				else:
					pass
				return None
		else:
			if token.myType == 'type':
				return token.lexem
			else:
					ret = self.ClassNameExists()
					if ret == 0 :
						raise Exception(TossError(self,"Type"))
	def  ClassNameExists(self):
		if(self.FirstPass):
			return 1
		else:
			if( self.SymbolTable.Exists(self.Lexical.getToken().lexem)):
				return 1
			else:
				return 0
			
	def isModifier(self):
		token = self.Lexical.getToken()
		if( token.lexem == "public"):
			return
		elif(token.lexem == 'private'):
			return
		else:
			raise Exception()
	def field_declaration(self):
		token = self.Lexical.getToken()
		if(token.lexem == '('):
			self.Lexical.GetNextToken()
			if(self.parameter_list()):
				self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem !=  ')'):
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
			ret = self.SymbolTable.ClassExists(self.Lexical.getToken().lexem)
			if(not ret):
				raise Exception()
			if(not self.FirstPass):	
				symId = self.SymbolTable.getSymID("method")
				token = self.Lexical.getToken()
				try:
					node = SymbolNode(self.SymbolTable.getScope(),symId,token.lexem,"method",None)
					self.SymbolTable.addNode(node)
				except Exception as e:
					print str(e)
			self.SymbolTable.startScope(self.Lexical.getToken().lexem)
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
			self.SymbolTable.endScope()
		except Exception as e:
			raise e

		
	def method_body(self):
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
		
		if(self.Lexical.getToken().lexem != '}'):
			raise Exception(TossError(self,'}'))
		
	def variable_declaration(self):
		try:
			mytype = self.isType()
		except Exception as e:
			raise e
		if(self.Lexical.Peek().myType != 'Identifier'):
			raise self.handleException(Exception(TossError(self,'Identifier')))
		self.Lexical.GetNextToken()
		if(self.Lexical.getToken().myType != 'Identifier'):
			self.handleException(Exception(TossError(self,'Identifier')))
		if( not self.SymbolTable.Exists(self.Lexical.getToken().lexem)):
			symid = self.SymbolTable.getSymID("local")
			self.SymbolTable.addNode(SymbolNode(self.SymbolTable.getScope(),symid,self.Lexical.getToken().lexem,"lvar",{"type":mytype}))
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
				#self.Lexical.GetNextToken()
			except Exception as e:
				self.HandleException(e)
		if(self.Lexical.getToken().lexem != ';'):
			self.HandleException(Exception(TossError(self,';')))
	def statement(self):
		if(self.Lexical.getToken().lexem == "{"):
			self.Lexical.GetNextToken()
			try:
				self.statement()
			except Exception as e:
				raise e
			self.Lexical.GetNextToken()
			if self.Lexical.getToken().lexem != "}":
				raise Exception(TossError(self,"}"))
		elif(self.Lexical.getToken().lexem == "if"):
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "("):
				raise Exception(TossError(self,"("))
			self.Lexical.GetNextToken()
			try:
				self.expression()
			except Exception as e:
				raise e
			self.Lexical.GetNextToken()
			if self.Lexical.getToken().lexem != ")":
				raise Exception(TossError(self,")"))
			try:
				self.Lexical.GetNextToken()
				self.statement()
			except Exception as e:
				raise e
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem == "else"):
				try:
					self.Lexical.GetNextToken()
					self.statement()
				except Exception as e:
					raise e	
			return
		elif(self.Lexical.getToken().lexem  == "while"):
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "("):
				raise Exception(TossError(self,"("))
			self.Lexical.GetNextToken()
			try:
				self.exception()
			except Exception as e:
				raise e
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ")"):
				raise Exception(TossError(self,")"))
			self.Lexical.GetNextToken()
			try:
				self.statement()
			except Exception as e:
				raise e
		elif (self.Lexical.getToken().lexem == "return"):
			self.Lexical.GetNextToken()
			try:
			    self.expression()
			except Exception as e:
				raise e
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ";"):
				raise Exception(TossError(self,";"))
		elif (self.Lexical.getToken().lexem == "cout"):
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != "<<"):
				raise Exception(TossError(self,"<<"))
			self.Lexical.GetNextToken()
			try:
				self.expression()
			except Exception as e:
				raise e
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ";"):
				raise Exception(TossError(self,";"))
		elif self.Lexical.getToken().lexem == "cin":
			self.Lexical.GetNextToken()
			if(self.Lexical.getToken().lexem != ">>"):
				raise Exception(TossError(self,">>"))
			self.Lexical.GetNextToken()
			try:
				self.expression()
			except Exception as e:
				raise e
		else:
			try:
				ret =self.expression()
			except Exception as e:
				raise e
			
				
	def parameter_list(self):
		if(self.Lexical.getToken().lexem == ")"):
			return False
		while(True):
			try:
				self.parameter()
				self.Lexical.GetNextToken()
				if(self.Lexical.getToken().lexem != ","):
					break
				self.Lexical.GetNextToken()
			except Exception as e:
				self.HandleException(e)
		return False
	def parameter(self):
		try:
			myType = self.isType()
		except:
			raise Exception(TossError(self,"Type"))
		self.Lexical.GetNextToken()
		if(self.Lexical.getToken().myType != "Identifier" ):
			raise Exception(TossError(self,"Identifier"))

	def printTable(self):
		print self.SymbolTable.getScope()
		print self.SymbolTable
tmp = Syntax(Lexical.LexAnalyzer("test.re","main.kxi"))

tmp.run()
tmp.run(False)
tmp.printTable()
