import matplotlib.pyplot as plt
from pathlib import Path
from load_gestures import load_gestures

df = load_gestures('gestures/')

# Folder para guardar imágenes
images_path = Path('gestures/images/')
images_path.mkdir(exist_ok=True)  # lo crea si no existe

# Itera sobre las muestras
for (user, gesture, sample), sample_df in df.groupby(["user", "gesture", "sample"]):
    # Crea folder 'user'
    user_folder = images_path / user
    user_folder.mkdir(exist_ok=True)

    # Grafica x, y
    plt.figure(figsize=(4,4))
    plt.plot(sample_df["x"], sample_df["y"])
    plt.title(f"{gesture} - sample {sample}")
    plt.xlabel("x")
    plt.ylabel("y")

    # Guarda figura
    filename = f"{gesture}_sample_{sample}.png"
    plt.savefig(user_folder / filename)
    plt.close()  # close figure to avoid memory issues