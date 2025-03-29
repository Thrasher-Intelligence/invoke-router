# invoke-router

**Dynamic module routing for curses-based TUIs and terminal apps.**

`invoke-router` simplifies command and panel routing by dynamically loading and running modules from a centralized, JSON-based registry. Ideal for modular terminal apps, curses TUIs, and any CLI tool that requires dynamic, flexible command invocation.

---

## Features

- ✅ **Dynamic Routing**: No hardcoding—route commands dynamically.
- ✅ **JSON Registry**: Manage all modules centrally in `panels.json`.
- ✅ **Alias Support**: Easily assign and resolve aliases for commands.
- ✅ **Graceful Fallback**: Built-in error handling when modules fail to load or run.
- ✅ **Clean & Modular**: Easy to integrate and expand into any Python CLI or TUI app.

---

## Installation

```bash
pip install invoke-router
```

---

## Quick Start

### Step 1: Create your `panels.json`

Create a file named `panels.json`:

```json
{
  "1": {
    "module": "examples.one",
    "label": "Page One",
    "aliases": ["one"]
  },
  "2": {
    "module": "examples.two",
    "label": "Page Two",
    "aliases": ["two"]
  }
}
```

Place it in `./config/panels.json` at your project root.

### Step 2: Invoke modules dynamically

```python
from invoke_router.invoke import invoke

# Load your panel by key or alias
invoke("1")  # Loads examples.one
invoke("two")  # Loads examples.two
```

### Panel structure

Each panel module should define a `run(stdscr)` function:

```python
# examples/one.py
import curses

def run(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 1, "Hello from Panel One")
    stdscr.refresh()
```

---

## Advanced Usage

### Custom panel registry path

You can customize the location of your panel registry:

```python
from invoke_router.utils.panel_registry import load_registry

panel_map = load_registry(path="path/to/your/panels.json")
```

---

## Contributing

Feel free to fork, open issues, or submit pull requests. Contributions and feedback are warmly welcomed!

---

## License

GPL License © Jake Eaker

