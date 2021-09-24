# Hello, World!

## Getting Started

```
python -m venv ENV
source ENV/bin/activate
pip install -r requirements.txt
```

## Running the Pipeline

### Using Dagit

```
dagit -f hello_world.py
```

### Using Dagster Python API

Add this code to the pipeline.

```py
from dagster import execute_pipeline


if __name__ == "__main__":
    result = execute_pipeline(hello_pipeline)
```

Then run

```sh
python hello_world.py
```

### Using Dagster CLI

```sh
dagster pipeline execute -f hello_world.py
```
