import os
from urllib.parse import quote

# Get the names of folders in the current directory and sort them alphabetically
current_dir = os.getcwd()
folder_names = sorted([f for f in os.listdir(current_dir) if os.path.isdir(os.path.join(current_dir, f)) and not f.startswith('.')])

# Add folder links to README.md
with open("README.md", "r+") as readme_file:
    readme_content = readme_file.read()
    start_marker = "### start"
    end_marker = "### end"
    start_index = readme_content.index(start_marker) + len(start_marker)
    end_index = readme_content.index(end_marker)
    readme_file.seek(0)
    readme_file.write(readme_content[:start_index])
    readme_file.write("Folders:\n")
    for folder_name in folder_names:
        folder_link = f"[{folder_name}](./{quote(folder_name)})"
        readme_file.write(f"- {folder_link}\n")
    readme_file.write("\n")
    readme_file.write(readme_content[end_index:])

# Confirm that changes were made to README.md
with open("README.md", "r") as readme_file:
    readme_content = readme_file.read()
    print(f"Updated README content:\n{readme_content}\n")
