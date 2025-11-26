 Crowd Density Demo — Lightweight Proof of Concept

Short description
This repository contains a minimal, reproducible demonstration of a crowd-density estimation workflow. The implementation is intentionally lightweight and CPU-friendly: it estimates relative crowd density from a single image using simple, explainable image statistics. The purpose of this demo is educational — to provide a runnable example that can be evaluated by an instructor and extended later with state-of-the-art models (e.g., CSRNet, MCNN, P2PNet).

Intended audience
Undergraduate or postgraduate students preparing a coursework submission who need a working GitHub repository with clear instructions and a simple demo that produces visible output.

 Repository contents
- `inference.py` — Python script that runs a deterministic density estimate on an input image and writes an annotated output image.
- `requirements.txt` — Python dependencies required to run the demo.
- `sample_images/` — optional directory for small sample images (add via GitHub upload or local copy).
- `run_demo.sh` — convenience shell script to create a virtual environment, install dependencies, and run the demo (Linux / macOS / Git Bash on Windows).

 Dataset
This demo does not include large datasets. For a full research project, consider the following public datasets:
- HAJJv2 (KAU-Smart-Crowd) — Hajj crowd videos focused on abnormal behavior and crowd events.
- ShanghaiTech — common benchmark for crowd counting.

Do not upload large datasets to GitHub. Instead, provide download links and instructions in this README.

 Installation (recommended)
1. Clone or download the repository.
2. Create and activate a Python virtual environment.

```bash
 Create virtual environment (Linux / macOS)
python3 -m venv venv
source venv/bin/activate

 On Windows (PowerShell)
 python -m venv venv
 venv\Scripts\Activate.ps1

pip install --upgrade pip
pip install -r requirements.txt
```

 Usage
Run the demo on a single image and inspect the generated `output.jpg`.

```bash
python inference.py --image sample_images/test1.jpg
```

Expected behavior:
- The script prints an estimated crowd count (relative, approximate).
- The script saves an annotated image called `output.jpg` in the working directory.

 Notes for instructors
- This repository intentionally uses a simple algorithm so it is runnable on CPU-only machines.
- To evaluate state-of-the-art performance, replace the estimation function with a pre-trained model (e.g., CSRNet). I can provide a tested CSRNet example and instructions for GPU-based training if required.

 License
This example is provided under the MIT License. See `LICENSE` for details.



This repository contains a minimal, reproducible demonstration of a crowd-density estimation workflow. The implementation is intentionally lightweight and CPU-friendly: it estimates relative crowd density from a single image using simple, explainable image statistics. The purpose of this demo is educational — to provide a runnable example that can be evaluated by an instructor and extended later with state-of-the-art models (e.g., CSRNet, MCNN, P2PNet).

