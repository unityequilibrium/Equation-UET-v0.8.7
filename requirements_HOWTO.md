# requirements.txt (recommended approach)

Because the harness evolves, **the safest way** is to generate requirements from your working venv and pin versions.

## Option A (recommended): export from your venv
Activate your venv, then:

```powershell
pip freeze > requirements.txt
python -V > PYTHON_VERSION.txt
```

Pros: exact reproducibility for your current state.

## Option B: minimal hand-written starter (then pin later)
Start with this, run, then pin with Option A:

```
numpy
pandas
matplotlib
```

If you see ImportError during run_suite/validators/plot, add missing packages and then re-pin with pip freeze.

## Option C: auto-detect (best-effort)
Install pipreqs and run:

```powershell
pip install pipreqs
pipreqs . --force
```

Caveat: may miss optional/runtime imports. Still re-pin with pip freeze for release.
