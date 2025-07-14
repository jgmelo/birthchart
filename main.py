# main_panel.py

import argparse
from datetime import datetime
from geopy.geocoders import Nominatim
from helpers import get_cached_location, cache_location
from timezonefinder import TimezoneFinder
import pytz
import sys
from chart.drawing import render_chart

import chart.astro_calculations as astrocalc  # Assuming this is the module with get_chart_data
import chart.metrics as metrics

# ------------------------------
# 1. Parse CLI arguments
# ------------------------------

def parse_args():
    parser = argparse.ArgumentParser(description="Generate a graphical birth chart")
    parser.add_argument("--name", help="Name of the person", default="Unnamed")
    parser.add_argument("--date", required=True, help="Birth date in YYYY-MM-DD format")
    parser.add_argument("--time", required=True, help="Birth time in HH:MM (24h) format")
    parser.add_argument("--city", required=True, help="City of birth")
    parser.add_argument("--country", required=True, help="Country of birth")
    return parser.parse_args()

# ------------------------------
# 2. Validate and combine datetime
# ------------------------------

def validate_datetime(date_str, time_str):
    try:
        return datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Error: Invalid date or time format. Use YYYY-MM-DD and HH:MM.")
        sys.exit(1)

# ------------------------------
# 3. Get coordinates from location
# ------------------------------

def resolve_location(city, country):
    # Check cache first
    cached = get_cached_location(city, country)
    if cached:
        print("📦 Location found in cache.")
        return cached["lat"], cached["lon"]

    # If not cached, query Nominatim
    print("🌐 Querying Nominatim...")
    geolocator = Nominatim(user_agent="birth_chart_locator")
    location = geolocator.geocode(f"{city}, {country}")
    if not location:
        print(f"Error: Could not resolve location for {city}, {country}")
        sys.exit(1)

    lat, lon = location.latitude, location.longitude
    cache_location(city, country, lat, lon)
    return lat, lon

# ------------------------------
# 4. Get timezone from coordinates
# ------------------------------

def resolve_timezone(lat, lon):
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lng=lon, lat=lat)
    if not timezone_str:
        print("Error: Could not determine timezone for given coordinates.")
        sys.exit(1)
    return timezone_str

# ------------------------------
# 5. Convert local time to UTC
# ------------------------------

def convert_to_utc(local_dt, timezone_str):
    tz = pytz.timezone(timezone_str)
    local_aware = tz.localize(local_dt)
    return local_aware.astimezone(pytz.utc)

# ------------------------------
# 6. Main flow
# ------------------------------

def main():
    args = parse_args()

    print("🌐 Resolving location and time...")
    local_dt = validate_datetime(args.date, args.time)
    lat, lon = resolve_location(args.city, args.country)
    timezone_str = resolve_timezone(lat, lon)
    utc_dt = convert_to_utc(local_dt, timezone_str)

    print(f"\n📍 Location: {args.city}, {args.country}")
    print(f"🕰️ Local time: {local_dt} ({timezone_str})")
    print(f"🛰️ UTC time: {utc_dt}")
    print(f"📌 Coordinates: lat={lat:.4f}, lon={lon:.4f}\n")

    # Placeholder: Call astro calculations
    print("🔭 Calculating planetary positions...")
    chart_data = {
        # This will be returned from astro_calculations in future
        "planets": [],
        "houses": [],
        "aspects": [],
        "ascendant": None,
    }
    
    chart_data = astrocalc.get_chart_data(utc_dt, lat, lon)

    # Compute metrics
    metric_results = metrics.compute_all(chart_data)
    for name, result in metric_results.items():
        print(f"{name}: {result}")

    # Placeholder: Call chart rendering
    print("🎨 Rendering chart...")
    render_chart(chart_data, name=args.name)

    print("\n✅ Done!")

if __name__ == "__main__":
    main()
