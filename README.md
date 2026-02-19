# Interactive Three-Way ANOVA Calculator

A robust Python utility for performing **Three-Way Analysis of Variance (ANOVA)**. This tool is designed for researchers and students who need an interactive way to analyze the influence of three categorical factors on a single continuous variable.

---

## Features
- **File Support:** Reads `.csv` and `.xlsx` (Excel) files.
- **Interactive CLI:** No coding required to run, but follow the prompts to select your variables.
- **Special Character Support:** Uses `statsmodels` with `Q()` wrapping to handle column names containing spaces or symbols.
- **Significance Summary:** Automatically extracts and lists effects that meet your $p$-value threshold.
- **Scientific Notation:** Supports high-precision data (e.g., `1e-24`).

---

## Installation

Ensure you have Python 3.x installed. You will need the following libraries:

```bash
pip install pandas statsmodels openpyxl
