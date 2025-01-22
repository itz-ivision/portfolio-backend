import os
import subprocess

# Get the list of installed packages
installed_packages = subprocess.check_output(['pip', 'freeze'], text=True).splitlines()

# Read the required packages from requirements.txt
with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

# Find unused packages
unused_packages = [
    pkg.split('==')[0]
    for pkg in installed_packages
    if pkg not in required_packages
]

# Uninstall unused packages
for pkg in unused_packages:
    subprocess.run(['pip', 'uninstall', '-y', pkg])

print(f"Removed unused packages: {unused_packages}")
