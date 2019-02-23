

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

	@staticmethod
	def reverse_date(date):
		""" reverse date for Portuguese """
		receive = str.split(str(date), '-')
		return receive[2] + '-' + receive[1] + '-' + receive[0]

	@staticmethod
	def orderItemValue(value, quantity):
		return value * quantity

	


		