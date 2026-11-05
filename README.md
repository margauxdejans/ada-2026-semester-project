# ada-2026-semester-project

End-of-semester project (Autumn 2026) for the Advanced Data Analytics course at HEC Lausanne.

**Author:** _TODO: full name, as registered at the University_

## What the project does

_TODO: two sentences — the research question, the data, and the methods._

## What the repository holds

```
paper.pdf              the research paper (SIAM style, ~10 pages)   — TODO: add
README.md              this file: how to reproduce, in order
requirements.txt       the packages needed
recording.mp4          ~15-minute presentation, or a link below if too large — TODO: add
code/
  01_get_data.ipynb    stage 1: download the raw data  -> data/raw/
  02_clean.ipynb       stage 2: clean it               -> data/processed/
  03_model.ipynb       stage 3: fit the models         -> data/processed/
  04_figures.ipynb     stage 4: figures and tables     -> figures/
  helpers.py           code used in more than one notebook
data/                  the data, or the instructions that fetch it (see data/README.md)
figures/               every figure and table that appears in the paper
paper/outline.tex      section skeleton for the Overleaf SIAM template
```

## What to install

```bash
pip install -r requirements.txt
```

## What to run, in order

Run each notebook from top to bottom in a freshly started kernel:

1. `code/01_get_data.ipynb`
2. `code/02_clean.ipynb`
3. `code/03_model.ipynb`
4. `code/04_figures.ipynb`

Or run all of them from the command line:

```bash
for nb in code/0*.ipynb; do jupyter nbconvert --to notebook --execute --inplace "$nb"; done
```

## Running time and resources

- Approximate total running time: _TODO (e.g. ~5 minutes)_ on the provided Nuvolos workspace.
- Resources beyond the provided workspace: _TODO: none / describe them, and what each result was run on._
- API keys: _TODO: none / name the key needed and the environment variable it is read from._

## What it produces

_TODO: list the files written to `data/processed/` and `figures/`, and which figure or table of the paper each one is._

## Where the data came from

_TODO: source, URL, download date and licence. Details are in [`data/README.md`](data/README.md)._

## Recording

_TODO: `recording.mp4` in this repository, or a working link here if the file is too large._

## Declaration of tools and reused code

See the appendix of the paper. The initial repository scaffold (folder layout, `helpers.py`,
notebook templates, this README template and `paper/outline.tex`) was generated with Claude Code.
