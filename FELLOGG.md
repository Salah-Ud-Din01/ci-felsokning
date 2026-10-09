# Fellogg

En rad per fel.

| Nr | Vad stod i loggen? | Lokalt eller på GitHub? | Hur tog du reda på orsaken? | Hur löste du det? |
|----|----|----|----|----|
| 1 | "Invalid workflow file ... yaml syntax on line 11" | GitHub | Körningen startade aldrig. Jag jämförde indraget i ci.yml. Rad 14 hade ett blanksteg för mycket. | Tog bort ett blanksteg. |
| 2 | "Unable to find lockfile at uv.lock, but --frozen was provided" | GitHub | Läste felet i det första röda steget. uv.lock saknades, och filen stod i .gitignore. | Tog bort raden ur .gitignore, körde uv lock och checkade in filen. |
| 3 | "F401 os imported but unused" i baseline.py rad 3 (ruff check) | GitHub, sedan lokalt | Körde samma kommando lokalt: uv run ruff check src tests. | Körde uv run ruff check --fix. |
| 4 | "2 files would be reformatted" (ruff format --check) | Lokalt | Körde nästa steg i workflowet lokalt innan GitHub hann köra det. | Körde uv run ruff format src tests. |
| 5 | "ModuleNotFoundError: No module named numpy" (pytest) | Lokalt | features.py importerar numpy, men numpy fanns inte i pyproject.toml. | Körde uv add numpy. |
| 6 | test_moving_average_window_two failed: [1.0, 1.666...] != [1.5, 2.5, 3.5] | Lokalt | Läste vad testet förväntade sig och började i moving_average. Kernel delades med (window + 1) i stället för window. | Ändrade till / window. Testet ändrades inte. |

## Vad jag lärde mig
Felen kommer i en kedja: när ett steg går grönt körs nästa, och då dyker nästa fel upp. Det snabbaste är att köra samma kommandon lokalt som workflowet. Jag använde Claude som stöd för att läsa loggarna.
