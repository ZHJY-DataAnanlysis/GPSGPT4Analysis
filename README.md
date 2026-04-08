````markdown
#GPSGPT4Analysis

GPSGPT4Analysis is a geometry and multimodal geometry prompting framework for GPT4.  
It organizes multiple prompting strategies under a unified execution pipeline.

## Project Structure

```text
MGeoPrompting-main/
├── core/
│   ├── __init__.py
│   ├── backend.py
│   ├── interface.py
│   └── runtime.py
├── prompt/
│   ├── __init__.py
│   ├── COT.py
│   ├── geometry_prompt.py
│   ├── leastToMost.py
│   ├── MathPrompter.py
│   ├── multimodal_geometric_prompt.py
│   ├── PAL.py
│   ├── PS.py
│   ├── RESPROMPT.py
│   └── SATLM.py
````

## Main Files

### `core/interface.py`

Main entry of the project.
Used to run the whole prompting pipeline.

### `core/backend.py`

Backend logic for model calling and pipeline execution.

### `core/runtime.py`

Runtime utilities and configuration support.

### `prompt/`

Contains different prompting strategies, such as:

* `COT.py`: Chain-of-Thought prompting
* `leastToMost.py`: Least-to-Most prompting
* `PAL.py`: Program-Aided Language prompting
* `geometry_prompt.py`: geometry-specific prompts
* `multimodal_geometric_prompt.py`: multimodal geometry prompts

## How to Run

Enter the project directory:

```bash
cd MGeoPrompting-main
```

Run the program:

```bash
python core/interface.py
```

If needed, try:

```bash
python -m core.interface
```

Check available arguments:

```bash
python core/interface.py --help
```

## Workflow

A typical workflow is:

1. prepare a geometry problem
2. choose a prompting strategy
3. run `interface.py`
4. get the reasoning result

## Notes

* Run the program from the project root directory
* Make sure both `core/` and `prompt/` exist
* If import errors occur, use:

```bash
python -m core.interface
```

## Quick Start

```bash
cd MGeoPrompting-main
python core/interface.py
```

```
```
