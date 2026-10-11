# APPLICATION FOR DATA ACCUMULATION FOR EQUITY

## Running the Application

This project uses [uv](https://docs.astral.sh/uv/) to manage Python dependencies and the virtual environment.

### 1. Install dependencies

From the project root, run:

```bash
uv sync
```

### 2. Start the application

**Development:**

```bash
uv run fastapi dev --port 3003
```

**Production:**

```bash
uv run fastapi run --port 3003
```

Using `uv run` is the recommended approach because it runs the command in the project's environment without requiring you to activate the virtual environment manually.

### Alternative: Activate the virtual environment

You can activate `.venv` in your current shell and run the commands directly:

```bash
source .venv/bin/activate
```

Then start the application with either `fastapi dev --port 3003` or `fastapi run --port 3003`.
