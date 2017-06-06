import sys, os, zipfile


class Zipped:

	def zipdir(self,zipname, dirname):
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
				print '%3d%% %s' % (percent, path)

				z.write(path, arcname)
				current += os.path.getsize(path)
		z.close()

if __name__ == '__main__':
	print "Do Not Run this!!"
