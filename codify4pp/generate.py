import os
import argparse

def create_project_structure(project_name="codify_paper_codes"):
    """
    Create the project structure for the paper publication.

    Args:
        project_name: The name of the project.
    """

    base_dir = project_name
    os.makedirs(base_dir, exist_ok=True)

    dirs = [
        "data",
        "models",
        "configs",
        "scripts",
        "utils",
        "checkpoints/run1",  # Example run directory
        "experiments",
        "docs",
    ]

    for dir_name in dirs:
        os.makedirs(os.path.join(base_dir, dir_name), exist_ok=True)

    files = {
        "README.md": f"# {project_name}\n\nProject description and instructions go here.",
        "LICENSE": "MIT License\n\n(Add your license details here)",  # Example: MIT
        "requirements.txt": "# List your dependencies here, e.g.,\n# torch==1.13.1\n# torchvision==0.14.1",
        "data/prepare_data.py": "# Script to download, preprocess, and generate keypoints/masks",
        "models/hst.py": "# HandStyle Transformer model definition",
        "models/components.py": "# Common model components (Encoder, Decoder, Attention)",
        "models/losses.py": "# Custom loss functions",
        "configs/default.yaml": "# Default configuration parameters (YAML format)",
        "scripts/train.py": "# Training script",
        "scripts/evaluate.py": "# Evaluation script",
        "scripts/inference.py": "# Inference script",
        "scripts/visualize.py": "# Visualization script",
        "utils/utils.py": "# Utility functions",
        "utils/logger.py": "# Logging module",
        "utils/transforms.py": "# Data augmentation functions",
        "experiments/experiment_1.ipynb": "# Example experiment notebook",
        "docs/architecture.png": "",  # Placeholder for a diagram (you'll create this manually)

    }

    for file_path, content in files.items():
        full_path = os.path.join(base_dir, file_path)
        with open(full_path, "w") as f:
            f.write(content)

    print(f"Project structure created at: {base_dir}")
    print("Remember to:")
    print("  - Fill in the code for each file.")
    print("  - Add dependencies to requirements.txt.")
    print("  - Create a model architecture diagram (e.g., architecture.png).")
    print("  - Populate the YAML configuration file.")
    print("  -  Create the proper LICENSE file")


def main():
    parser = argparse.ArgumentParser(description="Create project structure.")
    parser.add_argument("project_name", type=str,
                        help="Name of the project directory.")
    args = parser.parse_args()

    create_project_structure(args.project_name)


if __name__ == "__main__":
    main()