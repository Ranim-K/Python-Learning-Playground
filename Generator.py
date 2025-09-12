# project_creator.py

# Ask user for project name
project_name = input("Enter your project name: ")

# Add .py extension
filename = f"{project_name}.py"

# Define the signature block
top_signature = "# >>>>> 🌟 CodeHero Journey 🌟 <<<<<"
bottom_signature = "# <<<<< 🚀 Program 1 of 100 🚀 >>>>>"

# Open file and write
with open(filename, "w", encoding="utf-8") as f:
    f.write(top_signature + "\n")
    f.write("\n" * 10)  # 10 empty lines
    f.write(bottom_signature + "\n")

print(f"✅ File '{filename}' created successfully!")
