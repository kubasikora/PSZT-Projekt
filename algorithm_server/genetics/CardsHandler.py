class CardsHandler:
	def __init__(self, a_value, b_value):
		self.a_value = a_value
		self.b_value = b_value
		with open('./genetics/conf.json') as conf_file:
			self.conf = json.load(conf_file)
		self.judge = Judge(self.conf['cards'])
	
	def evaluate(self):
	    return {
	        "A": self.a_value,
	        "B": self.b_value
	    }
