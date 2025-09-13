import os

folder_path = input("Enter folder path: ")
prefix = input("Enter a prefix (leave empty for none): ")

files = os.listdir(folder_path)
preview = []
for file in files:
    full_path = os.path.join(folder_path, file)
    if os.path.isfile(full_path):
        name, ext = os.path.splitext(file)
        ext = ext[1:]
        folder_for_ext = os.path.join(folder_path, ext)
        if not os.path.exists(folder_for_ext):
            os.mkdir(folder_for_ext)
        new_name = f"{prefix}{file}"
        new_path = os.path.join(folder_for_ext, new_name)
        preview.append((full_path, new_path))
        counter = 1
        temp_new_path = new_path
        while os.path.exists(temp_new_path):
            temp_new_path = f"{name}_{counter}.{ext}"
            temp_new_path = os.path.join(folder_for_ext, temp_new_path)
            counter += 1 
        new_path = temp_new_path
        print(f"{full_path} => {new_path}")

confirmation = input("Do you want to move these files? (y/n): ")

if confirmation == "y":
    for old_path, new_path in preview:
        os.rename(old_path, new_path)
    print("✅ All files moved!")
else:
    print("❌ No changes made.")