class Buffer:
	def __init__(self):
		self.buf = []
	def add(self,*a):
		# print(type(a))
		# print(a[0])
		# print(len(a))
		self.buf.extend(a)
		# [self.buf.extend(a[i]) for i in range(len(a))]
		def print_element():
			if len(self.buf) >=5:
				sum_element = 0
				for i in range(5):
					sum_element += self.buf[i]
				print(sum_element)
				del self.buf[:5]

				print_element()
			else:
				return
		print_element()
	def get_current_part(self):
		return self.buf
