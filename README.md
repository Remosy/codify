# Codify: Your Deep Learning Project Structure Generator 📜 

[![PyPI version](https://badge.fury.io/py/codify.svg)](https://badge.fury.io/py/codify)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
Codify is a simple command-line tool that quickly generates a well-organized project structure for your deep learning projects. It helps you start your projects with a clean and consistent foundation, promoting best practices and reproducibility.

## Features 👇

*   **Fast Project Setup:**  Get started with a new project in seconds.
*   **Standard Structure:** Creates a directory structure that is commonly used in deep learning projects, making it easy to understand and navigate.
*   **Customizable:**  You provide the project name, and Codify does the rest.
*   **Easy to Use:**  Install with pip and run a single command.
*   **No Dependencies:** Codify itself has minimal dependencies, making it lightweight.
*   **Python-Based:** Written in Python and easily extensible.

## Installation 💪
```bash
pip install codify
```

## Usage
:beers: :cocktail: :tropical_drink:
To create a new project structure, simply run:

```bash
create-project <project_name>
```

Replace <project_name> with the desired name for your project.  For example:
```bash
create-project my_awesome_model
```

:page_facing_up: This will create a directory named my_awesome_model in your current working directory with the following structure

```bash
codify_project_name/  # (Your chosen project name)
├── README.md             # Project description, usage instructions, etc.
├── LICENSE               # The license for your project (e.g., MIT, Apache 2.0)
├── setup.py              # For packaging your project (if you make it a package)
├── requirements.txt      # Python dependencies (e.g., torch, torchvision, numpy)

├── data/                 # Data-related scripts and (optionally) small sample data
│   └── prepare_data.py   # Script to download, preprocess, and prepare data
│   └── ...               # Other data-related files (but NOT the full dataset)

├── models/               # Deep learning model definitions
│   ├── init.py       # Makes models a Python package
│   ├── hst.py            # Example: HandStyle Transformer model definition
│   ├── components.py     # Reusable model components (e.g., encoders, decoders)
│   ├── losses.py         # Custom loss function implementations
│   └── ...               # Other model-related files

├── configs/              # Configuration files (usually YAML)
│   └── default.yaml      # Default configuration parameters
│   └── ...               # Other configurations (e.g., for different experiments)

├── scripts/              # Scripts for training, evaluation, inference, etc.
│   ├── train.py          # Training script
│   ├── evaluate.py       # Evaluation script
│   ├── inference.py      # Inference/prediction script
│   ├── visualize.py     # Visualization script (e.g., for attention maps)
│   └── ...               # Other scripts

├── utils/                # Utility functions and helper classes
│   ├── init.py       # Makes utils a Python package
│   ├── utils.py          # General utility functions
│   ├── logger.py         # Logging setup
│   ├── transforms.py     # Data augmentation transformations
│   └── ...               # Other utility files

├── checkpoints/          # Directory to save trained model checkpoints
│   └── run1/             # Subdirectory for a specific training run
│       ├── model_best.pth # Example: Best model checkpoint
│       └── ...            # Other checkpoints from that run
│   └── ...               # Other run directories

├── experiments/          # Jupyter Notebooks or Markdown files for experiments
│   ├── experiment_1.ipynb # Example experiment notebook
│   └── ...               # Other experiment records

└── docs/                 # Project documentation
└── architecture.png # (Optional) Diagram of your model architecture
└── ...               # Other documentation files
```
