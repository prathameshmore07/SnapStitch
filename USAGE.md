# SnapStitch User Guide

A step-by-step operational guide for aggregating, arranging, and compiling bulk screenshots into formatted Microsoft Word (`.docx`) and PDF (`.pdf`) documents.

**Built by Prathamesh More**

---

## Table of Contents
1. [How to Pull & Setup (New Users)](#how-to-pull--setup-new-users)
2. [Quick Overview](#quick-overview)
3. [Workflow 1: Web Interface (Recommended)](#workflow-1-web-interface-recommended)
4. [Workflow 2: Command-Line Interface (CLI)](#workflow-2-command-line-interface-cli)
5. [Clearing Workspace for New Batches](#clearing-workspace-for-new-batches)
6. [Advanced Features & Shortcuts](#advanced-features--shortcuts)
7. [Folder Structure & File Storage](#folder-structure--file-storage)
8. [Troubleshooting & FAQs](#troubleshooting--faqs)

---

## How to Pull & Setup (New Users)

Follow these steps to get SnapStitch running on your machine:

### Step 1: Clone / Pull the Code
Open your terminal and run:
```bash
git clone https://github.com/prathameshmore07/SnapStitch.git
cd SnapStitch
```

*If you already cloned the repository and want the latest updates:*
```bash
git pull origin main
```

### Step 2: Create a Virtual Environment & Install Dependencies

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

---

## Quick Overview

SnapStitch eliminates the repetitive friction of manually importing, arranging, resizing, and converting screenshots for academic submissions, lab records, and technical reports.

```text
[ Capture Screenshots ] 
         │
         ▼
[ Ingest into SnapStitch ] (Web UI or ss/ folder)
         │
         ▼
[ Arrange & Configure ] (Reorder, set page size, captions)
         │
         ▼
[ One-Click Compilation ] ──► output/arranged_screenshots.docx
                          └──► output/arranged_screenshots.pdf
         │
         ▼
[ Clear Workspace ] (Reset for next assignment/task)
```

---

## Workflow 1: Web Interface (Recommended)

### Step 1: Launch the Application
In your terminal, run:
```bash
python3 main.py
```
This starts the local SnapStitch service and automatically opens `http://localhost:5050` in your web browser.

### Step 2: Ingest Screenshots
You can add screenshots using any of the following methods:
- **Drag & Drop**: Drag one or multiple image files directly onto the central drop zone.
- **File Browser**: Click anywhere inside the drop zone to open your system file picker.
- **Clipboard Paste**: Press `Cmd + V` (macOS) or `Ctrl + V` (Windows/Linux) anywhere on the page to paste screenshots copied from your clipboard or screenshot tool.

*Supported formats: PNG, JPG, JPEG, WEBP, BMP, TIFF, GIF.*

### Step 3: Organize and Configure
Once images are loaded into the **Screenshots Queue**:
- **Reorder**: Use the `↑` and `↓` buttons to arrange images in the exact sequence you want them to appear in the document.
- **Delete Single Item**: Click the `✕` button to remove any unwanted image from the queue.
- **Document Name**: Type a custom file name in the Document Name field.
- **Page Size**: Select **Letter** (Standard US) or **A4** (International standard).
- **Captions**: Check or uncheck **Numbered captions** to toggle automatic image labels (`1. filename.png`, etc.).

### Step 4: Compile Documents
Click **Compile & Save Documents**.
- The backend automatically copies and indexes your images into the local [`ss/`](ss/) folder.
- Both `.docx` and `.pdf` files are compiled and saved into the local [`output/`](output/) folder.
- Dedicated on-screen **Download PDF** and **Download DOC (Word)** buttons will appear immediately.

---

## Workflow 2: Command-Line Interface (CLI)

For headless or terminal-only workflows without opening a browser:

1. **Place your images** into the [`ss/`](ss/) directory.
2. **Run the compilation script**:
   ```bash
   python3 main.py --cli
   ```
3. **Retrieve your compiled documents** from the [`output/`](output/) directory:
   - `output/arranged_screenshots.docx`
   - `output/arranged_screenshots.pdf`

---

## Clearing Workspace for New Batches

When you finish an assignment or project and want to start a new one, old screenshots must not mix with new ones.

### In the Web Interface:
1. After downloading your files from the result card, click **Clear Workspace & Start New**.
2. A confirmation prompt will appear:
   > **Clear Workspace?**
   > *This will delete all saved screenshots from `ss/` and generated documents from `output/` so you can start your next task completely fresh.*
3. Click **Yes, Clear All**.
4. All previous screenshots in `ss/` and old documents in `output/` are deleted, and the user interface resets to a clean slate.

---

## Advanced Features & Shortcuts

| Feature | Description |
| :--- | :--- |
| `Cmd + V` / `Ctrl + V` | Paste screenshots directly into the browser without saving to disk first |
| Aspect Ratio Fitting | Automatically calculates proportions to prevent distortion and margin overflow |
| Clean Output | Output documents contain no watermarks, branding, or tool tags |
| Standalone Fallback | The web interface also operates client-side if opened directly as a static file |

---

## Folder Structure & File Storage

```text
├── ss/                  # Holds the current active batch of screenshot images
├── output/              # Contains the generated DOCX and PDF documents
├── index.html           # Minimalist web application
├── server.py            # Local backend service
├── main.py              # Application entry point (Web & CLI)
├── logo.png             # SnapStitch brand logo
├── favicon.png          # Browser favicon
├── requirements.txt     # Python dependencies
├── USAGE.md             # This guide
└── README.md            # Technical documentation
```

---

## Troubleshooting & FAQs

### Port 5050 is in use
If port 5050 is occupied by another service, `server.py` automatically rolls over to port `5051`, `5052`, etc., without crashing.

### Reinstalling Dependencies
If you move to a new machine or re-create your virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Stopping the Local Server
To shut down the background server, return to your terminal window and press:
```bash
Ctrl + C
```

---

## Author

**Prathamesh More**
