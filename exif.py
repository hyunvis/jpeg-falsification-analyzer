handle = open('/Users/hyunvis/Desktop/IMG.jpg')
handle.seek(0)
checker = handle.read(100)
def time:
	

if ord(checker[0]) == 0xFF and ord(checker[1]) == 0xD8 : 
	print('JPEG Checked')



else:
	print('Not JPEG')
