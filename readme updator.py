import os

# Read the content of README.md file
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()
    print(f"README content:\n{readme_content}\n")


# Get the names of folders in the current directory and sort them alphabetically
current_dir = os.getcwd()
folder_names = sorted([f for f in os.listdir(current_dir)
                       if os.path.isdir(os.path.join(current_dir, f)) and not f.startswith(".")])

# Create the new section for folder links
new_section = "\nFolders:\n"
for folder_name in folder_names:
    folder_path = os.path.join(".", folder_name)
    main_py_path = os.path.join(folder_path, "main.py")
    if os.path.isfile(main_py_path):
        main_py_link = f"[main.py]({main_py_path})"
        folder_link = f"[{folder_name}]({folder_path})"
        new_section += f"- {folder_link}: {main_py_link}\n"
    else:
        folder_link = f"[{folder_name}]({folder_path})"
        new_section += f"- {folder_link}\n"
new_section += "\n"

# Insert the new section into the README.md file
start_marker = "### Codes Here:"
end_marker = "### End Here"
start_index = readme_content.find(start_marker)
if start_index != -1:
    start_index += len(start_marker) + 1
    end_index = readme_content.index(end_marker) - 1
    new_readme_content = readme_content[:start_index] + new_section + readme_content[end_index:]
else:
    new_readme_content = readme_content + "\n\n" + new_section

# Write the updated content to README.md file
with open("README.md", "w") as readme_file:
    readme_file.write(new_readme_content)

# Confirm that changes were made to README.md
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()
    print(f"Updated README content:\n{readme_content}\n")
