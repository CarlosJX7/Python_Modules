import sys
import importlib.util


pandas = importlib.util.find_spec("pandas") is not None
numpy = importlib.util.find_spec("numpy") is not None


if not pandas or not numpy:
    print("Error en las dependencias")
    sys.exit(1)

import numpy
import pandas