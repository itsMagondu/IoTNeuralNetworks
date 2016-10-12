import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "noisefilter.settings.development")

import django
django.setup()
from filter.models import TrainingExample

import numpy as np
pure = np.linspace(18, 22, 100)
noise = np.random.normal(0, 0.5, 100)
signal = pure + noise

count = 0
for item in signal:
    TrainingExample.objects.create(datainput=item, dataoutput=pure[count])
    count += 1
