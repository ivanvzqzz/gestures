import pandas as pd
from pathlib import Path

def load_gestures(base_path: str | Path = None) -> pd.DataFrame:
    # Path de los archivos, usa por defecto el directorio actual
    if base_path is None:
        base_path = Path.cwd()
    else:
        base_path = Path(base_path)
    all_data = []   # Arreglo de datos

    # Iteramos sobre cada folder de usuario
    for user_folder in base_path.glob("user_*"):
        user_id = user_folder.name 

        # Iteramos sobre todos los gestos
        for csv_file in user_folder.glob("gesture_*_sample_*.csv"):
            gesture_name = csv_file.stem.split("_sample_")[0]
            sample_id = csv_file.stem.split("_sample_")[-1]

            # Leemos el archivo csv
            df = pd.read_csv(csv_file)

            # Agregamos columnas paraa usuario, gesto y muestra
            df["user"] = user_id
            df["gesture"] = gesture_name
            df["sample"] = sample_id

            # Anexamos a la lista
            all_data.append(df)

    # Concatenamos en un df
    final_df = pd.concat(all_data, ignore_index=True)

    # Reordenamos las columnas
    cols = ["user", "gesture", "sample"] + [c for c in final_df.columns if c not in ["user", "sample", "gesture"]]
    final_df = final_df[cols]

    return final_df

if __name__ == "__main__":
    df = load_gestures("gestures/")
    print("DataFrame cargado con éxito")