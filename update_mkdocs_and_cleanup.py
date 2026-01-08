#!/usr/bin/env python
"""
Script to update mkdocs.yml and clean up marimo files
"""
import os
import shutil
from pathlib import Path
import yaml

def update_mkdocs_yml(mkdocs_path: str):
    """Update mkdocs.yml to point to .ipynb files instead of .py files"""

    with open(mkdocs_path, 'r') as f:
        content = f.read()

    original_content = content

    # Replace all Python marimo files with their ipynb counterparts
    # Pattern: python_fundamental_course/modules/moduleXX/XX_*.py -> python_fundamental_course/modules/moduleXX/XX_*.ipynb
    lines = content.split('\n')
    updated_lines = []

    for line in lines:
        # Check if line contains a Python file reference (but not __marimo__)
        if '.py' in line and '__marimo__' not in line:
            # Check if the referenced file has a corresponding ipynb
            # Extract the file path
            match = None
            if ': ' in line:
                parts = line.split(': ')
                if len(parts) == 2:
                    file_path = parts[1].strip()
                    if file_path.endswith('.py'):
                        # Check if this is a marimo file
                        full_path = Path('/home/abdullahalazmi/Programming/Euclidean-Norm/docs') / file_path
                        if full_path.exists():
                            try:
                                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                                    if 'import marimo' in f.read():
                                        # Replace .py with .ipynb
                                        ipynb_path = file_path.replace('.py', '.ipynb')
                                        ipynb_full = Path('/home/abdullahalazmi/Programming/Euclidean-Norm/docs') / ipynb_path
                                        if ipynb_full.exists():
                                            line = line.replace(file_path, ipynb_path)
                                            print(f"✓ Updated: {file_path} → {ipynb_path}")
                            except Exception as e:
                                print(f"✗ Error checking {full_path}: {e}")

        updated_lines.append(line)

    updated_content = '\n'.join(updated_lines)

    if updated_content != original_content:
        with open(mkdocs_path, 'w') as f:
            f.write(updated_content)
        print("\n✓ mkdocs.yml updated successfully")
    else:
        print("\n✗ No changes needed in mkdocs.yml")

    return updated_content != original_content

def remove_marimo_py_files():
    """Remove all marimo .py files"""
    workspace_root = Path('/home/abdullahalazmi/Programming/Euclidean-Norm/docs')
    removed = 0

    for py_file in workspace_root.rglob('*.py'):
        if '__pycache__' in str(py_file) or '__marimo__' in str(py_file):
            continue

        try:
            with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                if 'import marimo' in f.read():
                    os.remove(py_file)
                    print(f"✓ Removed: {py_file}")
                    removed += 1
        except Exception as e:
            print(f"✗ Error removing {py_file}: {e}")

    print(f"\nRemoved {removed} marimo .py files")
    return removed

def remove_marimo_directories():
    """Remove all __marimo__ directories"""
    workspace_root = Path('/home/abdullahalazmi/Programming/Euclidean-Norm/docs')
    removed = 0

    for marimo_dir in sorted(workspace_root.rglob('__marimo__')):
        try:
            shutil.rmtree(marimo_dir)
            print(f"✓ Removed directory: {marimo_dir}")
            removed += 1
        except Exception as e:
            print(f"✗ Error removing {marimo_dir}: {e}")

    print(f"\nRemoved {removed} __marimo__ directories")
    return removed

def main():
    mkdocs_path = '/home/abdullahalazmi/Programming/Euclidean-Norm/mkdocs.yml'

    print("=" * 60)
    print("Updating mkdocs.yml...")
    print("=" * 60)
    update_mkdocs_yml(mkdocs_path)

    print("\n" + "=" * 60)
    print("Removing marimo .py files...")
    print("=" * 60)
    remove_marimo_py_files()

    print("\n" + "=" * 60)
    print("Removing __marimo__ directories...")
    print("=" * 60)
    remove_marimo_directories()

    print("\n" + "=" * 60)
    print("Cleanup complete!")
    print("=" * 60)

if __name__ == "__main__":
    main()

