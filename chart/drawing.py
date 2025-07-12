# drawing.py

import matplotlib.pyplot as plt
import numpy as np

def render_chart(chart_data, name="Unnamed"):
    """
    Renders a circular birth chart from precomputed data.
    """
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={'projection': 'polar'})
    ax.set_theta_direction(-1)   # Clockwise
    ax.set_theta_offset(np.pi / 2)  # Start at top (Ascendant)

    ax.set_xticks([])  # No default labels
    ax.set_yticks([])  # No radial grid

    # === Draw Zodiac Wheel ===
    for i in range(12):
        start_angle = i * 30
        theta = np.deg2rad(start_angle)
        ax.plot([theta, theta], [0, 1], color='black', lw=1)
        sign_label = get_zodiac_label(i)
        ax.text(np.deg2rad(start_angle + 15), 1.05, sign_label,
                ha='center', va='center', fontsize=20, fontweight='bold')

    # === Plot Houses ===
    for house in chart_data['houses']:
        theta = np.deg2rad(house['lon'])
        ax.plot([theta, theta], [0, 1], color='blue', lw=1.5, linestyle='--')
        ax.text(theta, 0.75, f"H{house['number']}", ha='center', va='center', fontsize=14, color='blue')

    # === Plot Planets ===
    for planet in chart_data['planets']:
        theta = np.deg2rad(planet['lon'])
        ax.plot(theta, 0.55, marker='o', color='red', markersize=6)
        ax.text(theta, 0.62, get_planet_symbol(planet['name']), ha='center', va='center', fontsize=14, color='darkred')

    # === Plot Ascendant ===
    asc_theta = np.deg2rad(chart_data['ascendant']['lon'])
    ax.plot([asc_theta], [0.9], marker='o', color='green', markersize=6)
    ax.text(asc_theta, 0.97, "ASC", ha='center', va='center', fontsize=9, color='green', fontweight='bold')

    # === Title ===
    ax.set_title(f"Mapa Astral de {name}", fontsize=14, pad=20)

    plt.tight_layout()
    plt.show()


def get_zodiac_label(index):
    """Returns Unicode glyphs for zodiac signs based on 0-based index (0=Aries)."""
    glyphs = ['♈', '♉', '♊', '♋', '♌', '♍',
              '♎', '♏', '♐', '♑', '♒', '♓']
    return glyphs[index % 12]

def get_planet_symbol(name):
    symbols = {
        'SUN': '☉',
        'MOON': '☽',
        'MERCURY': '☿',
        'VENUS': '♀',
        'MARS': '♂',
        'JUPITER': '♃',
        'SATURN': '♄'
    }
    return symbols.get(name.upper(), name.title())  # fallback to name if missing
