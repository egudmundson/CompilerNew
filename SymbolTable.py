
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

	def addNode(self,Node):
		key = Node.symid;
	def Exists(self,value):


	def __str__(self):
		string = ''
		for x in self.Table.keys():
			string += str(self.Table[x])
		return string




