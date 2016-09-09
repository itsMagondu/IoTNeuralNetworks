from __future__ import unicode_literals

from django.db import models

class Data(models.Model):
    reading = models.FloatField(null=True, blank=True)
    prevreading = models.FloatField(null=True, blank=True)
    output = models.FloatField(null=True, blank=True)
    error = models.FloatField(null=True, blank=True)
    truevalue = models.FloatField(null=True, blank=True)
    kalmanvalue = models.FloatField(null=True, blank=True)

    added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class KalmanConfiguration(models.Model):
    base_value = models.FloatField(null=True, blank=True)
    iterations = models.FloatField(null=True, blank=True)
    initial_guess = models.FloatField(null=True, blank=True)
    posteri_estimate = models.FloatField(null=True, blank=True)

    added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class ANNConfiguration(models.Model):
    layers = models.IntegerField(null=True, blank=True)
    activation = models.CharField(max_length=20, default='',null=True, blank=True)

    #Fitting info
    learning_rate = models.IntegerField(null=True, blank=True)
    epochs = models.IntegerField(null=True, blank=True)

    added = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class TrainingExample(models.Model):
    dataoutput = models.FloatField(null=True, blank=True)
    datainput = models.FloatField(null=True, blank=True)

class AnnResult(models.Model):
    prediction = models.FloatField(null=True, blank=True)
    epochs = models.IntegerField(null=True, blank=True)
    seconds = models.IntegerField(null=True, blank=True)
    hidden_layer_size = models.IntegerField(null=True, blank=True)
    truevalue = models.FloatField(null=True, blank=True)

    added = models.DateTimeField(auto_now_add=True)


class KalmanResult(models.Model):
    prediction = models.FloatField(null=True, blank=True)
    iterations = models.IntegerField(null=True, blank=True)
    seconds = models.IntegerField(null=True, blank=True)
    initial_guess = models.IntegerField(null=True, blank=True)
    truevalue = models.FloatField(null=True, blank=True)

    added = models.DateTimeField(auto_now_add=True)