# Iron Condor Daily Strategy
This repository contains an initial MVP scaffold for an options trading system.  
Currently, only the **architecture and scoping decisions** have been implemented.

---
## Goal:
A daily options strategy that can be backtested and paper-traded safely, with explicit risk controls and realistic execution assumptions.


--- 
## Key Design Choices (so far)
- Context
  - Daily
  - SPY (for liquidity)
  - Option Type = "European" but added an option to extend to American later
  - Minimal ML, No AI

#### Arch Choices 
- Python classes are immutable
  - Better for scaling and concurrency
  - Will break at high frequency but ok for this use case
- Backtest uses the SAME portfolio & pricing logic as live
  - Seems self-explanitory but doing this increases accuracy of backtesting

## Project Structure

```text
quant-options-mvp/
├── src/            # Source code (empty / scaffolding)
├── tests/          # Test folder (minimal pytest test)
├── pyproject.toml  # Project dependencies and metadata
└── README.md       # This file
