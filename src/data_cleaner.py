import numpy as np
import sklearn as sk
from song import Song
# Missing Values
class BaseImputer :
    def impute(self):
        pass


class MeanImputer(BaseImputer) :
    pass


class MedianImputer(BaseImputer):
    pass

class KNNImputer(BaseImputer):
    pass


# Outliers
class BaseOutlierHandler :
    def handle(self):
        pass

class IQROutlierHandler(BaseOutlierHandler):
    pass

class ZScoreOutlierHandler(BaseOutlierHandler):
    pass