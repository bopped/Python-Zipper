import sys, os, zipfile, time
from colorama import init
init()

class Zipped:
	def log(self,msg,Color):
		Reset = '\033[0m'
		currenttime = time.strftime("%H:%M:%S")
		sys.stdout.write("[%s] %s\n" % (currenttime, Color + (msg) + Reset))
		sys.stdout.flush()

	def zipdir(self,zipname, dirname):
		Underline = '\033[04m'
		Lightblue = '\033[94m'
		Red = '\033[31m'
		Green = '\033[32m'
		Reset = '\033[0m'

		total = 0
		for root, dirs, files in os.walk(dirname):
			for fname in files:
				path = os.path.join(root, fname)
				total += os.path.getsize(path)
		basename = os.path.basename(dirname)
		z = zipfile.ZipFile(zipname, 'w', zipfile.ZIP_DEFLATED)
		current = 0
		for root, dirs, files in os.walk(dirname):
			for fname in files:
				path = os.path.join(root, fname)
				arcname = os.path.join(basename, fname)
				percent = 100 * current / total
				self.log('%s%3d%% %s%s' % (Green, percent, Reset, path), "")
				z.write(path, arcname)
				current += os.path.getsize(path)
		z.close()

if __name__ == '__main__':
	print "Do Not Run this!!"
