# AccaSim for Very Large HPC System Simulations (Exascale+)

This repository contains a slightly modified version of the AccaSim simulator, adapted to support large-scale simulations of exascale-like systems (Aurora, Frontier).

The original simulator implementation was unable to complete even relatively short segments of real exascale workload traces within a reasonable amount of time (or it crashed).

**Main modifications:**

- Fixed the threading issue in the method responsible for writing simulation results to a file.
- Fixed the import statement `import collections.abc` (formerly part of `collections`).
- Added the bounded slowdown metric to the simulation output.
- Added workload traces and system configuration `.json` files to the `./workload` and `./config` directories, respectively.

## How to Run the Simulator

In `run.py`, edit lines 23 and 24 to select the workload and the `.json` file describing the HPC system infrastructure, e.g.:

```python
workload = "workloads/frontier2025.swf"
sys_cfg = "config/frontier.json"
```

Save the `run.py` file and execute the following commands:

```bash
cd accasim
python -m venv .venv
source .venv/bin/activate
pip install matplotlib psutil sortedcontainers numpy scipy
python run.py
```

**Note:** If you encounter any problems when running the simulator, consult an AI chatbot with the error message. Most likely, the issue will be a minor incompatibility related to the Python version. We tested the simulator with `Python 3.14`.

---

# AccaSim: A Workload Management Simulator for Job Dispatching Research

*Current version:* |version|

AccaSim is a Workload management [sim]ulator for [H]PC systems, useful for developing dispatchers and conducting controlled experiments in HPC dispatching research. It is scalable and highly customizable, allowing users to carry out large experiments across different workload sources, resource settings, and dispatching methods.

AccaSim enables users to design novel advanced dispatchers by exploiting information regarding the current system status, which can be extended to include custom behaviors such as power consumption and resource failures. Researchers can use AccaSim, for instance, to mimic any real system by configuring synthetic resources appropriately, develop advanced power-aware and fault-resilient dispatching methods, and test them over a wide range of workloads by generating them synthetically or using real workload traces from HPC users.

For more information, please visit the [AccaSim webpage](http://accasim.readthedocs.io/en/latest/).

## What's New?

- **10-11-2026:** Fixes to avoid crashes on large datasets (exascale-like).
- **23-06-2018:** Major improvements. Additional data is executed during Submission, Dispatching and Completion events (before and after).
- **15-06-2018:** Version 1.0 released.
- **01-06-2018:** New version of the dispatchers. Job requests are verified during the scheduling process.
- **27-05-2018:** New version of the resources and resource manager. All simulation methods were improved. Logger is used instead of printing messages.
- **21-05-2018:** Asynchronous file writing to reduce the I/O overhead of the simulations.
- **06-12-2017:** A workload generator is available for generating new workloads from existing workloads.
- **13-11-2017:** Simulating distinct dispatchers under the same system and simulator configuration can be managed under the Experimentation class. It also includes automatic plot generation.
- **21-08-2017:** Automatic plot generation for comparison of multiple workload schedules and benchmark files: Slowdown, Queue sizes, Load ratio, Efficiency, Scalability, Simulation time, Memory Usage.
- **19-07-2017:** Documentation moved to [http://accasim.readthedocs.io](http://accasim.readthedocs.io/en/latest/).
- **12-07-2017:** First version of the package.