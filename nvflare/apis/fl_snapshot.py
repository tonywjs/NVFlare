# Copyright (c) 2021-2022, NVIDIA CORPORATION.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


class RunSnapshot:
    """RunSnapshot keeps a snapshot of all the FLComponent states.

    The format is:
            { component_id: component_state_dict }
    """

    def __init__(self) -> None:
        super().__init__()
        self.component_states = {}
        self.completed = False

    def get_component_snapshot(self, component_id: str) -> dict:
        """Get a state snapshot of a particular FL component.

        Args:
            component_id: Component ID

        Returns:
            A component state dict.
        """
        return self.component_states.get(component_id)

    def set_component_snapshot(self, component_id: str, component_state: dict):
        """Set the snapshot of a particular FL component.

        Args:
            component_id: Component ID
            component_state: component state dict
        """
        self.component_states[component_id] = component_state

    def get_snapshot(self) -> dict:
        return self.component_states


class FLSnapshot:
    """FLSnapshot keeps a snapshot of all the current running FL application RunSnapshots.

    The format is:
            { run_number: RunSnapshot }
    """

    def __init__(self) -> None:
        super().__init__()
        self.run_snapshots = {}

    def add_snapshot(self, run_number: str, snapshot: RunSnapshot):
        """Add the RunSnapshot for run_number to the FLSnapshot.

        Args:
            run_number: the run_number
            snapshot: snapshot of the Run

        Returns:

        """
        self.run_snapshots[run_number] = snapshot

    def get_snapshot(self, run_number: str) -> RunSnapshot:
        """Get the RunSnapshot for run_number to the FLSnapshot.

        Args:
            run_number: the run_number

        Returns: Snapshot of the Run

        """
        return self.run_snapshots.get(run_number)

    def remove_snapshot(self, run_number: str):
        """Remove the RunSnapshot of run_number from the FLSnapshot.

        Args:
            run_number: the run_number

        Returns:

        """
        if run_number in self.run_snapshots.keys():
            self.run_snapshots.pop(run_number)