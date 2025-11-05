import pandas as pd

def cargar_datos(ruta):
    """Carga un dataset desde un archivo CSV"""
    return pd.read_csv(ruta)

def limpiar_datos(df):
    """Elimina valores nulos y duplicados"""
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def normalizar_datos(df):
    """Normaliza columnas numéricas"""
    num_cols = df.select_dtypes(include=['float64', 'int64']).columns
    df[num_cols] = (df[num_cols] - df[num_cols].mean()) / df[num_cols].std()
    return df

def preprocesar_dataset(ruta):
    df = cargar_datos(ruta)
    df = limpiar_datos(df)
    df = normalizar_datos(df)
    return df


