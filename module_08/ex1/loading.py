import sys
import importlib.util


pandas = importlib.util.find_spec("pandas") is not None
numpy = importlib.util.find_spec("numpy") is not None
matplotlib = importlib.util.find_spec("matplotlib") is not None


if not pandas or not numpy or not matplotlib:
    print("Error en las dependencias")
    sys.exit(1)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2. Generación de datos sintéticos
rng = np.random.default_rng(42)
data = rng.normal(loc=0.0, scale=1.0, size=1000)

df = pd.DataFrame({
    "timestamp": range(1000),
    "signal_strength": data,
    "anomaly_score": np.abs(data)
})

# 3. Resumen y visualización de datos
print("=== Estadísticas descriptivas ===")
print(df.describe())
print("\n=== Primeros 5 registros ===")
print(df.head())

# 4. Generación y exportación del histograma
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(data, bins=50, color="gr een", alpha=0.7, edgecolor="black")
ax.set_title("Matrix Data Distribution")
ax.set_xlabel("Signal Value")
ax.set_ylabel("Frequency")
ax.grid(axis="y", linestyle="--", alpha=0.5)

fig.savefig("matrix_analysis.png", dpi=150, bbox_inches="tight")
plt.close(fig)
print("\nGráfico guardado correctamente como 'matrix_analysis.png'.")