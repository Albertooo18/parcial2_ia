import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#  URL raw del dataset (ya corregida)
url = "https://raw.githubusercontent.com/Albertooo18/parcial2_ia/main/dataset/trafico_red.csv"

try:
    # Cargar el dataset
    df = pd.read_csv(url)
    print("Dataset cargado correctamente.\n")
    print(df.head())
    
except Exception as e:
    print("Error al cargar el dataset:", e)
