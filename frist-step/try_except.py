# import sys
# try:
# 	s=input('Enter something-->')
# except EOFError:
# 	print('\nWhy did you do an EOF on me?')
# 	sys.exit()
# except:
# 	print("\nSome error/exception occurred.")
# print('Done')

class ShortInputException(Exception):
	def __init__(self,length,atleast):
		Exception.__init__(self)
		self.length=length
		self.atleast=atleast
try:
	s=input('Enter something-->')
	if len(s)<3:
		raise ShortInputException(len(s),3)
except EOFError:
    print('\nWhy did you do an EOF on me?')
except ShortInputException:
    print('ShortInputException: The input was of length %d, \
          was expecting at least')
else:
    print('No exception was raised.')