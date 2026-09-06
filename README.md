# SnapStitch

A tool to sequence and compile screenshots and image assets into clean Microsoft Word (`.docx`) and PDF (`.pdf`) documents.

---

## The Problem

When preparing lab submissions, assignments, project documentation, or technical reports, you often capture dozens of screenshots or download reference diagrams that need to be organized in a specific order.

Doing this manually is frustrating and tedious:
- You have to insert images one by one into a document editor.
- You waste time resizing each screenshot so it does not overflow margins or get distorted.
- Keeping images in their correct sequential order requires constant readjustment.
- You have to repeat export steps to produce both editable Word files and submission-ready PDFs.

---

## The Solution

SnapStitch automates the entire process:
- **Instant Ingestion**: Drag and drop any number of screenshots into the web interface, paste them from the clipboard (`Cmd+V` / `Ctrl+V`), or place them directly into the `ss/` folder.
- **Automatic Sequence**: Images are arranged chronologically or in your custom defined order.
- **Smart Formatting**: Image dimensions and aspect ratios are calculated automatically to fit page bounds without manual resizing.
- **Dual Export**: Compiles both `.docx` and `.pdf` files simultaneously, saving them to the `output/` directory and providing instant on-screen download buttons.

---

## Workflow Architecture

```mermaid
flowchart LR
    subgraph Ingestion["1. Image Ingestion"]
        A["Screenshots & Diagrams"] --> B["Drag-and-Drop / Paste (SnapStitch Web UI)"]
        A --> C["Direct Placement (ss/ directory)"]
    end

    subgraph Processing["2. Processing Engine"]
        B --> D["Sequence & Order Management"]
        C --> D
        D --> E["Aspect Ratio & Margin Computation"]
    end

    subgraph Generation["3. Compilation & Output"]
        E --> F["DOCX Document Generator"]
        E --> G["PDF Document Generator"]
        F --> H["output/arranged_screenshots.docx"]
        G --> I["output/arranged_screenshots.pdf"]
        H --> J["On-Screen Download & Local Storage"]
        I --> J
    end
```

---

## Key Features

- **Automated Chronological Sequencing**: Automatically orders images based on creation or modification timestamps, with manual reordering capabilities in the web interface.
- **Dynamic Dimension Scaling**: Automatically computes proportions to ensure all images fit cleanly within standard page boundaries (Letter / A4) without cropping or distortion.
- **Dual Format Compilation**: Compiles both Microsoft Word (`.docx`) and PDF (`.pdf`) formats in a single pass.
- **Clean Output**: Generated documents are clean and unwatermarked for official academic and professional submissions.
- **Flexible Execution**: Operates via a clean web interface or direct command-line interface (CLI).
- **Automated Directory Persistence**: Images submitted through the web interface are automatically persisted in the `ss/` directory, while compiled documents are written directly to `output/`.

---

## Project Structure

```text
├── index.html           # SnapStitch web application
├── server.py            # Local HTTP service and API handler
├── main.py              # Core compilation engine and CLI entry point
├── TEST.PY              # Backward-compatible execution wrapper
├── requirements.txt     # Project dependencies
├── pyrightconfig.json   # Static analysis configuration
├── .gitignore           # Git ignore definitions
├── logo.png             # SnapStitch brand logo
├── favicon.png          # Favicon icon
├── USAGE.md             # Detailed operational user guide
├── ss/                  # Input directory for raw screenshot files
└── output/              # Target directory for generated DOCX and PDF files
```

---

## Getting Started & Usage

For full step-by-step setup instructions, pulling the repository, web interface guides, command-line operations, and workspace management, please refer to the detailed [**USAGE.md**](USAGE.md) guide.

---

## Technical Specifications

| Component | Implementation |
| :--- | :--- |
| Backend Server | Python standard library (`http.server`) |
| DOCX Engine | `python-docx` |
| PDF Engine | `reportlab` |
| Image Processing | `Pillow` (PIL) |
| Frontend | Vanilla JavaScript, HTML5, CSS3 (No external framework dependencies) |
| Supported Image Formats | PNG, JPEG, JPG, WEBP, BMP, TIFF, GIF |

---

## Author

**Prathamesh More**