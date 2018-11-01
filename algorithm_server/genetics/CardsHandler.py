class CardsHandler:
	def __init__(self, a_value, b_value):
		self.a_value = a_value
		self.b_value = b_value
	
	def evaluate(self):
	    return {
	        "A": self.a_value,
	        "B": self.b_value
	    }
