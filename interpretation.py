import json
import os
import openai

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")
OPENAI_API_KEY = "hidden"

CACHE_FILE = "interpretation_cache.json"
INTERPRETATIONS_FILE = "interpretations.txt"

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}
    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def get_or_generate(key, generator):
    cache = load_cache()
    # if key in cache:
    #     return cache[key]
    text = generator()
    cache[key] = text
    save_cache(cache)
    return text

def default_generate(metric_name, result):
    """Generate an interpretation using OpenAI's chat completion API."""
    print("✨ In default_generate")
    prompt = (
        "Provide a concise astrological interpretation for the following metric, in Brazilian Portuguese:\n"
        f"Metric: {metric_name}\nResult: {result}\n"
    )
    client = openai.OpenAI(api_key=OPENAI_API_KEY)  # or set via environment variable
    try:
        print("🔍 Generating interpretation with OpenAI API...")
        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.choices[0].message.content.strip()
    except Exception as e:
        print(f"❗ Error: {e}")
        print("❌ Error generating interpretation with OpenAI API. Using default text.")
        text = f"Interpretation for {metric_name}: {result}"
    return text

def write_interpretation(text):
    with open(INTERPRETATIONS_FILE, "a", encoding="utf-8") as f:
        f.write(text + "\n")

