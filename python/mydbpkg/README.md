# mydbpkg

Exercise package for learning Python packaging and basic MySQL CRUD helpers.

## Install (editable)

```bash
pip install -e .
```

## Usage

```python
from mydbpkg import db, repository
```

Notes:
- CRUD helpers live in `src/mydbpkg/repository.py`.
- Connection setup lives in `src/mydbpkg/db.py`.
