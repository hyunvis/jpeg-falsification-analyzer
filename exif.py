import os, sys
import exifread

print('Input file')
f = sys.argv[1]
handle = open(f, 'rb')
tags = exifread.process_file(handle)

DateTime = tags["Image DateTime"]
DateTimeOriginal = tags["EXIF DateTimeOriginal"]
DateTimeDigitized = tags["EXIF DateTimeDigitized"]

print(DateTime)
print(DateTimeOriginal)
print(DateTimeOriginal)

print(sys.argv[1])

handle.seek(0)
checker = handle.read(100)

if ord(checker[0]) == 0xFF and ord(checker[1]) == 0xD8 : 
	print('JPEG Checked')
	#print(tags)


else:
	print('Not JPEG')

