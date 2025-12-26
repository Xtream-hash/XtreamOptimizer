import os

JUNK_EXTENSIONS = (
    ".tmp", ".log", ".cache", ".bak",
    ".old", ".temp"
)

def scan_storage(path="/storage/emulated/0"):
    junk_files = []

    for root, dirs, files in os.walk(path):
        for file in files:
            if file.lower().endswith(JUNK_EXTENSIONS):
                full_path = os.path.join(root, file)
                try:
                    size = os.path.getsize(full_path)
                    junk_files.append((full_path, size))
                except:
                    pass

    return junk_files

