import json
from .Judge import Judge
from .Population import Population

class CardsHandler:
	def __init__(self, a_value, b_value):
		if not isinstance(a_value, (int, float)): 
			raise TypeError
		if not isinstance(b_value, (int, float)):
			raise TypeError

		self.a_value = a_value
		self.b_value = b_value

		with open('./genetics/conf.json') as conf_file:
			self.conf = json.load(conf_file)
		self.judge = Judge(self.conf['cards'])

	def evaluate(self):
		p = Population(self.conf, self.judge, self.a_value, self.b_value)
		p.generate_random_population()
		for i in range(self.conf['epochs']):
			nextp = p.create_next_epoch()
			p = nextp
			
		best = p.get_the_best_error()
		A_ret = []
		B_ret = []
		for i in range(len(self.conf['cards'])):
			if(best[i]):
				A_ret.append(self.conf['cards'][i])
			else:
				B_ret.append(self.conf['cards'][i])
		return {
	    	"A": A_ret,
	        "B": B_ret
	    }