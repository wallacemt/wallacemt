import re

DARK_GIFS = ["rain_astetic_dark.gif", "stairs_dark.gif", "underground_dark.gif"]
LIGHT_GIFS = ["building_white.gif", "stairs_white.gif"]

with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

match = re.search(
    r"<!-- ROTATING_GIF_START -->.*?assets/([^\s\"]+\.gif)", content, re.DOTALL
)
current_dark = match.group(1) if match else DARK_GIFS[0]

dark_idx = DARK_GIFS.index(current_dark) if current_dark in DARK_GIFS else 0
next_dark_idx = (dark_idx + 1) % len(DARK_GIFS)
next_light_idx = next_dark_idx % len(LIGHT_GIFS)

new_dark = DARK_GIFS[next_dark_idx]
new_light = LIGHT_GIFS[next_light_idx]

new_section = f"""<!-- ROTATING_GIF_START -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/{new_dark}" style="border-radius:50%;">
  <source media="(prefers-color-scheme: light)" srcset="assets/{new_light}" style="border-radius:50%;">
  <img src="assets/{new_dark}" alt="vibe" width="50%" style="border-radius:70%;"/>
</picture>
<!-- ROTATING_GIF_END -->"""

content = re.sub(
    r"<!-- ROTATING_GIF_START -->.*?<!-- ROTATING_GIF_END -->",
    new_section,
    content,
    flags=re.DOTALL,
)

with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print(f"Rotated → dark: {new_dark}  |  light: {new_light}")
