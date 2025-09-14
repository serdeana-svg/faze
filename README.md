# Faze

This repository includes a simple Python example for storing images, names, and actions in an SQLite database.

## Usage

1. Ensure you have Python 3 installed.
2. Run `python database.py` to create the `data.db` file.
3. Insert images with:

```python
from pathlib import Path
from database import insert_image

insert_image("Alice", "Running", Path("alice.jpg"))
```

4. Retrieve records with:

```python
from database import fetch_all
print(fetch_all())
```
