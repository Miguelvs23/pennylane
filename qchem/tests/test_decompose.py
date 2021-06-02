import os

import numpy as np

import pytest

from pennylane import qchem

ref_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), "test_ref_files")


@pytest.mark.parametrize(
    (
        "name",
        "core",
        "active",
        "mapping",
        "coeffs_ref",
        "pauli_strings_ref",
    ),
    [
        (
            "lih",
            [0],
            [1, 2],
            "jordan_WIGNER",
            np.array(
                [
                    -7.50915719e00 + 0.0j,
                    1.55924093e-01 + 0.0j,
                    1.40159380e-02 + 0.0j,
                    1.40159380e-02 + 0.0j,
                    1.55924093e-01 + 0.0j,
                    1.40159380e-02 + 0.0j,
                    1.40159380e-02 + 0.0j,
                    -1.50398257e-02 + 0.0j,
                    -1.50398257e-02 + 0.0j,
                    1.21827742e-01 + 0.0j,
                    1.21448939e-02 + 0.0j,
                    1.21448939e-02 + 0.0j,
                    1.21448939e-02 + 0.0j,
                    1.21448939e-02 + 0.0j,
                    3.26599399e-03 + 0.0j,
                    -3.26599399e-03 + 0.0j,
                    -3.26599399e-03 + 0.0j,
                    3.26599399e-03 + 0.0j,
                    5.26365152e-02 + 0.0j,
                    5.59025092e-02 + 0.0j,
                    -1.87104184e-03 + 0.0j,
                    -1.87104184e-03 + 0.0j,
                    5.59025092e-02 + 0.0j,
                    -1.87104184e-03 + 0.0j,
                    -1.87104184e-03 + 0.0j,
                    5.26365152e-02 + 0.0j,
                    8.44705692e-02 + 0.0j,
                ]
            ),
            [
                (),
                ((0, "Z"),),
                ((0, "Y"), (1, "Z"), (2, "Y")),
                ((0, "X"), (1, "Z"), (2, "X")),
                ((1, "Z"),),
                ((1, "Y"), (2, "Z"), (3, "Y")),
                ((1, "X"), (2, "Z"), (3, "X")),
                ((2, "Z"),),
                ((3, "Z"),),
                ((0, "Z"), (1, "Z")),
                ((0, "Y"), (2, "Y")),
                ((0, "X"), (2, "X")),
                ((0, "Z"), (1, "Y"), (2, "Z"), (3, "Y")),
                ((0, "Z"), (1, "X"), (2, "Z"), (3, "X")),
                ((0, "Y"), (1, "X"), (2, "X"), (3, "Y")),
                ((0, "Y"), (1, "Y"), (2, "X"), (3, "X")),
                ((0, "X"), (1, "X"), (2, "Y"), (3, "Y")),
                ((0, "X"), (1, "Y"), (2, "Y"), (3, "X")),
                ((0, "Z"), (2, "Z")),
                ((0, "Z"), (3, "Z")),
                ((0, "Y"), (1, "Z"), (2, "Y"), (3, "Z")),
                ((0, "X"), (1, "Z"), (2, "X"), (3, "Z")),
                ((1, "Z"), (2, "Z")),
                ((1, "Y"), (3, "Y")),
                ((1, "X"), (3, "X")),
                ((1, "Z"), (3, "Z")),
                ((2, "Z"), (3, "Z")),
            ],
        ),
        (
            "lih",
            [0],
            [1, 2],
            "BRAVYI_kitaev",
            np.array(
                [
                    -7.50915719e00 + 0.0j,
                    1.55924093e-01 + 0.0j,
                    1.40159380e-02 + 0.0j,
                    -1.40159380e-02 + 0.0j,
                    1.55924093e-01 + 0.0j,
                    -1.40159380e-02 + 0.0j,
                    1.40159380e-02 + 0.0j,
                    -1.50398257e-02 + 0.0j,
                    -1.50398257e-02 + 0.0j,
                    1.21827742e-01 + 0.0j,
                    1.21448939e-02 + 0.0j,
                    1.21448939e-02 + 0.0j,
                    -1.21448939e-02 + 0.0j,
                    1.21448939e-02 + 0.0j,
                    3.26599399e-03 + 0.0j,
                    3.26599399e-03 + 0.0j,
                    3.26599399e-03 + 0.0j,
                    3.26599399e-03 + 0.0j,
                    5.26365152e-02 + 0.0j,
                    5.59025092e-02 + 0.0j,
                    1.87104184e-03 + 0.0j,
                    1.87104184e-03 + 0.0j,
                    5.59025092e-02 + 0.0j,
                    1.87104184e-03 + 0.0j,
                    -1.87104184e-03 + 0.0j,
                    5.26365152e-02 + 0.0j,
                    8.44705692e-02 + 0.0j,
                ]
            ),
            [
                (),
                ((0, "Z"),),
                ((0, "X"), (1, "Y"), (2, "Y")),
                ((0, "Y"), (1, "Y"), (2, "X")),
                ((0, "Z"), (1, "Z")),
                ((0, "Z"), (1, "X"), (3, "Z")),
                ((1, "X"), (2, "Z")),
                ((2, "Z"),),
                ((1, "Z"), (2, "Z"), (3, "Z")),
                ((1, "Z"),),
                ((0, "Y"), (1, "X"), (2, "Y")),
                ((0, "X"), (1, "X"), (2, "X")),
                ((1, "X"), (3, "Z")),
                ((0, "Z"), (1, "X"), (2, "Z")),
                ((0, "Y"), (1, "Z"), (2, "Y"), (3, "Z")),
                ((0, "X"), (1, "Z"), (2, "X")),
                ((0, "X"), (1, "Z"), (2, "X"), (3, "Z")),
                ((0, "Y"), (1, "Z"), (2, "Y")),
                ((0, "Z"), (2, "Z")),
                ((0, "Z"), (1, "Z"), (2, "Z"), (3, "Z")),
                ((0, "X"), (1, "X"), (2, "X"), (3, "Z")),
                ((0, "Y"), (1, "X"), (2, "Y"), (3, "Z")),
                ((0, "Z"), (1, "Z"), (2, "Z")),
                ((0, "Z"), (1, "X"), (2, "Z"), (3, "Z")),
                ((1, "X"),),
                ((0, "Z"), (2, "Z"), (3, "Z")),
                ((1, "Z"), (3, "Z")),
            ],
        ),
        (
            "h2_pyscf",
            list(range(0)),
            list(range(2)),
            "jordan_WIGNER",
            np.array(
                [
                    -0.04207898 + 0.0j,
                    0.17771287 + 0.0j,
                    0.17771287 + 0.0j,
                    -0.24274281 + 0.0j,
                    -0.24274281 + 0.0j,
                    0.17059738 + 0.0j,
                    0.04475014 + 0.0j,
                    -0.04475014 + 0.0j,
                    -0.04475014 + 0.0j,
                    0.04475014 + 0.0j,
                    0.12293305 + 0.0j,
                    0.16768319 + 0.0j,
                    0.16768319 + 0.0j,
                    0.12293305 + 0.0j,
                    0.17627641 + 0.0j,
                ]
            ),
            [
                (),
                ((0, "Z"),),
                ((1, "Z"),),
                ((2, "Z"),),
                ((3, "Z"),),
                ((0, "Z"), (1, "Z")),
                ((0, "Y"), (1, "X"), (2, "X"), (3, "Y")),
                ((0, "Y"), (1, "Y"), (2, "X"), (3, "X")),
                ((0, "X"), (1, "X"), (2, "Y"), (3, "Y")),
                ((0, "X"), (1, "Y"), (2, "Y"), (3, "X")),
                ((0, "Z"), (2, "Z")),
                ((0, "Z"), (3, "Z")),
                ((1, "Z"), (2, "Z")),
                ((1, "Z"), (3, "Z")),
                ((2, "Z"), (3, "Z")),
            ],
        ),
        (
            "h2_pyscf",
            list(range(0)),
            list(range(2)),
            "BRAVYI_kitaev",
            np.array(
                [
                    -0.04207898 + 0.0j,
                    0.17771287 + 0.0j,
                    0.17771287 + 0.0j,
                    -0.24274281 + 0.0j,
                    -0.24274281 + 0.0j,
                    0.17059738 + 0.0j,
                    0.04475014 + 0.0j,
                    0.04475014 + 0.0j,
                    0.04475014 + 0.0j,
                    0.04475014 + 0.0j,
                    0.12293305 + 0.0j,
                    0.16768319 + 0.0j,
                    0.16768319 + 0.0j,
                    0.12293305 + 0.0j,
                    0.17627641 + 0.0j,
                ]
            ),
            [
                (),
                ((0, "Z"),),
                ((0, "Z"), (1, "Z")),
                ((2, "Z"),),
                ((1, "Z"), (2, "Z"), (3, "Z")),
                ((1, "Z"),),
                ((0, "Y"), (1, "Z"), (2, "Y"), (3, "Z")),
                ((0, "X"), (1, "Z"), (2, "X")),
                ((0, "X"), (1, "Z"), (2, "X"), (3, "Z")),
                ((0, "Y"), (1, "Z"), (2, "Y")),
                ((0, "Z"), (2, "Z")),
                ((0, "Z"), (1, "Z"), (2, "Z"), (3, "Z")),
                ((0, "Z"), (1, "Z"), (2, "Z")),
                ((0, "Z"), (2, "Z"), (3, "Z")),
                ((1, "Z"), (3, "Z")),
            ],
        ),
        (
            "h2o_psi4",
            list(range(3)),
            list(range(3, 6)),
            "jordan_WIGNER",
            np.array(
                [
                    -7.33320454e01 + 0.0j,
                    5.15279475e-01 + 0.0j,
                    7.77875498e-02 + 0.0j,
                    7.77875498e-02 + 0.0j,
                    5.15279475e-01 + 0.0j,
                    7.77875498e-02 + 0.0j,
                    7.77875498e-02 + 0.0j,
                    4.81292588e-01 + 0.0j,
                    4.81292588e-01 + 0.0j,
                    9.03094918e-02 + 0.0j,
                    9.03094918e-02 + 0.0j,
                    1.95659072e-01 + 0.0j,
                    3.03466140e-02 + 0.0j,
                    3.03466140e-02 + 0.0j,
                    1.39775966e-02 + 0.0j,
                    -1.39775966e-02 + 0.0j,
                    -1.39775966e-02 + 0.0j,
                    1.39775966e-02 + 0.0j,
                    3.03466140e-02 + 0.0j,
                    3.03466140e-02 + 0.0j,
                    1.71852512e-02 + 0.0j,
                    -1.71852512e-02 + 0.0j,
                    -1.71852512e-02 + 0.0j,
                    1.71852512e-02 + 0.0j,
                    1.68241745e-01 + 0.0j,
                    2.95127118e-02 + 0.0j,
                    2.95127118e-02 + 0.0j,
                    1.82219342e-01 + 0.0j,
                    2.90775939e-02 + 0.0j,
                    2.90775939e-02 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    1.20083139e-01 + 0.0j,
                    1.37268390e-01 + 0.0j,
                    1.11493731e-02 + 0.0j,
                    1.11493731e-02 + 0.0j,
                    1.82219342e-01 + 0.0j,
                    2.90775939e-02 + 0.0j,
                    2.90775939e-02 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    -4.35117913e-04 + 0.0j,
                    -4.35117913e-04 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    1.68241745e-01 + 0.0j,
                    2.95127118e-02 + 0.0j,
                    2.95127118e-02 + 0.0j,
                    1.37268390e-01 + 0.0j,
                    1.11493731e-02 + 0.0j,
                    1.11493731e-02 + 0.0j,
                    1.20083139e-01 + 0.0j,
                    2.20039773e-01 + 0.0j,
                    9.64747528e-03 + 0.0j,
                    -9.64747528e-03 + 0.0j,
                    -9.64747528e-03 + 0.0j,
                    9.64747528e-03 + 0.0j,
                    1.37589592e-01 + 0.0j,
                    1.47237067e-01 + 0.0j,
                    1.47237067e-01 + 0.0j,
                    1.37589592e-01 + 0.0j,
                    1.49282756e-01 + 0.0j,
                ]
            ),
            [
                (),
                ((0, "Z"),),
                ((0, "Y"), (1, "Z"), (2, "Z"), (3, "Z"), (4, "Y")),
                ((0, "X"), (1, "Z"), (2, "Z"), (3, "Z"), (4, "X")),
                ((1, "Z"),),
                ((1, "Y"), (2, "Z"), (3, "Z"), (4, "Z"), (5, "Y")),
                ((1, "X"), (2, "Z"), (3, "Z"), (4, "Z"), (5, "X")),
                ((2, "Z"),),
                ((3, "Z"),),
                ((4, "Z"),),
                ((5, "Z"),),
                ((0, "Z"), (1, "Z")),
                ((0, "Y"), (2, "Z"), (3, "Z"), (4, "Y")),
                ((0, "X"), (2, "Z"), (3, "Z"), (4, "X")),
                ((0, "Y"), (1, "X"), (2, "X"), (3, "Y")),
                ((0, "Y"), (1, "Y"), (2, "X"), (3, "X")),
                ((0, "X"), (1, "X"), (2, "Y"), (3, "Y")),
                ((0, "X"), (1, "Y"), (2, "Y"), (3, "X")),
                ((0, "Z"), (1, "Y"), (2, "Z"), (3, "Z"), (4, "Z"), (5, "Y")),
                ((0, "Z"), (1, "X"), (2, "Z"), (3, "Z"), (4, "Z"), (5, "X")),
                ((0, "Y"), (1, "X"), (4, "X"), (5, "Y")),
                ((0, "Y"), (1, "Y"), (4, "X"), (5, "X")),
                ((0, "X"), (1, "X"), (4, "Y"), (5, "Y")),
                ((0, "X"), (1, "Y"), (4, "Y"), (5, "X")),
                ((0, "Z"), (2, "Z")),
                ((0, "Y"), (1, "Z"), (3, "Z"), (4, "Y")),
                ((0, "X"), (1, "Z"), (3, "Z"), (4, "X")),
                ((0, "Z"), (3, "Z")),
                ((0, "Y"), (1, "Z"), (2, "Z"), (4, "Y")),
                ((0, "X"), (1, "Z"), (2, "Z"), (4, "X")),
                ((0, "Y"), (1, "Z"), (2, "Y"), (3, "Y"), (4, "Z"), (5, "Y")),
                ((0, "Y"), (1, "Z"), (2, "Y"), (3, "X"), (4, "Z"), (5, "X")),
                ((0, "X"), (1, "Z"), (2, "X"), (3, "Y"), (4, "Z"), (5, "Y")),
                ((0, "X"), (1, "Z"), (2, "X"), (3, "X"), (4, "Z"), (5, "X")),
                ((0, "Z"), (4, "Z")),
                ((0, "Z"), (5, "Z")),
                ((0, "Y"), (1, "Z"), (2, "Z"), (3, "Z"), (4, "Y"), (5, "Z")),
                ((0, "X"), (1, "Z"), (2, "Z"), (3, "Z"), (4, "X"), (5, "Z")),
                ((1, "Z"), (2, "Z")),
                ((1, "Y"), (3, "Z"), (4, "Z"), (5, "Y")),
                ((1, "X"), (3, "Z"), (4, "Z"), (5, "X")),
                ((1, "Y"), (2, "X"), (3, "X"), (4, "Y")),
                ((1, "Y"), (2, "Y"), (3, "X"), (4, "X")),
                ((1, "X"), (2, "X"), (3, "Y"), (4, "Y")),
                ((1, "X"), (2, "Y"), (3, "Y"), (4, "X")),
                ((1, "Z"), (3, "Z")),
                ((1, "Y"), (2, "Z"), (4, "Z"), (5, "Y")),
                ((1, "X"), (2, "Z"), (4, "Z"), (5, "X")),
                ((1, "Z"), (4, "Z")),
                ((1, "Y"), (2, "Z"), (3, "Z"), (5, "Y")),
                ((1, "X"), (2, "Z"), (3, "Z"), (5, "X")),
                ((1, "Z"), (5, "Z")),
                ((2, "Z"), (3, "Z")),
                ((2, "Y"), (3, "X"), (4, "X"), (5, "Y")),
                ((2, "Y"), (3, "Y"), (4, "X"), (5, "X")),
                ((2, "X"), (3, "X"), (4, "Y"), (5, "Y")),
                ((2, "X"), (3, "Y"), (4, "Y"), (5, "X")),
                ((2, "Z"), (4, "Z")),
                ((2, "Z"), (5, "Z")),
                ((3, "Z"), (4, "Z")),
                ((3, "Z"), (5, "Z")),
                ((4, "Z"), (5, "Z")),
            ],
        ),
        (
            "h2o_psi4",
            list(range(3)),
            list(range(3, 6)),
            "BRAVYI_kitaev",
            np.array(
                [
                    -7.33320454e01 + 0.0j,
                    5.15279475e-01 + 0.0j,
                    7.77875498e-02 + 0.0j,
                    -7.77875498e-02 + 0.0j,
                    5.15279475e-01 + 0.0j,
                    7.77875498e-02 + 0.0j,
                    -7.77875498e-02 + 0.0j,
                    4.81292588e-01 + 0.0j,
                    4.81292588e-01 + 0.0j,
                    9.03094918e-02 + 0.0j,
                    9.03094918e-02 + 0.0j,
                    1.95659072e-01 + 0.0j,
                    -3.03466140e-02 + 0.0j,
                    -3.03466140e-02 + 0.0j,
                    1.39775966e-02 + 0.0j,
                    1.39775966e-02 + 0.0j,
                    1.39775966e-02 + 0.0j,
                    1.39775966e-02 + 0.0j,
                    3.03466140e-02 + 0.0j,
                    -3.03466140e-02 + 0.0j,
                    1.71852512e-02 + 0.0j,
                    1.71852512e-02 + 0.0j,
                    1.71852512e-02 + 0.0j,
                    1.71852512e-02 + 0.0j,
                    1.68241745e-01 + 0.0j,
                    2.95127118e-02 + 0.0j,
                    -2.95127118e-02 + 0.0j,
                    1.82219342e-01 + 0.0j,
                    2.90775939e-02 + 0.0j,
                    -2.90775939e-02 + 0.0j,
                    -4.35117913e-04 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    -4.35117913e-04 + 0.0j,
                    -4.35117913e-04 + 0.0j,
                    1.20083139e-01 + 0.0j,
                    1.37268390e-01 + 0.0j,
                    1.11493731e-02 + 0.0j,
                    1.11493731e-02 + 0.0j,
                    1.82219342e-01 + 0.0j,
                    2.90775939e-02 + 0.0j,
                    -2.90775939e-02 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    -4.35117913e-04 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    4.35117913e-04 + 0.0j,
                    1.68241745e-01 + 0.0j,
                    2.95127118e-02 + 0.0j,
                    2.95127118e-02 + 0.0j,
                    1.37268390e-01 + 0.0j,
                    1.11493731e-02 + 0.0j,
                    -1.11493731e-02 + 0.0j,
                    1.20083139e-01 + 0.0j,
                    2.20039773e-01 + 0.0j,
                    9.64747528e-03 + 0.0j,
                    9.64747528e-03 + 0.0j,
                    9.64747528e-03 + 0.0j,
                    9.64747528e-03 + 0.0j,
                    1.37589592e-01 + 0.0j,
                    1.47237067e-01 + 0.0j,
                    1.47237067e-01 + 0.0j,
                    1.37589592e-01 + 0.0j,
                    1.49282756e-01 + 0.0j,
                ]
            ),
            [
                (),
                ((0, "Z"),),
                ((0, "X"), (1, "X"), (3, "Y"), (4, "Y"), (5, "X")),
                ((0, "Y"), (1, "X"), (3, "Y"), (4, "X"), (5, "X")),
                ((0, "Z"), (1, "Z")),
                ((0, "Z"), (1, "X"), (3, "Y"), (5, "Y")),
                ((1, "Y"), (3, "Y"), (4, "Z"), (5, "X")),
                ((2, "Z"),),
                ((1, "Z"), (2, "Z"), (3, "Z")),
                ((4, "Z"),),
                ((4, "Z"), (5, "Z")),
                ((1, "Z"),),
                ((0, "Y"), (1, "Y"), (3, "Y"), (4, "Y"), (5, "X")),
                ((0, "X"), (1, "Y"), (3, "Y"), (4, "X"), (5, "X")),
                ((0, "Y"), (1, "Z"), (2, "Y"), (3, "Z")),
                ((0, "X"), (1, "Z"), (2, "X")),
                ((0, "X"), (1, "Z"), (2, "X"), (3, "Z")),
                ((0, "Y"), (1, "Z"), (2, "Y")),
                ((1, "X"), (3, "Y"), (5, "Y")),
                ((0, "Z"), (1, "Y"), (3, "Y"), (4, "Z"), (5, "X")),
                ((0, "Y"), (4, "Y"), (5, "Z")),
                ((0, "X"), (1, "Z"), (4, "X")),
                ((0, "X"), (4, "X"), (5, "Z")),
                ((0, "Y"), (1, "Z"), (4, "Y")),
                ((0, "Z"), (2, "Z")),
                ((0, "X"), (1, "X"), (2, "Z"), (3, "Y"), (4, "Y"), (5, "X")),
                ((0, "Y"), (1, "X"), (2, "Z"), (3, "Y"), (4, "X"), (5, "X")),
                ((0, "Z"), (1, "Z"), (2, "Z"), (3, "Z")),
                ((0, "X"), (1, "Y"), (2, "Z"), (3, "X"), (4, "Y"), (5, "X")),
                ((0, "Y"), (1, "Y"), (2, "Z"), (3, "X"), (4, "X"), (5, "X")),
                ((0, "X"), (1, "X"), (2, "X"), (3, "Y"), (5, "Y")),
                ((0, "X"), (1, "Y"), (2, "Y"), (3, "X"), (4, "Z"), (5, "X")),
                ((0, "Y"), (1, "X"), (2, "Y"), (3, "Y"), (5, "Y")),
                ((0, "Y"), (1, "Y"), (2, "X"), (3, "X"), (4, "Z"), (5, "X")),
                ((0, "Z"), (4, "Z")),
                ((0, "Z"), (4, "Z"), (5, "Z")),
                ((0, "X"), (1, "X"), (3, "Y"), (4, "X"), (5, "Y")),
                ((0, "Y"), (1, "X"), (3, "Y"), (4, "Y"), (5, "Y")),
                ((0, "Z"), (1, "Z"), (2, "Z")),
                ((0, "Z"), (1, "X"), (2, "Z"), (3, "Y"), (5, "Y")),
                ((1, "Y"), (2, "Z"), (3, "Y"), (4, "Z"), (5, "X")),
                ((0, "Z"), (1, "Y"), (2, "X"), (3, "X"), (4, "Y"), (5, "X")),
                ((0, "Z"), (1, "Y"), (2, "Y"), (3, "X"), (4, "X"), (5, "X")),
                ((1, "Y"), (2, "Y"), (3, "Y"), (4, "Y"), (5, "X")),
                ((1, "Y"), (2, "X"), (3, "Y"), (4, "X"), (5, "X")),
                ((0, "Z"), (2, "Z"), (3, "Z")),
                ((0, "Z"), (1, "Y"), (2, "Z"), (3, "X"), (5, "Y")),
                ((1, "X"), (2, "Z"), (3, "X"), (4, "Z"), (5, "X")),
                ((0, "Z"), (1, "Z"), (4, "Z")),
                ((0, "Z"), (1, "X"), (3, "Y"), (4, "Z"), (5, "Y")),
                ((1, "Y"), (3, "Y"), (5, "X")),
                ((0, "Z"), (1, "Z"), (4, "Z"), (5, "Z")),
                ((1, "Z"), (3, "Z")),
                ((2, "Y"), (4, "Y"), (5, "Z")),
                ((1, "Z"), (2, "X"), (3, "Z"), (4, "X")),
                ((2, "X"), (4, "X"), (5, "Z")),
                ((1, "Z"), (2, "Y"), (3, "Z"), (4, "Y")),
                ((2, "Z"), (4, "Z")),
                ((2, "Z"), (4, "Z"), (5, "Z")),
                ((1, "Z"), (2, "Z"), (3, "Z"), (4, "Z")),
                ((1, "Z"), (2, "Z"), (3, "Z"), (4, "Z"), (5, "Z")),
                ((5, "Z"),),
            ],
        ),
    ],
)
def test_transformation(name, core, active, mapping, coeffs_ref, pauli_strings_ref, tol):
    r"""Test the correctness of the decomposed Hamiltonian for the (:math: `H_2, H_2O, LiH`)
    molecules using Jordan-Wigner and Bravyi-Kitaev transformations."""

    hf_file = os.path.join(ref_dir, name)

    qubit_hamiltonian = qchem.decompose(hf_file, mapping=mapping, core=core, active=active)

    coeffs = np.array(list(qubit_hamiltonian.terms.values()))
    pauli_strings = list(qubit_hamiltonian.terms.keys())

    assert np.allclose(coeffs, coeffs_ref, **tol)
    assert pauli_strings == pauli_strings_ref


def test_not_available_transformation():
    r"""Test that an error is raised if the chosen fermionic-to-qubit transformation
    is neither 'jordan_wigner' nor 'bravyi_kitaev'."""

    with pytest.raises(TypeError, match="transformation is not available"):
        qchem.decompose(
            os.path.join(ref_dir, "lih"),
            mapping="not_available_transformation",
            core=[0],
            active=[1, 2],
        )
