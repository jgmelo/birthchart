# Birth Chart

A command-line tool to calculate planetary positions and render a simple polar birth chart.

## Requirements

- Python 3.10+
- See `requirements.txt` for Python package dependencies.

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the program with birth information:

```bash
python main.py --name "Ada" --date 1990-12-01 --time 13:30 \
    --city "Paris" --country "France"
```

The program resolves the location, calculates the chart using Flatlib, and displays a polar plot.

Metric results (if any) are printed to the console.
