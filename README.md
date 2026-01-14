# Iron Condor Daily Strategy
This repository contains an initial MVP scaffold for an options trading system.  
Currently, only the **architecture and scoping decisions** have been implemented.

---
## Goal:
A daily options strategy that can be backtested and paper-traded safely, with explicit risk controls and realistic execution assumptions.

--- 

## Project Scope (so far)

- **Immutable design**  
  All core objects (Portfolio, Position, OptionContract) are intended to be frozen dataclasses.

- **Minimal ML / AI placeholders**  
  Planning for future regime tagging or signal processing. 

- **Repository structure set up**  
  - `src/` for main code  
  - `tests/` for unit tests  
  - `pyproject.toml` for project metadata / dependencies

- **Testing framework initialized**  
  - Minimal `pytest` setup to ensure the repository runs without errors

---

## Project Structure

```text
quant-options-mvp/
├── src/            # Source code (empty / scaffolding)
├── tests/          # Test folder (minimal pytest test)
├── pyproject.toml  # Project dependencies and metadata
└── README.md       # This file
