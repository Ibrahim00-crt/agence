import os

folder_path = "images"

files = os.listdir(folder_path)
files.sort()

# Étape 1 : donner un nom temporaire à chaque fichier
for i, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]:
        old_path = os.path.join(folder_path, filename)
        temp_name = f"temp_{i}{ext}"
        new_path = os.path.join(folder_path, temp_name)
        os.rename(old_path, new_path)

# Étape 2 : renommer vers les bons numéros
temp_files = os.listdir(folder_path)
temp_files.sort()

for i, filename in enumerate(temp_files, start=1):
    ext = os.path.splitext(filename)[1].lower()
    if ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp"]:
        old_path = os.path.join(folder_path, filename)
        new_name = f"{i}{ext}"
        new_path = os.path.join(folder_path, new_name)
        os.rename(old_path, new_path)
        print(f"{filename} -> {new_name}")

print("✅ Renommage terminé sans conflit !")
