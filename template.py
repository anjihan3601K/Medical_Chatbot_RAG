import os

# Creating directory structure
os.makedirs('src', exist_ok=True)
os.makedirs('research', exist_ok=True)

# Creating files
files = [
    'src/__init__.py',
    'src/helper.py',
    'src/prompt.py',
    '.env',
    'setup.py',
    'app.py',
    'research/trials.ipynb',
    'requirements.txt'
]

for file in files:
    # "touch" the file by opening and closing it
    open(file, 'a').close()

print("Directory and files created successfully!.")
