# Copyright 2018-2022 Xanadu Quantum Technologies Inc.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Code for the tape transform implementing the deferred measurement principle."""
import math

import pennylane as qml
from pennylane.transforms import qfunc_transform, ctrl
from pennylane.queuing import apply
from pennylane.tape import QuantumTape

@qfunc_transform
def defer_measurements(tape):

    with QuantumTape() as new_tape:
        for op in tape.queue:
            if isinstance(op, qml.ops.mid_circuit_measure._MidCircuitMeasure):
                pass

            elif op.__class__.__name__ == "_IfOp":
                control = op.dependant_measurements
                flipped = [False] * len(control)
                for branch, value in op.branches.items():
                    if value:
                        flip_wires = []
                        for i, wire_val in enumerate(branch):
                            if wire_val and flipped[i] or not wire_val and not flipped[i]:
                                flip_wires.append(control[i])
                        if flip_wires:
                            qml.RZ(math.pi, wires=flip_wires)
                        controlled_op = ctrl(op.construct_op, control=control)()
                flip_wires = []
                for i, flip in enumerate(flipped):
                    if flip:
                        flip_wires.append(control[i])
                if flip_wires:
                    qml.RZ(math.pi, wires=flip_wires)

            else:
                apply(op)

    return new_tape
