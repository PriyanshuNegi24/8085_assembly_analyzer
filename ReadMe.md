# 8085 Assembly Analyzer

A tool for analyzing and processing 8085 assembly language code. This project leverages ANTLR for parsing and Python for analysis, making it easy to inspect, validate, and visualize 8085 assembly programs.

## Features
- Parses 8085 assembly code using ANTLR grammar
- Provides analysis and validation of assembly instructions
- Sample input and output files for demonstration
- Modular and extensible codebase

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd 8085_assembly_analyzer
   ```
2. **Set up Python environment:**
   - (Optional) Create a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - If using the provided `pbl` environment, activate it:
     ```bash
     pbl/bin/activate  # Or use Activate.ps1 on Windows
     ```
3. **Install Node.js dependencies:**
   ```bash
   npm install
   ```
4. **Ensure Java is installed** (required for ANTLR):
   - Download and install Java from [here](https://www.java.com/).

## Usage

- To analyze a sample assembly file:
  ```bash
  python src/8085_assembly_analyzer/src/main/analyze.py samples/sample.asm
  ```
- Or use the provided batch scripts:
  ```bash
  src/8085_assembly_analyzer/build.bat
  src/8085_assembly_analyzer/run.bat
  ```
- To start the web interface :
  ```bash
  npm run start
  ```
- Output and analysis results will be displayed in the terminal or written to output files as configured.

## Project Structure

```
8085_assembly_analyzer/
├── analyze.spec
├── build.bat
├── demo.js
├── forge.config.js
├── lib/
│   └── antlr-4.9.2-complete.jar
├── pbl/                # Python virtual environment (optional)
├── samples/
│   └── sample.asm      # Example 8085 assembly file
├── src/
│   └── 8085_assembly_analyzer/
│       ├── build.bat
│       ├── lib/
│       │   └── antlr-4.9.2-complete.jar
│       ├── ReadMe.md
│       ├── run.bat
│       ├── samples/
│       │   └── sample.asm
│       └── src/
│           └── main/
│               ├── analyze.py
│               ├── antlr4/
│               │   ├── antlr-4.13.1-complete.jar
│               │   └── Assembly8085.g4
│               ├── generated/
│               └── input.asm
└── ...
```

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements, bug fixes, or new features.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
