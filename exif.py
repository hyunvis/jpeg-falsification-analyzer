import sys
import exifread

print('Input file')
f = sys.argv[1]
handle = open(f, 'rb')

print(sys.argv[1])
handle.seek(0)
checker = handle.read(100)

if ord(checker[0]) == 0xFF and ord(checker[1]) == 0xD8 : 
	print('JPEG Checked')
else:
	print('Not JPEG')

tags = exifread.process_file(handle)
print(tags)