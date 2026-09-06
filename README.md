# SnapStitch

> **Navigation**: [**Overview (README.md)**](README.md) &nbsp;•&nbsp; [**User Guide & Setup (USAGE.md)**](USAGE.md)

A tool to sequence, arrange, and compile bulk screenshots into clean Microsoft Word (`.docx`) and PDF (`.pdf`) documents.

---

## Why SnapStitch?

When working on lab records, assignments, code walkthroughs, or project documentation, you often capture dozens of screenshots. Putting them into a final document by hand is slow and repetitive:
- Inserting images one by one into a word processor takes time.
- Images need manual resizing so they do not break page margins or look distorted.
- Keeping screenshots in the exact order you took them requires constant checking.
- Producing both an editable Word file and a final PDF requires repeating export steps.

SnapStitch handles all of this automatically.

---

## Smart Auto-Ordering

SnapStitch automatically arranges your screenshots in the exact sequence you need:

1. **Chronological Time Order (Earliest to Latest)**:
   - When you drop screenshots or add them from your system, SnapStitch reads each file's creation timestamp.
   - Your images are automatically sorted from the very first screenshot you took to the last one, preserving your exact chronological workflow without manual effort.

2. **Custom File Name Sorting**:
   - If you prefer naming your files (such as `01_setup.png`, `02_config.png`, `step_A.png`), SnapStitch can instantly sort them in alphabetical order (A to Z or Z to A) with a single click.

3. **Instant Manual Reordering**:
   - Fine-tune your document order at any time using simple Move Up and Move Down controls or reverse the entire list in one click.

---

## Core Capabilities

- **Instant Ingestion**: Drag and drop batches of images, paste directly from your clipboard (`Cmd+V` / `Ctrl+V`), or place files inside the local `ss/` folder.
- **Automatic Proportion Scaling**: Every screenshot is automatically scaled to fit standard page dimensions (Letter or A4) with balanced margins, preventing image distortion or page overflow.
- **Dual Format Output**: Compiles both Microsoft Word (`.docx`) and PDF (`.pdf`) files in a single pass.
- **Clean Documents (No Watermarks)**: Output files are completely clean and unbranded, suitable for academic and professional submissions.
- **Numbered Captions**: Optional automatic captions display the sequential number and file name above each image.
- **Workspace Reset**: Clear your workspace with one click after downloading so old screenshots never mix into your next project.

---

## Workflow Overview

```mermaid
flowchart LR
    subgraph Step1["1. Capture & Add"]
        A["Take Screenshots"] --> B["Paste (Cmd+V) / Drag & Drop"]
        A --> C["Drop into ss/ folder"]
    end

    subgraph Step2["2. Smart Ordering"]
        B --> D["Auto-sorted Chronologically (First to Last)"]
        C --> D
        D --> E["Optional: Sort by Name or Reorder"]
    end

    subgraph Step3["3. Automatic Formatting"]
        E --> F["Proportions & Page Margins Scaled"]
    end

    subgraph Step4["4. Dual Export"]
        F --> G["output/arranged_screenshots.docx"]
        F --> H["output/arranged_screenshots.pdf"]
        G --> I["Instant Download & Local Files"]
        H --> I
    end
```

---

## Project Structure

```text
├── index.html           # SnapStitch web application interface
├── server.py            # Local HTTP server and generation API
├── main.py              # Compilation engine and CLI entry point
├── TEST.PY              # Backward-compatible execution script
├── requirements.txt     # Python dependencies
├── pyrightconfig.json   # Configuration for type analysis
├── .gitignore           # Git ignore rules
├── logo.png             # SnapStitch header logo
├── favicon.png          # Browser favicon asset
├── favicon.ico          # Multi-resolution icon file
├── USAGE.md             # Complete step-by-step setup and operational guide
├── ss/                  # Local folder for input screenshots
└── output/              # Local folder for generated DOCX and PDF documents
```

---

## Getting Started & Setup

For complete step-by-step setup instructions, cloning the repository, running the web service, command-line operations, and resetting your workspace, please refer to the [**USAGE.md**](USAGE.md) guide.

---

## Technical Specifications

| Component | Implementation |
| :--- | :--- |
| Backend Server | Python standard library (`http.server`) |
| DOCX Engine | `python-docx` |
| PDF Engine | `reportlab` |
| Image Processing | `Pillow` (PIL) |
| Web Interface | Vanilla JavaScript, HTML5, CSS3 (Zero external web framework dependencies) |
| Supported Formats | PNG, JPG, JPEG, WEBP, BMP, TIFF, GIF |

---

## Author

**Prathamesh More**