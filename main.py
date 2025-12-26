from engine.scanner import scan_storage
from engine.cleaner import delete_file, clear_cache, whatsapp_clean
from engine.malware import malware_scan
from colorama import Fore, init
import os

init(autoreset=True)

def human_size(size):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024:
            return f"{size:.2f} {unit}"
        size /= 1024


def banner():
    print(Fore.CYAN + "\n🔥 XtreamOptimizer 🔥\n")


def menu():
    print(Fore.YELLOW + """
[1] Scan Junk Files
[2] Clear Cache
[3] Clean WhatsApp Junk
[4] Boost Performance
[5] Malware Scan
[0] Exit
""")


def boost():
    print(Fore.GREEN + "Optimizing memory...")
    os.system("pkill -f background")
    print("RAM optimized ✔")


banner()

while True:
    menu()
    choice = input("Choose option: ").strip()

    if choice == "1":
        files = scan_storage()
        if not files:
            print("No junk files found.")
        else:
            total = 0
            for i, (p, s) in enumerate(files):
                print(f"[{i}] {p} ({human_size(s)})")

            confirm = input("Delete all junk? (y/n): ").lower()
            if confirm == "y":
                for f, _ in files:
                    total += delete_file(f)
                print(f"✔ Freed {human_size(total)}")

    elif choice == "2":
        print(f"✔ Cache cleaned: {clear_cache()} files")

    elif choice == "3":
        print(f"✔ WhatsApp cleaned: {whatsapp_clean()} files")

    elif choice == "4":
        boost()

    elif choice == "5":
        print("🔍 Scanning for threats...\n")
        threats = malware_scan()

        if not threats:
            print("✅ No threats detected")
        else:
            freed = 0
            for t in threats:
                print(t)

            confirm = input("Delete all threats? (y/n): ").lower()
            if confirm == "y":
                for t in threats:
                    try:
                        freed += os.path.getsize(t)
                        os.remove(t)
                    except:
                        pass
                print(f"🛡 Freed {human_size(freed)}")

    elif choice == "0":
        print("Goodbye 👋")
        break

    else:
        print("Invalid option ❌")
