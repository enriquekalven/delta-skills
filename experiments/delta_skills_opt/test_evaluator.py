import pytest
import os
import json
from evaluator import evaluate_program, main
from initial_program import resolve_capability_slot

def test_evaluate_program(tmp_path):
    prog_file = tmp_path / "initial_program.py"
    with open("initial_program.py", "r", encoding="utf-8") as f:
        code = f.read()
    
    result = evaluate_program(code)
    assert result["score"] is not None
    assert result["score"] > 80.0
    assert len(result["insights"]) > 0

def test_evaluator_cli(tmp_path):
    out_file = tmp_path / "output.json"
    prog_dir = os.getcwd()
    
    import sys
    sys.argv = ["evaluator.py", "--program-dir", prog_dir, "--output-file", str(out_file)]
    main()
    
    assert out_file.exists()
    with open(out_file, "r") as f:
        data = json.load(f)
    assert data["score"] is not None
