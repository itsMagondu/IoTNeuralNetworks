from django.views.generic.base import TemplateView
from django.shortcuts import render

from .kalmanfilter import KalmanFilter
from .neuralnetwork import NeuralNetwork


class IndexView(TemplateView):
	template_name = "home.html"


class KalmanView(TemplateView):
	template_name = "kalman.html"


class ANNView(TemplateView):
	template_name = "ann.html"


class DashboardView(TemplateView):
	template_name = "dashboard.html"


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