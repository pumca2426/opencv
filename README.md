# OpenCV Image Tools

Lightweight utilities for comparing and inspecting images using OpenCV and NumPy.

This folder contains a small utility script to compare images (`image_compare.py`) and a contained virtual environment (`venvopencv`) with OpenCV and NumPy preinstalled for Windows.

**Status:** Minimal utility — extend or adapt for your workflows.

## Contents
- `image_compare.py` — main comparison script (see script help for options).
- `venvopencv/` — optional Windows virtual environment with OpenCV and NumPy already installed.

## Features
- Compare two images and report similarity metrics (pixel difference, basic statistics).
- Optionally show or save a visual diff (depends on `image_compare.py` options).

## Requirements
- Windows (tested with the included virtual environment).
- Python 3.13 (the provided `venvopencv` packages target CPython 3.13).
- If you don't use the included venv: `opencv-python`, `numpy`.

## Using the included virtual environment (Windows)
To use the supplied environment, activate it from PowerShell or CMD.

PowerShell:

```powershell
.\venvopencv\Scripts\Activate.ps1
python -V
python image_compare.py --help
```

Command Prompt (cmd.exe):

```bat
.\venvopencv\Scripts\activate.bat
python -V
python image_compare.py --help
```

If you prefer creating a fresh environment:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install opencv-python numpy
```

## Basic usage
The script accepts two image paths and prints comparison results. Check the script's help for full options:

```powershell
python image_compare.py <imageA> <imageB>
python image_compare.py img1.png img2.png --show --save-diff diff.png
python image_compare.py --help
```

Replace the example flags above with the actual options reported by `--help`.

## Troubleshooting
- Cannot import `cv2` or `numpy`: activate the included `venvopencv` or install `opencv-python` and `numpy` into your active environment.
- Different Python version: the included venv targets CPython 3.13. Use a matching interpreter when activating the venv.

## Contributing
- Open an issue or create a pull request with improvements to `image_compare.py` or additional tools.
- Add tests and update the README with example outputs for new features.

## License
This folder does not include an explicit license. Add a `LICENSE` file if you wish to make the code reusable under a specific license.

---

If you'd like, I can:
- Run `python image_compare.py --help` to capture and add the script's exact usage text to this README.
- Add an example output section with a sample pair of images.

Enjoy — ask me to extend the README with examples or to document `image_compare.py`'s options.

