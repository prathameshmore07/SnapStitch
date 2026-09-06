# Screenshot Arranger (DOCX & PDF Generator)

An ultra-minimalist tool that compiles any number of screenshots into formatted **Word (`.docx`)** and **PDF (`.pdf`)** documents.

---

## 📁 Project Structure

```text
├── index.html           # Minimalist Web Interface (Drag & Drop)
├── server.py            # Local Python Web Server
├── main.py              # Core Arranger Engine (Web & CLI modes)
├── TEST.PY              # Quick-run wrapper
├── ss/                  # Input folder (stores uploaded screenshots)
├── output/              # Output folder (stores generated DOCX & PDF)
├── requirements.txt     # Dependencies
├── pyrightconfig.json   # IDE configuration
├── .gitignore           # Clean git ignore rules
└── README.md            # Documentation
```

---

## 🚀 Key Features

- **Minimalist Web Interface**: Clean dark-mode interface with zero clutter.
- **Unlimited Screenshots**: Upload as many screenshots as you want via drag-and-drop, file selection, or clipboard paste (`⌘V` / `Ctrl+V`).
- **Real-Time Organization**: Reorder screenshots with `↑` / `↓`, preview dimensions, or delete individual items.
- **Saves to Local Folders**: Automatically saves your screenshots into [`ss/`](ss/) and generated files into [`output/`](output/).
- **On-Screen Downloads**: Direct on-screen **Download PDF** and **Download DOC (Word)** buttons.
- **CLI & Web Support**: Run via interactive browser UI or standard terminal CLI.

---

## 💻 How to Run

### 1. Web App (Recommended)

Simply start the server:

```bash
python main.py
```
*(or `./venv/bin/python main.py` / `python server.py`)*

This starts the local server at `http://localhost:5050` and automatically opens the browser page. 
- Drag & drop your screenshots.
- Click **Compile & Save Documents**.
- Download your **PDF** and **DOCX** files on screen or grab them from the [`output/`](output/) folder.

---

### 2. Terminal / CLI Mode

If you prefer placing images directly in [`ss/`](ss/) and generating files from terminal:

```bash
python main.py --cli
```
*(or `python TEST.PY`)*

Generated documents will be saved immediately to:
- `output/arranged_screenshots.docx`
- `output/arranged_screenshots.pdf`
