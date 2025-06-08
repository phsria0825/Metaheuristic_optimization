# Metaheuristic Optimization

This repository provides code and sample data for traffic-signal optimization
with reinforcement learning.  Raw bus OD and signal records (sampled from
`20220810`) are placed under `data/raw/`.

Preprocessing helpers referenced in the code base are incomplete.  The
included utilities primarily generate scenario folders and time-plan tables
for reinforcement learning experiments.

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

2. **Initialize the scenario**
   Run the provided `main.py` script.  This script adds
   `src/tlops_tools/tools` to the path and invokes the preprocessing module to
   create the `outputs/` directory and a `time_plan_with_begin_sec.pkl` file:
   ```bash
   python main.py
   ```
   Data-cleaning helpers mentioned in the code (`preprocess_signal_data`,
   `preprocess_demand_data`) are not included in this repository.

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
