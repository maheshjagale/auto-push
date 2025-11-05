import subprocess
import sys
import os

def validate_terraform_file(file_path):
    """Validates a single Terraform file for syntax errors."""
    try:
        result = subprocess.run(
            ["terraform", "validate", "-no-color"],
            cwd=os.path.dirname(file_path),
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ {file_path}: Validation successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {file_path}: Validation failed!")
        print(e.stderr)
        return False

def validate_terraform_module(module_dir):
    """Validates a Terraform module by running `terraform validate` in its directory."""
    try:
        result = subprocess.run(
            ["terraform", "validate", "-no-color"],
            cwd=module_dir,
            capture_output=True,
            text=True,
            check=True
        )
        print(f"✅ Module {module_dir}: Validation successful!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Module {module_dir}: Validation failed!")
        print(e.stderr)
        return False

def find_terraform_files_and_modules(directory):
    """Finds all .tf files and modules in the specified directory."""
    tf_files = []
    modules = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".tf"):
                tf_files.append(os.path.join(root, file))
        if "main.tf" in files or "variables.tf" in files or "outputs.tf" in files:
            modules.append(root)

    return tf_files, modules

def validate_all(directory):
    """Validates all Terraform files and modules in the specified directory."""
    tf_files, modules = find_terraform_files_and_modules(directory)

    all_valid = True

    # Validate individual files
    for file in tf_files:
        if not validate_terraform_file(file):
            all_valid = False

    # Validate modules
    for module in modules:
        if not validate_terraform_module(module):
            all_valid = False

    return all_valid

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_terraform.py <terraform_directory>")
        sys.exit(1)

    terraform_dir = sys.argv[1]
    success = validate_all(terraform_dir)
    sys.exit(0 if success else 1)

