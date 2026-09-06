# Screenshot Arranger (DOCX & PDF Generator)

A clean tool that compiles screenshots into formatted **Word (`.docx`)** and **PDF (`.pdf`)** documents via both an interactive drag-and-drop web UI and an automated Python CLI.

---

## 📁 Project Structure

```text
├── index.html           # Drag & Drop Web Page (Run in browser)
├── ss/                  # Place your screenshots here (.png, .jpg, .jpeg, etc.)
├── output/              # Generated DOCX and PDF files will appear here
├── main.py              # Main Python script
├── TEST.PY              # Quick-run wrapper
├── requirements.txt     # Python dependencies
├── pyrightconfig.json   # IDE configuration
├── .gitignore           # Git ignore rules
└── README.md            # Project documentation
```

---

## 🚀 Features

- **🌐 Interactive Drag & Drop Web App (`index.html`)**:
  - Drag and drop multiple screenshots or paste via `Cmd+V` / `Ctrl+V`.
  - Reorder, preview, remove, and rename screenshots on the fly.
  - One-click instant PDF and DOCX downloads directly in the browser (zero server required).
- **🐍 Python CLI Script (`main.py`)**:
  - Automatically arranges screenshots based on creation / modification timestamps.
  - Proportional image scaling to fit standard page bounds without distortion.
  - Generates both DOCX and PDF into `output/` folder.

---

## 🛠️ Usage Options

### Option 1: Web Interface (No terminal needed)
Double-click [`index.html`](index.html) to open it in your browser, drag and drop your screenshots, and click **Download PDF** or **Download DOCX**.

---

### Option 2: Python Script

1. **Install dependencies (first time only):**
   ```bash
   pip install -r requirements.txt
   ```

2. **Paste your screenshots** into the [`ss/`](ss/) folder.

3. **Run the script:**
   ```bash
   python main.py
   ```

4. **Retrieve your documents** from the [`output/`](output/) folder:
   - `output/arranged_screenshots.docx`
   - `output/arranged_screenshots.pdf`
