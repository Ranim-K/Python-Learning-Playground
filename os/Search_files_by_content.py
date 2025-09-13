import os

folder_path = input("Enter folder path: ")
search_term = input("Enter text to search for: ")
file_type = input("Filter by file extension (leave empty for all): ")

# Walk through all folders and files
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file_type:  # If user entered a file type, skip others
            if not file.endswith(file_type):
                continue
        
        full_path = os.path.join(root, file)
        try:
            with open(full_path, "r", errors="ignore") as f:
                for line_number, line in enumerate(f, start=1):
                    if search_term in line:
                        print(f"Found in {full_path} at line {line_number}: {line.strip()}")
        except:
            print(f"Cannot read: {full_path}")
