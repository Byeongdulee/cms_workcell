#!/usr/bin/env python3
"""Example experiment application that uses the WEI client to run a workflow."""

import json
from pathlib import Path

from wei import ExperimentClient


def main() -> None:
    """Runs an example WEI workflow"""
    # This defines the Experiment object that will communicate with the WEI server
    exp = ExperimentClient("localhost", "8000", "Example_Program")

    # The path to the Workflow definition yaml file
    wf_path = Path(__file__).parent.parent / "workflows" / "example_workflow.yaml"

    # This runs the workflow
    run_info = exp.start_run(
        wf_path.resolve(),
        #payload={
        #    "wait_time": 5,
        #    "file_name": "experiment_output.jpg",
        #},
    )
    print(json.dumps(run_info, indent=2))

    # # The below line can be used to fetch the result and save it in our local directory
    # exp.get_wf_result_file(
    #     run_id=run_info["run_id"],
    #     filename=run_info["hist"]["Take Picture"]["action_msg"],
    #     output_filepath="experiment_output.jpg",
    # )


if __name__ == "__main__":
    main()
