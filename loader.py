from sys import stdout
import collections
#http://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
#http://social.technet.microsoft.com/wiki/contents/articles/7180.data-visualization-on-the-interactive-javascript-console.aspx
#TODO filter

class DefaultShow:
	def __init__(self,data):
		self.data = data
	def show():pass

class LoadData(object):
	class _LoadData:
		def __init__(self,filename):
			self.filename = filename

		def read(self):
			with open(self.filename) as f:
				self.data = f.readlines();
				return ''.join(self.data)
	def __init__(self, filename):
		self.filename = filename
	def read(self):
		return LoadData._LoadData(self.filename).read()



class RepresentData:
	def __init__(self, filename,**kwargs):
		self.filename = filename
		self.dirty_data = LoadData(filename).read() #optimize
		#self.ViewData = collections.namedtuple('CData', 'description value')
		self.data = self._tsplit()

	def show_data(self):
		return self.data

	def _tsplit(self):
		ViewData = collections.namedtuple('CData', 'description value')
		return (list(map(lambda x:
			ViewData(description = x.split()[0], value=x.split()[1]),\
		    filter(lambda x: len(x) > 0, \
		 	self.dirty_data.split('\n')))))

	def count_lines(self):
		return self.count_lines

	def sum(self):
		return (sum(map(lambda x: float(x.value), self.data)))


	def funcmaxmin(self, func):
		return func(self.data, key=lambda x: x.value)

	def max(self):
		return self.funcmaxmin(max).value

	def min(self):
		return self.funcmaxmin(min).value

	def avg(self):
		return self.sum()/len(self.data)


class HistView:
	def __init__(self,data, suum, mean ):
		self.data = data
		self.sum = suum
		self.mean = suum/len(data)

	def naive_variance(self,data):
		n = 0
		Sum = 0
		SQR = 0
		for x in data:
			n = n + 1
			Sum = Sum + x
			SQR = SQR + x*x
		variance = (SQR - ((Sum*Sum)/n))/(n - 1)
		return variance

	def hist(self):
		result=[]
		for word in self.data:
			st=''
			for w in range(round(int(float(word.value)))):
				st+='*'
			print (word.description, word.value ,(st))

		for w in self.data:
			result.append(float(w.value))

		print('Native variance = {0}'.format(self.naive_variance(result)))



class BarGraph:
	def __init__(self,data):
		self.data = data

	def show(self):
		for dat in self.data:
			print (dat.value)
		for dat in self.data:
			stdout.write("    {0} ".format(dat.description))


class ShowData:
	def __init__(self,filename):
		self.rd = RepresentData(filename)
		self._print_first_nums()
		#self.print_hist()
		self.bar_graph()

	#print max, min, avg
	def _print_first_nums(self):
		print ('max value = {0}; min value = {1}; avg value = {2}'\
			.format(self.rd.max(), self.rd.min(), self.rd.avg()))

	def print_hist(self):
		HistView(self.rd.show_data(), self.rd.sum(), self.rd.show_data()).hist()

	def bar_graph(self):
		BarGraph(self.rd.show_data()).show()

sh = ShowData('data')