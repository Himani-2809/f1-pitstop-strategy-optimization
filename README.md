## F1 Pit-Stop Strategy Analysis

### Project Overview
This project explores Formula 1 pit-stop strategy using historical race data.
The objective is to understand how pit timing, tyre choices, and race conditions
affect performance, and to gradually build toward data-driven strategy models.

The work emphasizes **feature engineering, exploratory analysis, and structured experimentation**
rather than end-to-end prediction at this stage.

### Project Structure
├── src/                  # Data extraction and preprocessing scripts
├── notebooks/            # Phase-wise analysis notebooks
├── docs/                 # Assumptions and feature documentation
├── requirements.txt      # Python dependencies
└── README.md

### Methodology
1. Extract lap-level and race-level data using FastF1
2. Identify pit-stop events and compute pre/post pit performance metrics
3. Analyze race-specific behavior (selected circuits)
4. Study contextual factors such as tyre choice and temperature

### Current Status
- Phase 1: Baseline pit-stop feature extraction ✔
- Phase 2: Race-specific exploratory analysis ✔
- Phase 3: Environmental context analysis ✔

### Planned Extensions
- Multi-stop pit strategy modeling
- Team-specific strategy patterns
- Optimization-based pit timing models
- Strategy simulation under varying constraints

## Notes
This repository is designed to remain modular.  
Feature extraction logic is intentionally kept minimal and extensible to allow
future experiments to append or modify features based on specific research goals.
