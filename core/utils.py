

class Utils():
	"""This class have some methods for general tasks """
	@staticmethod
	def convertStringForNumber(received):
		new_received = received.replace(',', '.')
		try:
			number = float(new_received)
			return number
		except Exception as e:
			print(e)
			return False

		