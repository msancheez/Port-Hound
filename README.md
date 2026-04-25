# PORT-HOUND
TCP PORT SCANNER

**Port-Hound** is a lightweight network auditing tool, Python based. It uses concurrent programming to scan thousands of ports in seconds.

## Features

- 🚀 **Concurrent Scanning:** Utilizes a thread pool to maximize performance.
- 🛠️ **Command-Line Interface (CLI):** Professional usage via arguments (`argparse`).
- 🔢 **Flexible Range:** Allows defining the target, max port, and number of concurrent threads.
- 🛑 **Graceful Interruption:** Clean shutdown handling via `Ctrl+C`.

## Structure 📂

```text
.
├── main.py              # Application entry point
├── pyproject.toml       # Installation and custom command configuration
├── scanner/             # Core scanner package
│   ├── cli.py           # Terminal interface and argument parsing
│   └── core.py          # Socket logic and thread pool execution
└── .gitignore           # Ignored files for Git
```

## Instalation & Usage

### Prerequisites
- Python 3.10 or higher

### Instalation
```
git clone [https://github.com/msancheez/Port-Hound.git](https://github.com/msancheez/Port-Hound.git)
cd porthound
pip install -e .
```

### Usage Examples

#### Basic scan (Ports 1-1024)
porthound -t 127.0.0.1

#### Custom scan (Ports 1-8080 with 200 threads)
porthound -t 192.168.1.1 -p 8080 -w 200

#### Show help menu
porthound --help

## Created by msancheez
