from tkinter import *
import random

root = Tk()
root.title("Quick Maths")
root.geometry("827x485")
root.resizable(0,0)


class mathGame:

	def __init__(self,main):
		bigGrid = Frame(main)
		bigGrid.grid(row=1,column=1)
		# Frame setup
		self.entryBox = Entry(main, width=25,borderwidth=2, font=("Calibri 21"))
		self.entryBox.grid(row=5,column=3,columnspan=2,ipady=19)
		# -------------------  Displays   ----------
		self.silverScreen = Label(main,width=20,relief='sunk', height=4,font=('Calibri 44'),borderwidth=0)
		self.silverScreen.grid(row=0,column=1,columnspan=4,rowspan=4)
		self.feedbackScreen = Label(main, width=25,borderwidth=2, relief='groove',height=2, font=('Calibri 20'),text='Enter answer or \npress new for new problem')
		self.feedbackScreen.grid(row=4,column=3,columnspan=2)
		# ------------------   Labels ----------------
		self.answerLabel = Label(main, text='Your Answer:',font=('Calibri 12'),justify=LEFT)
		self.answerLabel.grid(row=5,column=1,columnspan=2)
		self.counterStringLabel = Label(main, text='Number of Tries: ',font=('Calibri 12'), justify=RIGHT)
		self.counterLabel = Label(main,text='0',font=('Calibri 12'))
		self.counterStringLabel.grid(row=4,column=1)
		self.counterLabel.grid(row=4,column=2)
		# ---------------  Buttons  -----------------------
		self.checkButton = Button(main, text='check', padx=40 ,pady=100,font=('Calibri 12'),command=self.check)
		self.newButton = Button(main, text='new', padx=44 ,pady=100,font=('Calibri 12'),command=self.new)
		self.quitButton = Button(main, text='quit', padx=31 ,pady=25,font=('Calibri 12'),command=root.destroy)
		self.addButton = Button(main, text="+" , padx=39, pady=25,font=('Calibri 12'),command=self.addButtonPress)
		self.subtractButton = Button(main, text= "-", padx=40 , pady=25,font=('Calibri 12'),command=self.subtractButtonPress)
		self.multiplyButton = Button(main, text="*" , padx=39 , pady=25,font=('Calibri 12'),command=self.multiplyButtonPress)
		self.divideButton = Button(main, text="/", padx=40 , pady=25,font=('Calibri 12'),command=self.divideButtonPress)
		self.anyButton = Button(main, text='any',padx=32,pady=25,font=('Calibri 12'),command=self.anyButtonPress,bg='#33634a')
		# -----------------  Grid  ---------------------------
		self.checkButton.grid(row=0,column=0,rowspan=3)
		self.newButton.grid(row=3,column=0,rowspan=3)
		self.quitButton.grid(row=0,column=5)
		self.addButton.grid(row=1,column=5)
		self.subtractButton.grid(row=2,column=5)
		self.multiplyButton.grid(row=3,column=5)
		self.divideButton.grid(row=4,column=5)
		self.anyButton.grid(row=5,column=5)
		# ---------------   Misc  ----------------------
		self.buttonColor,self.answer,self.dictType = None,None,None
		self.counter1,self.numberSolved,self.numAttempted = 0,0,0
		self.counterList, self.probChecklist= [],[]
		self.probDictionary = {'addition':[],'multiplication':[],'subtraction':[],'division':[]}
		self.anyButtonPress()
		self.any()


	def new(self):
			if self.counter1 != 0:
				self.dictionaryUpdate(self.counter1)
			self.entryBox.configure(state='normal')
			self.entryBox.delete(0,END)
			
			self.feedbackScreen.configure(text='Please enter a number')
			self.counter1 = 0
			probType = self.buttonColor
			if probType == 'add':
				self.add()
			if probType == 'subtract':
				self.subtract()
			if probType == 'multiply':
				self.multiply()
			if probType == 'divide':
				self.divide()
			if probType =='any':
				self.any()
			self.counterLabel.configure(text='0')

	def addButtonPress(self):
		self.anyButton.configure(bg='#F0F0F0')
		self.subtractButton.configure(bg='#F0F0F0')
		self.multiplyButton.configure(bg='#F0F0F0')
		self.divideButton.configure(bg='#F0F0F0')
		self.addButton.configure(bg='#33634a')
		self.buttonColor = 'add'
	def subtractButtonPress(self):
		self.anyButton.configure(bg='#F0F0F0')
		self.subtractButton.configure(bg='#33634a')
		self.multiplyButton.configure(bg='#F0F0F0')
		self.divideButton.configure(bg='#F0F0F0')
		self.addButton.configure(bg='#F0F0F0')
		self.buttonColor = 'subtract'
	def multiplyButtonPress(self):
		self.anyButton.configure(bg='#F0F0F0')
		self.subtractButton.configure(bg='#F0F0F0')
		self.multiplyButton.configure(bg='#33634a')
		self.divideButton.configure(bg='#F0F0F0')
		self.addButton.configure(bg='#F0F0F0')
		self.buttonColor = 'multiply'
	def divideButtonPress(self):
		self.anyButton.configure(bg='#F0F0F0')
		self.subtractButton.configure(bg='#F0F0F0')
		self.multiplyButton.configure(bg='#F0F0F0')
		self.divideButton.configure(bg='#33634a')
		self.addButton.configure(bg='#F0F0F0')
		self.buttonColor = 'divide'
	def anyButtonPress(self):
		self.buttonColor = 'any'
		self.subtractButton.configure(bg='#F0F0F0')
		self.multiplyButton.configure(bg='#F0F0F0')
		self.divideButton.configure(bg='#F0F0F0')
		self.addButton.configure(bg='#F0F0F0')
		self.anyButton.configure(bg='#33634a')

	def add(self):
		numsToUse = self.addNums()
		num1 = numsToUse[0]
		num2 = numsToUse[1]
		string1 = "{} + {}".format(num1,num2)
		self.silverScreen.configure(text=string1)
		self.dictType = 'add'
	def subtract(self):
		numsToUse = self.subtractNums()
		num1 = numsToUse[0]
		num2 = numsToUse[1]
		string1 = "{} - {}".format(num1,num2)
		self.silverScreen.configure(text=string1)
		self.dictType = 'subtract'
	def multiply(self):
		numsToUse = self.multiplyNums()
		num1 = numsToUse[0]
		num2 = numsToUse[1]
		string1 = "{} x {}".format(num1,num2)
		self.silverScreen.configure(text=string1)
		self.dictType = 'multiply'
	def divide(self):
		numsToUse = self.divideNums()
		num1 = numsToUse[0]
		num2 = numsToUse[1]
		string1 = "{} / {}".format(num1,num2)
		self.silverScreen.configure(text=string1)
		self.dictType = 'divide'
	
	def addNums(self):
		num1 = random.randint(0,1000)
		num2 = random.randint(0,1000)
		stringToCheck = "{}+{}".format(num1,num2)
		while stringToCheck in self.probChecklist:
			num2 = random.randint(0,1000)
		else:
			probString = "{}+{}".format(num1,num2)
			self.probChecklist.append(probString)
			answer = num1+num2
			self.answer = answer
		return [num1,num2]

	def multiplyNums(self):
		num1 = random.randint(1,100)
		num2 = random.randint(1,100)
		stringToCheck = "{}*{}".format(num1,num2)
		string2Tocheck = "{}*{}".format(num2,num1)
		while stringToCheck in self.probChecklist or string2Tocheck in self.probChecklist:
			num2 = random.randint(1,100)
		else:
			answer = num1 * num2
			self.answer = answer
			probString = "{}*{}".format(num1,num2)
			self.probChecklist.append(probString)
			return [num1,num2]

	def divideNums(self):
		num1 = random.randint(1,30)
		num2 = random.randint(1,30)
		product = num1 * num2
		stringToCheck = "{}/{}".format(product,num1)
		while stringToCheck in self.probChecklist:
			num2 = random.randint(1,30)
		else:
			product = num1 * num2
			answer = num2
			self.answer = answer
			probstring = "{}/{}".format(product,num1)
			self.probChecklist.append(probstring)
		return [product,num1]
	def subtractNums(self):
		num1 = random.randint(1,1000)
		num2 = random.randint(1,1000)
		stringToCheck = "{}-{}".format(num1,num2)
		while num2 > num1 or stringToCheck in self.probChecklist:
			num2 = random.randint(1,1000)
		else:
			probString = "{}-{}".format(num1,num2)
			answer = num1 - num2
			self.answer = answer
			self.probChecklist.append(probString)
			return [num1,num2]

	def dictionaryUpdate(self,num):
		if self.dictType == 'add':
			list1 = self.probDictionary['addition']
			list1.append(num)
		if self.dictType == 'subtract':
			list1 = self.probDictionary['subtraction']
			list1.append(num)
		if self.dictType == 'multiply':
			list1 = self.probDictionary['multiplication']
			list1.append(num)
		if self.dictType == 'divide':
			list1 = self.probDictionary['division']
			list1.append(num)

	def check(self):
		numbers = ['1','2','3','4','5','6','7','8','9','0']
		userList = []
		isNum = True

		userAnswer = self.entryBox.get()
		if userAnswer == '':
			self.feedbackScreen.configure(text="Please enter a number.")

		else:
			for item in userAnswer:
				if item not in numbers:
					isNum = False
			if isNum:
				userAnswer = int(userAnswer)
				if self.counter1 == 0:
					self.numAttempted += 1
				self.counter1 += 1
				userAnswer = int(userAnswer)
				self.counterLabel.configure(text=str(self.counter1))
				if userAnswer != self.answer:
					self.feedbackScreen.configure(text='Wrong. \nTry Again.')
				else:
					self.feedbackScreen.configure(text='You are correct! \n Press new for new problem')
					self.counterLabel.configure(text=str(self.counter1))
					self.counterList.append(self.counter1)
					self.entryBox.configure(state='disabled')
					self.numberSolved += 1
			else:
				self.feedbackScreen.configure(text='Those look like letters. \n Please enter a number')



		self.entryBox.delete(0,END)

	def finalStats(self):
		totalNumTries = 0
		for key in self.probDictionary:
			numList = self.probDictionary[key]
			length = len(numList)
			if length != 0:
				totalTries = sum(numList)
				totalNumTries += totalTries
				#average = sum(numList) / length
				#statString = "For {} problems, the average number of attempts: {}".format(key,average)
				#numString = "Number of {} problems attempted: {}".format(key,len(numList))
				#print(numString)
				#print(statString)
				#print("\n")

		numAttemptedString = "Total number of attempted problems: {}".format(self.numAttempted)
		numSolvedString = "Total number of solved problems: {}".format(self.numberSolved)
		print(numAttemptedString)
		print(numSolvedString)
		if totalNumTries != 0:
			totalAverage = round(totalNumTries / self.numberSolved,1)
			triesString = "Average number of tries per solved problem: {}".format(totalAverage)
			print(triesString)

	def any(self):
		typeList= ['+','-','*','/']
		choice = random.choice(typeList)
		if choice == '+':
			self.add()
		if choice == '-':
			self.subtract()
		if choice == '*':
			self.multiply()
		if choice == '/':
			self.divide()
		
		
newGame = mathGame(root)

root.mainloop()

newGame.finalStats()

#print(newGame.probChecklist)
#print(newGame.probDictionary)


	