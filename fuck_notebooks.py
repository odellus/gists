# -*- coding: utf-8
"""fuck_notebooks.py

Description
===========
Fuck a bunch of notebooks. Just show me the damn code.
"""
import os
import json
import argparse

parser = argparse.ArgumentParser(description="Fuck Notebooks")
parser.add_argument("root", metavar="root", type=str,
    help="A root directory filled with a bunch of god damn notebooks.")

args = parser.parse_args()
print(args.root)


def load_json(fpath):
    """Load a JSON file.

    Params
    ======
        fpath (str): The file path of a JSON file to open.
    """
    with open(fpath, "r") as f:
        return json.load(f)


def pull_code(notebook):
    """Pull code cells out of a IPython Notebook.

    Params
    ======
        notebook (dict): An IPython notebook (.ipynb) format dictionary.
    """
    cells = notebook["cells"]
    code = []
    for cell in cells:
        if cell["cell_type"] == "code":
            code.extend(cell["source"] + ["\n"])
    return ''.join(code)


def write_code(code, fpath):
    """Write the code to a new Python file.

    Params
    ======
        code (str): The code pulled from the notebook.
        fpath (str): The file path of a JSON file to open.
    """
    with open(fpath, "w") as f:
        f.write(code)


def replace_ipynb(root):
    """Replace all IPython Notebooks in a directory with Python files.
    NOTE: Does NOT replace the notebooks but adds a .py file with the same name.

    Params
    ======
        root (str): The root directory containing a bunch of damn notebooks.
    """
    for (dirpath, dirname, fnames) in os.walk(root):
        for fname in fnames:
            name, ext = os.path.splitext(fname)
            if ext == ".ipynb":
                in_fpath = "{}/{}".format(dirpath, fname)
                out_fpath = "{}/{}".format(dirpath, name + ".py")
                notebook = load_json(in_fpath)
                code = pull_code(notebook)
                write_code(code, out_fpath)

def main(args):
    """Load a JSON file.

    Params
    ======
        args (Namespace): The arguments passed in through argparse. Consists of
        root exclusively at this time.
    """
    replace_ipynb(args.root)

if __name__ == "__main__":
    main(args)
