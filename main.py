import subprocess
import sys

def run_holehe(email):
    print(f"🔍 Checking email: {email}")
    subprocess.run(["holehe", email])

def run_maigret(username):
    print(f"🔍 Checking username: {username}")
    subprocess.run(["maigret", username, "--print-found"])

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python main.py --email test@gmail.com | --username john")
        sys.exit(1)

    option = sys.argv[1]
    value = sys.argv[2]

    if option == "--email":
        run_holehe(value)
    elif option == "--username":
        run_maigret(value)
    else:
        print("❌ Invalid option. Use --email or --username.")
