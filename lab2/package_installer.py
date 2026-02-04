import sys
import subprocess
import os
import platform

# -------------------------------
# Configuration: packages to install
# -------------------------------
REQUIRED_PACKAGES = [
    "numpy",
    "pandas",
    "matplotlib",
    "scikit-learn",
    "seaborn",
    "streamlit",
    "ipykernel"
]

# -------------------------------
# Check if virtual environment is activated
# -------------------------------
def is_venv_active():
    return (
        hasattr(sys, 'real_prefix') or
        (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix)
    )

# -------------------------------
# Show venv creation & activation instructions
# -------------------------------
def show_venv_instructions():
    os_name = platform.system()

    print("\n📌 How to create and activate a virtual environment:\n")
    print("Step 1: Create virtual environment")
    print("    python -m venv venv\n")

    print("Step 2: Activate virtual environment")

    if os_name == "Windows":
        print("    venv\\Scripts\\activate")
    else:
        print("    source venv/bin/activate")

    print("\nThen re-run this script:\n")
    print("    python install_packages.py\n")

# -------------------------------
# Check pip availability
# -------------------------------
def check_pip():
    try:
        subprocess.check_output([sys.executable, "-m", "pip", "--version"])
        return True
    except Exception:
        return False

# -------------------------------
# Install packages
# -------------------------------
def install_packages(packages):
    for package in packages:
        print(f"\nInstalling: {package}")
        try:
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", package
            ])
            print(f"✔ {package} installed successfully")
        except subprocess.CalledProcessError:
            print(f"✖ Failed to install {package}")
            sys.exit(1)

# -------------------------------
# Main execution
# -------------------------------
def main():
    print("Checking prerequisites...\n")

    if not is_venv_active():
        print("❌ Virtual environment is NOT activated.")
        show_venv_instructions()
        sys.exit(1)

    print("✔ Virtual environment is active")

    if not check_pip():
        print("❌ pip is not available")
        sys.exit(1)

    print("✔ pip is available")

    install_packages(REQUIRED_PACKAGES)

    print("\n🎉 All packages installed successfully!")

if __name__ == "__main__":
    main()