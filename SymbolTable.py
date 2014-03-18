
class SymbolNode():
	def __init__(self,scope,symid,myValue,myKind,myData):
		self.scope = scope
		self.symid = symid
		self.value = myValue
		self.kind = mykind
		self.data = myData

	def __str__(self):
		return "SymID: "+str(self.symid)+"Remaning:" + self.scope+" " +str(self.value)+ ' ' +str(self.kind) +' '+ str(self.data)

class SymbolTable():
	def __init__(self):
		self.Table = {}
		self.scope = "g"
		self.count = 0
	def addNode(self,Node):
		key = Node.symid;
	def Exists(self,value):
		print "Stub SymbolTable.Exists"
		return True
	def startScope(self,scope):
		self.scope +=".%s" % scope
	def endScope(self):
		newScope = self.scope.split(".")
		print newScope[:-1]
	def getScope(self):
		return self.scope
	def __str__(self):
		string = ''
		for x in self.Table.keys():
			string += str(self.Table[x])
		return string
	def getSymID(self,Type):
		data=''
		myType = Type.lower()[0]
		data += myType + str(self.count)
		self.count+=1
		return data






