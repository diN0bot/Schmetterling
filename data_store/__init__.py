
from django.db.models.base import ModelBase
import models

ALL_MODELS = [x for x in models.__dict__.values() if type(x) == ModelBase]

from lib.admins import Adminizer
Adminizer.Adminize(ALL_MODELS)
