from itertools import product

class Rod:

	def __init__(self, A=0, B=0, C=0, D=0):
		self.a = A
		self.b = B
		self.c = C
		self.d = D

	def setA(self, value):
		if(value>=0 and value<=3):
			self.a = value
		else:
			self.a = 0

	def setB(self, value):
		if(value>=0 and value<=3):
			self.b = value
		else:
			self.b = 0

	def setC(self, value):
		if (value >= 0 and value <= 3):
			self.c = value
		else:
			self.c = 0

	def setD(self, value):
		if (value >= 0 and value <= 3):
			self.d = value
		else:
			self.d = 0

	def getA(self):
		return self.a

	def getB(self):
		return self.b

	def getC(self):
		return self.c

	def getD(self):
		return self.d

	def spin(self, rodsection, value):
		if rodsection == 'a':
			self.a = (self.a + value) % 4
			print('a was spun:',self.a)
		elif rodsection == 'b':
			self.b = (self.b + value) % 4
			print('b was spun:', self.b)
		elif rodsection == 'c':
			self.c = (self.c + value) % 4
			print('c was spun:', self.c)
		elif rodsection == 'd':
			self.d = (self.d + value) % 4
			print('d was spun:', self.d)

	def shootA(self, times=1):
		for x in range(times):
			self.a = (self.a + 2) % 4
			self.b = (self.b + 1) % 4
			#print('shot A')
		#print('A shot:',times,' times')

	def shootB(self, times=1):
		for x in range(times):
			self.a = (self.a + 1) % 4
			self.b = (self.b + 2) % 4
			self.c = (self.c + 1) % 4
			#print("shot B")
		#print('B shot: ',times,' times')

	def shootC(self, times=1):
		for x in range(times):
			self.b = (self.b + 1) % 4
			self.c = (self.c + 2) % 4
			self.d = (self.d + 1) % 4
			#print("shot C")
		#print("C shot: ",times," times")
	def shootD(self, times=1):
		for x in range(times):
			self.c = (self.c + 1) % 4
			self.d = (self.d + 2) % 4
			#print("shot D")
		#print("D Shot: ",times," times")

	def checkIfCorrect(self):
		if (self.a == 0 and self.b == 0 and self.c == 0 and self.d == 0):
			return True
		else:
			return False

	def __str__(self):
		mes = 'A: ' + (str(self.getA())) + ' B: '+ str(self.getB()) + ' C: '+str(self.getC()) + ' D: '+str(self.getD())
		return mes

def getTrials():
	ttrials = list(product([0,1,2,3], repeat=4))
	return ttrials

def testrun(trod, trialcase):
	copyrod = Rod(trod.getA(), trod.getB(), trod.getC(), trod.getD())
	if trialcase[0] > 0:
		copyrod.shootA(trialcase[0])
	if trialcase[1] > 0:
		copyrod.shootB(trialcase[1])
	if trialcase[2] > 0:
		copyrod.shootC(trialcase[2])
	if trialcase[3] > 0:
		copyrod.shootD(trialcase[3])
	if(copyrod.checkIfCorrect()):
		print("found a solution: ", copyrod, trialcase)
		return trialcase
	#print(copyrod)

def findSolution(r):

	solutions = []


	#r = Rod(2,1,1,2)
	trials = getTrials()
	for i in trials:
		temp = testrun(r, i)
		if temp != None:
			solutions.append(testrun(r, i))
	return solutions

def main(r):
	return