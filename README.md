# Screenshot Arranger (DOCX & PDF Generator)

A clean and automated Python tool that scans screenshots from a dedicated input folder, orders them chronologically, and compiles them into formatted **Word (`.docx`)** and **PDF (`.pdf`)** documents.

---

## 📁 Project Structure

```text
├── ss/                  # Place your screenshots here (.png, .jpg, .jpeg, etc.)
├── output/              # Generated DOCX and PDF files will appear here
├── main.py              # Main application script
├── TEST.PY              # Quick-run wrapper
├── requirements.txt     # Python dependencies
├── pyrightconfig.json   # IDE configuration
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

---

## 🚀 Features

- **Chronological Sorting**: Automatically arranges screenshots based on creation / modification timestamps.
- **Aspect Ratio Preservation**: Dynamically scales images to fit standard letter page bounds without distortion or overflowing margins.
- **Dual Output**: Generates both Microsoft Word (`.docx`) and standalone PDF (`.pdf`) documents in one go.
- **Broad Image Support**: Supports PNG, JPG/JPEG, WEBP, BMP, TIFF, and GIF.

---

## 🛠️ Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 💻 Usage

1. **Paste your screenshots** into the [`ss/`](ss/) folder.
2. **Run the script:**
   ```bash
   python main.py
   ```
3. **Retrieve your documents** from the [`output/`](output/) folder:
   - `output/arranged_screenshots.docx`
   - `output/arranged_screenshots.pdf`
