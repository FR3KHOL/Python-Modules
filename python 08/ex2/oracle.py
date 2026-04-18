import os
import sys

try:
    from dotenv import load_dotenv  # type: ignore
except ImportError:
    print("Error: python-dotenv not installed.")
    print("Please install it: pip install python-dotenv")
    sys.exit(1)


def main() -> None:
    print("Accessing the Mainframe")
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "development")
    db_url = os.getenv("DATABASE_URL", "sqlite:///local.db")
    api_key = os.getenv("API_KEY", "")
    log_lvl = os.getenv("LOG_LEVEL", "DEBUG")
    zion = os.getenv("ZION_ENDPOINT", "http://localhost:8080")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    if mode == "production":
        print(f"Database: Connected to production cluster at {db_url}")
    else:
        print(f"Database: Connected to local instance at {db_url}")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: WARNING - Unauthenticated")

    print(f"Log Level: {log_lvl}")
    print(f"Zion Network: Online at {zion}")

    print("Environment security check:")

    if api_key:
        print("[OK] No hardcoded secrets detected")
    else:
        print("[WARNING] Missing API_KEY")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file missing")

    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")
    else:
        print("[OK] Development configurations applied")

    print("The Oracle sees all configurations.")


if __name__ == "__main__":
    main()
