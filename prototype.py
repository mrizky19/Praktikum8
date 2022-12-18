class Dict:
	def __init__(self):
		self.data = {}

	def	add(self, key, value):
		self.data[key] = value

	def	get(self, key):
		return self.data[key]

mydict = Dict()

Dict.add("apel", "a fruit")
Dict.add("car", "a vechile")

print(Dict.get("apel"))
