# build_command.py

NAME = "João"
DATE = "1984-07-17"
TIME = "15:30"
CITY = "Belo Horizonte"
COUNTRY = "Brazil"

def build_command_from_dict(param_dict, base_command="python main.py"):
    """
    Construct a CLI command from a dictionary of arguments.
    
    Args:
        param_dict (dict): Keys are argument names (without "--"), values are the corresponding argument values.
        base_command (str): The base command to run (e.g., python main_panel.py)

    Returns:
        str: The full command-line string
    """
    parts = [base_command]

    for key, value in param_dict.items():
        if value is None or value == "":
            continue  # Skip empty values
        key_flag = f"--{key}"
        # If the value is a string and contains spaces, we wrap it in quotes
        if isinstance(value, str) and " " in value:
            value = f'"{value}"'
        parts.append(f"{key_flag} {value}")

    # Parameters and values are joined with spaces
    return " ".join(parts)


# Example usage
if __name__ == "__main__":
    user_input = {
        "name": NAME,
        "date": DATE,
        "time": TIME,
        "city": CITY,
        "country": COUNTRY
    }

    command = build_command_from_dict(user_input)
    print("🖥️ Command to run:")
    print(command)


# 🌐📦⚡
# Cache management for location data
# This module handles caching of location data to avoid repeated API calls.
# It uses a JSON file to store latitude and longitude for city-country pairs.

import json
import os

CACHE_FILE = "location_cache.json"

def load_cache():
    if not os.path.exists(CACHE_FILE):
        return {}

    if os.path.getsize(CACHE_FILE) == 0:
        # File exists but is empty
        return {}

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            # Returns a dictionary from the JSON file.
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Warning: Cache file is corrupted or empty. Reinitializing it.")
        return {}

def save_cache(cache):
    with open(CACHE_FILE, "w", encoding="utf-8") as f:
        json.dump(cache, f, ensure_ascii=False, indent=2)

def get_cached_location(city, country):
    cache = load_cache()
    # Key is a combination of city and country, both lowercased and stripped of whitespace.
    key = f"{city.strip().lower()},{country.strip().lower()}"
    return cache.get(key)

def cache_location(city, country, lat, lon):
    # Load existing cache. Returns None if file doesn't exist.
    cache = load_cache()
    # Key is a combination of city and country, both lowercased and stripped of whitespace.
    key = f"{city.strip().lower()},{country.strip().lower()}"
    cache[key] = {"lat": lat, "lon": lon}
    save_cache(cache)
