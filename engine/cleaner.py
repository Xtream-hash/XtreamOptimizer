import os

def delete_file(path):
    try:
        size = os.path.getsize(path)
        os.remove(path)
        return size
    except:
        return 0


def clear_cache():
    paths = [
        "/storage/emulated/0/Download",
        "/storage/emulated/0/Android/media"
    ]

    deleted = 0
    for p in paths:
        if os.path.exists(p):
            for root, dirs, files in os.walk(p):
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                        deleted += 1
                    except:
                        pass
    return deleted


def whatsapp_clean():
    path = "/storage/emulated/0/WhatsApp/Media/.Statuses"

    deleted = 0
    if os.path.exists(path):
        for f in os.listdir(path):
            try:
                os.remove(os.path.join(path, f))
                deleted += 1
            except:
                pass
    return deleted
