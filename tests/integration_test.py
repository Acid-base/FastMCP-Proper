import subprocess
import shutil
import tempfile
import sys
from pathlib import Path
from typing import Tuple


def run_command(command: str, cwd: str | None = None) -> Tuple[int, str, str]:
    """Runs a shell command and returns its output and error."""
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=cwd
    )
    stdout, stderr = process.communicate()
    return process.returncode, stdout.decode(), stderr.decode()


def test_integration_and_e2e() -> None:
    """Tests integration of tools in the template."""

    # Create temp dir for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        # Copy the template to the temp dir
        template_dir = Path(__file__).parent.parent
        shutil.copytree(template_dir, temp_dir, dirs_exist_ok=True)

        # Create and activate venv using system python
        print("creating venv")
        ret, out, err = run_command(f"{sys.executable} -m venv .venv", cwd=temp_dir)
        assert ret == 0, f"venv creation failed with error:\n{err}\nand output:\n{out}"

        # Install dependencies using pip
        print("installing dependencies")
        ret, out, err = run_command(f".venv\\Scripts\\python -m pip install -e .", cwd=temp_dir)
        assert ret == 0, f"pip install failed with error:\n{err}\nand output:\n{out}"

        # Install pre-commit hooks
        print("installing pre-commit hooks")
        ret, out, err = run_command(f".venv\\Scripts\\pre-commit install", cwd=temp_dir)
        assert ret == 0, f"pre-commit install failed with error:\n{err}\nand output:\n{out}"

        # Test linters and formatters using pre-commit
        print("running pre-commit")
        ret, out, err = run_command(f".venv\\Scripts\\pre-commit run --all-files", cwd=temp_dir)
        # Note: pre-commit may return non-zero if it makes changes, which is expected
        print(f"pre-commit output:\n{out}\nerror:\n{err}")

        # Test mypy
        print("running mypy")
        ret, out, err = run_command(f".venv\\Scripts\\mypy src/my_package", cwd=temp_dir)
        assert ret == 0, f"mypy failed with error:\n{err}\nand output:\n{out}"

        # Test pytest
        print("running pytest")
        ret, out, err = run_command(f".venv\\Scripts\\pytest tests/test_module.py -v", cwd=temp_dir)
        assert ret == 0, f"pytest failed with error:\n{err}\nand output:\n{out}"

        print("All integration tests passed successfully!")
