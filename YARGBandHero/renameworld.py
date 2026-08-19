import os
import re

def process_files():
    current_dir = os.getcwd()
    py_files = [f for f in os.listdir(current_dir) if f.endswith('.py') and f != os.path.basename(__file__)]
    
    if not py_files:
        print("No Python files found in the current directory.")
        return

    for filename in py_files:
        filepath = os.path.join(current_dir, filename)
        
        with open(filepath, 'r', encoding='utf-8') as f:
            original = f.read()
        
        modified = original.replace('RockBand2', 'BandHero')
        modified = modified.replace('Rock Band 2', 'Band Hero')
        
        if modified != original:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified)
            print(f"Updated: {filename}")
        else:
            print(f"No changes: {filename}")

process_files()