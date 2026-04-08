# GPSGPT

## Overview

This folder contains the prompt templates and prompt construction strategies used in **GPSGPT4Analysis** for geometric and multimodal geometric problem solving.  
It provides multiple prompting styles, including direct chain-of-thought prompting, progressive prompting, program-aided prompting, response refinement, and multimodal geometric prompting.

The purpose of this module is to make it easy to switch among different prompting strategies when evaluating large language models or multimodal large language models on geometry-related tasks.

---

## Folder Structure

```text
prompt/
├── __init__.py
├── COT.py
├── geometry_prompt.py
├── leastToMost.py
├── MathPrompter.py
├── multimodal_geometric_prompt.py
├── PAL.py
├── PS.py
├── RESPROMPT.py
└── SATLM.py
