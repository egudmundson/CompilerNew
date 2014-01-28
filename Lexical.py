import re



class LexicalNode():
	def __init__(self,lexem,myType,line,colum):
		self.lexem = lexem
		self.myType = myType
		self.line = line
		self.colum = colum

	def __str__(self):
		return str(self.lexem)+" "+ str(self.myType) +" "+ str(self.line)+":"+str(self.colum)


class LexAnalyzer():
	def __init__(self,ReFile,Input):
		self.ReFile = ReFile
		self.Input = Input
		self.List = []
		self.grammer =[]
		self.location = 0
		f = open(self.ReFile,'r')
		for x in f:
			self.grammer.append(x);

	def __str__(self):
		item = ""
		for x in self.List:
			item +=str(x)
			item +="\n"
		return item

	def Run(self):
		Input = open(self.Input,'r')
		linecount = 0
		for line in Input:
			self.addToList(line,linecount)
			linecount+=1
		self.List.append(LexicalNode("EOT","EOT",0,0))

	def addToList(self,line,lineNumber):
		line = line.split("\n")[0].strip()
		line = line.split(" ")
		for x in range(0,len(line)):
			while len(line[x]) != 0:
				for data in self.grammer:
					data = data.split('\n');
					dataset = data[0].split('#')
					match = re.match(dataset[1],line[x])
					if( match != None):
						lexem =line[x][0:match.span()[1]]
						self.List.append(LexicalNode(lexem,dataset[0],lineNumber,x))
						line[x]= line[x][match.span()[1]:]

	def getToken(self):
		return self.List[self.location]

	def Peek(self):
		return self.List[self.location+1]
	def GetNextToken(self):
		location.i+=1


