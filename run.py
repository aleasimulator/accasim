from accasim.base.simulator_class import Simulator
from accasim.base.scheduler_class import FirstInFirstOut
from accasim.base.allocator_class import FirstFit

import threading
import time
import logging

logger = logging.getLogger("accasim")

def progress_monitor(simulator, total_jobs):
    last = 0

    while simulator.end_simulation_time is None:
        logger.info(
            f"Loaded jobs: {simulator.loaded_jobs}"            
        )
        
        time.sleep(5)

def main():
    # CHANGE HERE TO SELECT DIFFERENT WORKLOAD
    workload = "workloads/frontier2025.swf"
    sys_cfg = "config/frontier.json"

    allocator = FirstFit()
    dispatcher = FirstInFirstOut(allocator)

    simulator = Simulator(
        workload,
        sys_cfg,
        dispatcher,
        RESULTS_FOLDER_NAME="results",
        scheduling_output=True,
        statistics_output=True
    )

    threading.Thread(
       target=progress_monitor,
       args=(simulator,1),
       daemon=True
    ).start()

    simulator.start_simulation(
        system_status=False
    )


if __name__ == "__main__":
    main()