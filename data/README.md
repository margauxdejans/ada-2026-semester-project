# Data

- `raw/` — the data exactly as downloaded by `code/01_get_data.ipynb`. Never edited by hand.
- `processed/` — the cleaned data and model outputs written by `code/02_clean.ipynb` and `code/03_model.ipynb`.

## Source

| Data set | Source (URL) | Downloaded on | Licence | Included in repo? |
|----------|--------------|---------------|---------|-------------------|
| Horse racing — `horses_<year>.csv`, `races_<year>.csv`, 2010–2020 (22 files) | Kaggle, [hwaitt/horse-racing](https://www.kaggle.com/datasets/hwaitt/horse-racing) (uploader: hwaitt; scraped from public websites) | 21 Nov 2026 | [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/): non-commercial use only | No: not redistributed in this repository (scraped data, Requirement 4.15). Fetched by `01_get_data.ipynb` |


Data: "Horse Racing" by hwaitt, Kaggle, licensed CC BY-NC 4.0. Used here for non-commercial, academic purposes only.
The raw files are not included in this repository; `code/01_get_data.ipynb` downloads them.
The licence record saved by Kaggle's API is in `raw/dataset-metadata.json`.

### How to obtain the data

Either run `code/01_get_data.ipynb` with a Kaggle API token (instructions at the top of the notebook), or download
the 22 files by hand from the dataset page (*Download*, sign-in required) and put them in `data/raw/` unchanged.
The notebook then lists their sizes and row counts.

If licence or size prevents including the data (Requirement 4.15), commit only the download
code and describe here exactly how to obtain the data and what the licence permits.

Keep files under 100 MB (GitHub's limit), and use lowercase names without spaces or accents,
e.g. `prices_2020_2024.csv`.

## Cleaning log

Record every cleaning step and how many rows it affected, e.g. *dropped 412 rows with missing prices*.

- _TODO_
