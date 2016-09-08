from django.contrib import admin
from .models import Data, KalmanConfiguration, ANNConfiguration, TrainingExample

# Register your models here.
class DataAdmin(admin.ModelAdmin):
    fields = ['reading', 'prevreading', 'output', 'error','truevalue','kalmanvalue']
    list_display = ['id', 'reading', 'prevreading', 'output', 'error','truevalue','kalmanvalue']
    search_field = ['reading']

class KalmanAdmin(admin.ModelAdmin):
    fields = ['base_value', 'iterations', 'initial_guess', 'posteri_estimate','active']
    list_display = ['id', 'base_value', 'iterations', 'initial_guess', 'posteri_estimate','added','active']
    search_field = ['base_value']

class ANNAdmin(admin.ModelAdmin):
    fields = ['layers', 'activation','learning_rate','epochs']
    list_display = ['id', 'layers', 'activation','learning_rate','epochs']
    search_field = ['layers']

class TrainingAdmin(admin.ModelAdmin):
    fields = ['datainput','dataoutput']
    list_display = ['id', 'datainput','dataoutput']
    search_field = ['datainput']

admin.site.register(Data, DataAdmin)
admin.site.register(ANNConfiguration, ANNAdmin)
admin.site.register(KalmanConfiguration, KalmanAdmin)
admin.site.register(TrainingExample, TrainingAdmin)