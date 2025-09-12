import os 

def number_to_letter(n):
    result = ''
    while n > 0:
        n , remainder = divmod(n-1, 26)
        result = chr(65 + remainder) + result
    return result

folder_path = input("Enter Folder: ")
rename_style = input("Do you want to rename (N)umeric or (A)lphabetic: ").lower()
prefix = input("Enter a prefix (leave it empty for none): ")

#--- Only files ---
files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
files.sort()

preview = []
for index, file in enumerate(files, start=1):
    name, ext = os.path.splitext(file)
    if rename_style == 'n':
        new_name = f"{prefix}{index}{ext}"
    elif rename_style == 'a':
        new_name = f"{prefix}{number_to_letter(index)}{ext}"
    else:
        print("❌ Invalid style")
        exit()

    old_path = os.path.join(folder_path, file)
    new_path = os.path.join(folder_path, new_name)

    #--- conflict handler ---
    counter = 1
    temp_new_path = new_path
    while os.path.exists(temp_new_path):
        temp_new_name = f"{os.path.splitext(new_name)[0]}_{counter}{ext}"
        temp_new_path = os.path.join(folder_path, temp_new_name)
        counter += 1
    new_path = temp_new_path

    preview.append((old_path, new_path))
    print(f"{old_path} => {new_path}")

#--- Confirmation ---
confirmation = input("Do you want to rename these files? (y/n): ")
if confirmation.lower() == "y":
    for old_path, new_path in preview:
        os.rename(old_path, new_path)
    print("✅ Renaming done!")
else:
    print("❌ No changes made.")
