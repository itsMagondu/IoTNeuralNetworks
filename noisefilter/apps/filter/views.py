import numpy as np

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render

from .models import Data, KalmanConfiguration, ANNConfiguration, TrainingExample
import neuralnetwork
from .kalmanfilter import KalmanFilter


def index(request):
    return render(request, 'filter/home.html')


class IndexView(TemplateView):
	template_name = "home.html"


class KalmanView(TemplateView):
	template_name = "kalman.html"

	def get(self, request, *args, **kwargs):
		base_value = request.GET.get('base_value',20)
		iterations = request.GET.get('iterations',50)
		predict = request.GET.get('predict',19)
		error_estimate = request.GET.get('predict',4)

		examples = TrainingExample.objects.all()
		data = examples.values_list('datainput', flat=True)

		k = KalmanFilter(base_value,iterations,predict,error_estimate,data, True)
		noise,estimate, truth, plt = k.filter()
		
		plt.plot()
		canvas = FigureCanvas(plt.figure(1))
		response=HttpResponse(content_type='image/png')
		canvas.print_png(response)
		return response

		#return JsonResponse({'estimate': estimate[len(estimate)-1], 'truth': truth})


class ANNView(TemplateView):
	template_name = "ann.html"
	minValue = 0
	maxValue = 100


	def get(self,request, *args, **kwargs):
		layers = request.GET.get('layers',3)
		base_value = request.GET.get('base_value',20)
		learning_rate = request.GET.get('lrate',2)
		epochs = request.GET.get('epochs',50000)
		predict = request.GET.get('predict',19)

		examples = TrainingExample.objects.all()
		examples_list = examples.values_list('datainput', flat=True)
		layers = [1,layers,1]

		y = [base_value]* len(examples)
		n = neuralnetwork.NeuralNetwork(layers)

		scaled_x = []
		scaled_y = []
		scaled_predict = []

		index = 0
		for item in examples_list:
			scaled_x.append([self.scale_to_binary(item)])
			scaled_y.append(self.scale_to_binary(y[index]))
			index += 1

		predict = self.scale_to_binary(predict)

		scaled_y = np.array(scaled_y)
		scaled_x = np.array(scaled_x)

		print scaled_x
		print scaled_y

		print layers

		n.fit(scaled_x, scaled_y, learning_rate,epochs)
		prediction = n.predict([predict])

		return JsonResponse({'estimate':self.scale_from_binary(prediction[0]),'truth':base_value})

	def scale_to_binary(self, value):
		return neuralnetwork._scale_to_binary(value, self.minValue, self.maxValue)

	def scale_from_binary(self,value):
		return neuralnetwork.rescale_from_binary(value, self.minValue, self.maxValue)


class DashboardView(TemplateView):
	template_name = "dashboard.html"


class TrainingExamples(TemplateView):
	def __init__(self, base_value, error_range, values):
		self.base_value = base_value
		self.error_range = error_range
		self.lower_bound = base_value - error_range
		self.upper_bound = base_value + error_range
		self.values = values  # How many records to generate


	def generate(self):
		np.random.seed(0)

		for i in xrange(self.values):
			num = np.random.randint(self.lower_bound,self.upper_bound)
			TrainingExample.objects.create(datainput = num)


	def clear(self):
		TrainingExample.objects.all().delete()

def runTest():
	nn = neuralnetwork.NeuralNetwork([2,4,1], 'tanh')

	minValue = 0
	maxValue = 100

	#x_array = [[20, 24], [22, 23], [21, 23], [19, 22],[24, 27],[25, 29],[23, 25],[22, 24],[27, 29]]
	x_array = [[20, 24], [22, 23], [21, 23], [19, 22],[24, 27],[25, 29],[23, 25],[22, 24],[27, 29]]
	y_array = [22, 23, 22, 20, 25, 26, 27, 24, 23, 28]
	predict_array = [[19, 20], [26, 28], [24, 26],[21,24]]

	print "Network Input:"
	print x_array

	print "Network Output:"
	print y_array


	scaled_x_array = []
	scaled_y_array = []
	scaled_predict_array = []

	for item in x_array:
	    temp = []
	    for i in item:
	        temp.append(neuralnetwork._scale_to_binary(i, minValue, maxValue))
	    scaled_x_array.append(temp)

	for item in y_array:
	    scaled_y_array.append(neuralnetwork._scale_to_binary(item, minValue, maxValue))

	for item in predict_array:
	    temp = []
	    for i in item:
	        temp.append(neuralnetwork._scale_to_binary(i, minValue, maxValue))
	    scaled_predict_array.append(temp)

	#print scaled_y_array
	#print scaled_x_array
	#print scaled_predict_array

	X = np.array(scaled_x_array)#Training data
	y = np.array(scaled_y_array)#Testing data

	nn.fit(X, y)
	count = 0
	for i in scaled_predict_array:
	    result = nn.predict(i)
	    #print result
	    result= neuralnetwork.rescale_from_binary(result, minValue, maxValue)

	    print "\nInput values:"
	    print predict_array[count]
	    print "Prediction:"
	    print result[0]

	    count +=1
'''
So what is needed? I need to show some live simulations
1. Show the training of ANN
2. Show the prediction using a Kalman Filter
3. Show the predictions over time on each
4. Show power and memory usage of each over time
5. Show the accuracy of each
6. How does kalman behave when looking for trends? Non-linear data
7. Show the effects of various parameters on each filter.

So much to do. So help me God.
'''