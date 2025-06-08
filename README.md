# Metaheuristic Optimization

This repository provides code and example data for traffic-signal optimization
with reinforcement learning.  Raw bus OD and signal records (sampled from
`20220810`) are placed under `data/raw/` and can be processed into cleaned
tables using the helper modules under `src/tlops_tools`.

## Repository layout

```
├── data/
│   └── raw/                    # Original CSV inputs
│       ├── 90001220220810050000od.csv   # Sample OD table
│       └── signals/20220810/   # Signal state history
├── src/
│   └── tlops_tools/            # RL environment and training utilities
│       └── tools/
│           ├── Env.py
│           ├── Ppo.py
│           ├── Train.py
│           └── ...
```

## Quick start

1. **Prepare the environment**
   Install Python 3.8 with dependencies such as `pandas`, `numpy`,
   `tensorflow`, `sumolib` and `scikit-learn`.

2. **Preprocess sample data**
   Run the provided `main.py` script, which dispatches to the utilities in
   `src/tlops_tools`:
   ```bash
   python main.py
   ```
   This generates `data/processed/s_preprocessed.csv` and
   `data/processed/od_preprocessed.csv`.

3. **Train or test RL agents**
   Training and evaluation utilities are found under `src/tlops_tools/tools/`.
   The `runAll.py` helper can start multiple processes across predefined time
   plans.  For example:
   ```bash
   python src/tlops_tools/tools/runAll.py --run-type train --iteration 200
   ```

Refer to individual scripts for additional arguments and configuration options.
Configuration defaults are defined in `src/tlops_tools/tools/config.py`.

## License

The original repository did not specify a license file.  Consult the authors
before using the data or code in other projects.
