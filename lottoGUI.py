"""
Project: lottoGUI.py
Author: Erick Romero
"""

from breezypythongui import EasyFrame
import random

class LottoGUI(EasyFrame):
	

	def __init__(self):
		"""Sets up the window and widgets."""
		EasyFrame.__init__(self, title = "Lotto Number Generator", resizable = False, background = "cornsilk3")
		self.addLabel(text = "Lotto Number Generator", row = 0, column = 0, columnspan = 5, sticky = "NSEW", background = "cornsilk3").config(font = ("Georgia", 16))
		self.addLabel(text = "Here are your 5 numbers:", row = 1, column = 0, columnspan = 5, sticky = "NSEW", background = "cornsilk3")
		self.numPanel = self.addPanel(row = 2, column = 0, background = "cornsilk2", columnspan = 5)
		self.field1 = self.numPanel.addIntegerField(value = 0, row = 0, column = 0, width = 3, sticky = "NSEW")
		self.field2 = self.numPanel.addIntegerField(value = 0, row = 0, column = 1, width = 3, sticky = "NSEW")
		self.field3 = self.numPanel.addIntegerField(value = 0, row = 0, column = 2, width = 3, sticky = "NSEW")
		self.field4 = self.numPanel.addIntegerField(value = 0, row = 0, column = 3, width = 3, sticky = "NSEW")
		self.field5 = self.numPanel.addIntegerField(value = 0, row = 0, column = 4, width = 3, sticky = "NSEW")
		self.addLabel(text = "Your PowerBall number is:", row = 3, column = 0, sticky = "NSEW", background = "yellow")
		self.pBall = self.addIntegerField(value = 0, row = 3, column = 1, width = 3, sticky = "NSEW")
		self.pBall.config(background = "white")

		self.addButton(text = "Pick Numbers", row = 4, column = 0, columnspan = 5, command = self.pickNumbers)

	def pickNumbers(self):
		num1 = random.randint(1, 69)
		num2 = random.randint(1, 69)
		num3 = random.randint(1, 69)
		num4 = random.randint(1, 69)
		num5 = random.randint(1, 69)
		power = random.randint(1, 26)

		# now take those random number variables and update the fields of the GUI
		self.field1.setNumber(num1)
		self.field2.setNumber(num2)
		self.field3.setNumber(num3)	
		self.field4.setNumber(num4)	
		self.field5.setNumber(num5)
		self.pBall.setNumber(power)
		

# definition of the main() function for program entry
def main():

	LottoGUI().mainloop()

# global call to the main() function
main()