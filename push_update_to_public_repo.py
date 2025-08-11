import os
import shutil
import subprocess
import sys

# CONFIGURATION
PRIVATE_REPO_PATH = "/path/to/your/private/bams-app"  # Update this
PUBLIC_REPO_PATH = "/path/to/your/public/bams-downloads"  # Update this

# Files to copy (relative to PRIVATE_REPO_PATH)
FILES_TO_COPY = [
    "dist/BAMS-1.1.0.exe",           # Windows installer (example path)
    "dist/BAMS-1.1.0.AppImage",      # Linux installer (example path)
    "latest.json"                    # Version info file
]

def copy_files():
    for rel_path in FILES_TO_COPY:
        src = os.path.join(PRIVATE_REPO_PATH, rel_path)
        dst = os.path.join(PUBLIC_REPO_PATH, os.path.basename(rel_path))
        print(f"Copying {src} -> {dst}")
        shutil.copy2(src, dst)

def git_commit_and_push():
    os.chdir(PUBLIC_REPO_PATH)
    subprocess.run(["git", "add", "."], check=True)
    commit_msg = f"Release update {', '.join(os.path.basename(f) for f in FILES_TO_COPY)}"
    subprocess.run(["git", "commit", "-m", commit_msg], check=True)
    subprocess.run(["git", "push"], check=True)
    print("Files pushed to public repo.")

if __name__ == "__main__":
    try:
        copy_files()
        git_commit_and_push()
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
