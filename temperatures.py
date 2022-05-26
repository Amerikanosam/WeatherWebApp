class Temperatures:
	def __init__(self,location,Temperatures:list):
		self.temps = Temperatures
		self.location = location

	def computeavgtemp(self):
		self.avgtemps = sum(self.temps)/len(self.temps)
		return None