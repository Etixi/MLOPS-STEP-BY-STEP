import numpy as np
import bentoml
from bentoml.io import NumpyNdarray

iris_clf_runner = bentoml.sklearn.get("iris_clf:latest").to_runner()

svc = bentoml.Service("iris_classifier", runners=[iris_clf_runner])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
def classify(input_series: np.ndarray) -> np.ndarray:
    result = iris_clf_runner.predict.run(input_series)
    return result

# bentoml serve service.py:svc --reload
# Go to Postman : choose POST Request and put URL : 127.0.0.1:3000/classify
# Go to raw => select JSON
# put this array 2D : [[1, 2.3, 4.2, 1.0]]