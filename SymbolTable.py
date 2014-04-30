
class SymbolNode():
	def __init__(self,scope,symid,myValue,myKind,myData):
		self.scope = scope
		self.symid = symid
		self.value = myValue
		self.kind = myKind
		self.data = myData

	def __str__(self):
		return "SymID: "+str(self.symid)+"\nScope:" + self.scope+"\nValue " +str(self.value)+ '\nKind ' +str(self.kind) +'\nData '+ str(self.data)

class SymbolTable():
	def __init__(self):
		self.Table = {}
		self.scope = "g"
		self.count = 0
	def addNode(self,Node):
		key = Node.symid;
		self.Table[key] = Node
		if key.startswith("p"):
			self.addParam(key)
	def Exists(self,value):
		for x in self.Table:
			if self.Table[x].value == value : 
				return True
		return False
	def ClassExists(self,value):
		for x in self.Table:
			if( self.Table[x].value == value and x.startswith('c')):
				return True
		return False
	def addParam(self,symid):
		print "stub"
		
	def startScope(self,scope):
		self.scope +=".%s" % scope
	def endScope(self):
		newScope = self.scope.split(".")
		newScope = newScope[:-1]
		scope = ".".join(newScope)
		self.scope = scope
	def getScope(self):
		return self.scope
	def getSymID(self,Type):
		data=''
		myType = Type.lower()[0]
		data += myType + str(self.count)
		self.count+=1
		return data

	def __str__(self):
		string = ""
		for x in self.Table:
			string += str(self.Table[x])
			string += "\n\n\n"
		return string





