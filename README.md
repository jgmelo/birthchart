# Birth Chart

A command-line tool to calculate planetary positions and render a simple polar birth chart.

## Requirements

- Python 3.10+
- See `requirements.txt` for Python package dependencies.

Install dependencies with:

```bash
pip install -r requirements.txt
```

### OpenAI API

Interpretations use OpenAI's GPT models. Set the `OPENAI_API_KEY` environment
variable to your API key before running the program. Optionally set
`OPENAI_MODEL` to choose a model (defaults to `gpt-3.5-turbo`).

## Usage

Run the program with birth information:

```bash
python main.py --name "Ada" --date 1990-12-01 --time 13:30 \
    --city "Paris" --country "France"
```

The program resolves the location, calculates the chart using Flatlib, and displays a polar plot.

Metric results are printed to the console and a short interpretation is cached in
`interpretation_cache.json`. Each interpretation line is also appended to
`interpretations.txt` for later reference.
