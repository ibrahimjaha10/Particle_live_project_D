# Particle Life

Semesterprojekt im Modul *Data Science und KI Infrastrukturen*

## Ziel

Wir simulieren viele Partikel in einer 2D-Welt. Jedes Partikel hat einen Typ, und eine
Interaktionsmatrix legt fest, wie stark sich zwei Typen anziehen oder abstoßen. Aus diesen Regeln entstehen von selbst Muster wie Cluster oder Ketten (emergentes Verhalten).

## Geplante Nutzung

Man startet die Simulation mit festen Parametern (z. B. Anzahl Partikel, Anzahl Typen, Seed)
und sieht die Partikel in einem Fenster in Bewegung. Die Simulation soll auch ohne Fenster
laufen, damit Tests und Benchmarks möglich sind.

## Installation


```bash
git clone https://github.com/ibrahimjaha10/Particle_live_project_D.git
cd Particle_live_project_D
uv sync
uv run pytest
```

## Qualitätschecks

Vor jedem Pull Request:

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

## Projektstruktur

- `src/particle_life/`: der Code
- `tests/`: Tests mit pytest
- `docs/architecture.md`: Architektur und Designentscheidungen
- `.github/workflows/ci.yml`: CI mit Ruff und pytest
- `pyproject.toml`: Projektkonfiguration
- `uv.lock`: genaue Versionen aller Pakete

## Team

- Marlon: Product Owner, Setup, Konfiguration, Integration
- Yassine: Simulationskern (Kräfte, Simulationsschritt)
- Tolga: Visualisierung und GUI
- Ibo: CI, Tests, Randbehandlung, Benchmark

## Regeln

- Niemand pusht direkt auf `main`
- Jede Aufgabe ist ein Issue und hat eine verantwortliche Person
- Pro Issue ein eigener Branch, z. B. `docs/4-readme`
- Eine andere Person reviewt und merged, die CI muss grün sein



