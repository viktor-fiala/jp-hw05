import json
import pathlib
import subprocess
import sys

expected = {
    "L01E01": 39,
    "L01E02": 38,
    "L01E03": 38,
    "L01E04PEP": 38,
    "L02E01": 36,
    "L02E02": 35,
    "L02E03": 35,
    "L02E04PEP": 37,
    "L03E01": 36,
    "L03E02": 31,
    "L04E01": 31,
    "L04E02": 32,
    "L04E03": 29,
    "L05E01": 31,
    "L05E02": 21,
    "L06E01": 17,
    "L06E02": 5,
}


def test_sum_points(tmp_path):
    # Skript se spouští ze složky, kde leží sum_points.py, data/ a results/.
    output_file = tmp_path / "testfile.json"

    completed = subprocess.run(
        [sys.executable, "sum_points.py", "--output", str(output_file)],
        cwd=pathlib.Path.cwd(),
        capture_output=True,
        text=True,
    )

    assert completed.returncode == 0, completed.stderr
    assert json.loads(output_file.read_text(encoding="utf-8")) == expected


def test_sum_points_requires_output():
    completed = subprocess.run(
        [sys.executable, "sum_points.py"],
        cwd=pathlib.Path.cwd(),
        capture_output=True,
        text=True,
    )

    assert completed.returncode != 0
