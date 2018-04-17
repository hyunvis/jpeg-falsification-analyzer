import os, sys
import exifread
import datetime

print('Input file')
f = sys.argv[1]
handle = open(f, 'rb')

tags = exifread.process_file(handle)
DateTime = tags["Image DateTime"]
DateTimeOriginal = tags["EXIF DateTimeOriginal"]
DateTimeDigitized = tags["EXIF DateTimeDigitized"]

print('EXIF DATA')
print('DateTime')
print(DateTime)
print('DateTimeOriginal')
print(DateTimeOriginal)
print('DateTimeDigitized')
print(DateTimeDigitized)

ctime = datetime.datetime.fromtimestamp(os.path.getctime(f)) #create time
mtime = datetime.datetime.fromtimestamp(os.path.getmtime(f)) #modify time
atime = datetime.datetime.fromtimestamp(os.path.getatime(f)) #access time

atimea = atime.strftime('%Y:%m:%d %H:%M:%S')
mtimea = mtime.strftime('%Y:%m:%d %H:%M:%S')
ctimea = ctime.strftime('%Y:%m:%d %H:%M:%S')

print('\n')
print('SYSTEM DATA')
print('ctime')
print(ctimea)
print('mtime')
print(mtimea)
print('atime')
print(atimea)
print('\n')


if str(DateTime) != str(mtimea) :
	print('File Falsification Detected!!!!')
else:
	print('Good as well')


handle.seek(0)
checker = handle.read(100)

if ord(chr(checker[0])) == 0xFF and ord(chr(checker[1])) == 0xD8 : 
	print('JPEG Checked')
else:
	print('Not JPEG')