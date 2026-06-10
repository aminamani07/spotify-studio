import numpy as np
import sklearn as sk
from song import Song
# Missing Values
class BaseImputer :
    def impute(self , track_list , feature_name):
        pass


class MeanImputer(BaseImputer) :
    pass


class MedianImputer(BaseImputer):
    pass

class KNNImputer(BaseImputer):
    pass


# Outliers
class BaseOutlierHandler :
    def handle(self , track_list , feature_name):
        pass

class IQROutlierHandler(BaseOutlierHandler):
    pass

class ZScoreOutlierHandler(BaseOutlierHandler):
    pass