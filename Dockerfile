# ── Base image ────────────────────────────────────────────────────────────────
FROM python:3.10-slim

# ── Set working directory ──────────────────────────────────────────────────────
WORKDIR /app

# ── Install dependencies first (layer-cached separately from source code) ─────
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ── Copy project source ────────────────────────────────────────────────────────
COPY src/         ./src/
COPY artifacts/   ./artifacts/
COPY notebook/    ./notebook/
COPY app.py       .

# ── Expose FastAPI port ────────────────────────────────────────────────────────
EXPOSE 8000

# ── Start the FastAPI server ───────────────────────────────────────────────────
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
