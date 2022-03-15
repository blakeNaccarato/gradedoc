from pathlib import Path
from shutil import copytree

CWD = Path.cwd()


def copy_scripts(path: Path = CWD):
    """Copy AutoHotkey scripts to the current directory."""
    import gradedoc

    scripts = Path(gradedoc.__file__).parent / "scripts"
    copytree(scripts, path / scripts.name)
