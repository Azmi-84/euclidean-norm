#!/usr/bin/env python
"""
Script to convert marimo Python files to Jupyter notebooks and update mkdocs.yml
"""
import os
import sys
import json
import subprocess
from pathlib import Path

def convert_marimo_to_ipynb(py_file: str, output_ipynb: str) -> bool:
    """
    Convert a marimo Python file to Jupyter notebook using marimo export
    """
    try:
        # Use marimo to export the notebook
        result = subprocess.run(
            [sys.executable, "-m", "marimo", "export", "ipynb", py_file, "-o", output_ipynb],
            capture_output=True,
            text=True,
            cwd="/home/abdullahalazmi/Programming/Euclidean-Norm"
        )

        if result.returncode == 0:
            print(f"✓ Converted: {py_file} → {output_ipynb}")
            return True
        else:
            print(f"✗ Failed to convert {py_file}: {result.stderr}")
            return False
    except Exception as e:
        print(f"✗ Error converting {py_file}: {e}")
        return False

def main():
    workspace_root = Path("/home/abdullahalazmi/Programming/Euclidean-Norm")
    docs_dir = workspace_root / "docs"

    # Find all marimo Python files
    marimo_files = []
    for py_file in docs_dir.rglob("*.py"):
        if "__marimo__" in str(py_file) or "__pycache__" in str(py_file):
            continue

        with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
            if "import marimo" in f.read():
                marimo_files.append(py_file)

    print(f"Found {len(marimo_files)} marimo Python files to convert")

    successful = 0
    failed = 0

    for py_file in sorted(marimo_files):
        # Create output ipynb in same directory
        ipynb_file = py_file.with_suffix('.ipynb')

        if convert_marimo_to_ipynb(str(py_file), str(ipynb_file)):
            successful += 1
            # After successful conversion, we can optionally remove the .py file
            # (we'll handle this separately)
        else:
            failed += 1

    print(f"\nConversion complete: {successful} successful, {failed} failed")
    return failed == 0

if __name__ == "__main__":
    sys.exit(0 if main() else 1)

