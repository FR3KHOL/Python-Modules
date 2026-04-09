def recover_ancient_data() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")

    filename = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {filename}")

    try:
        file = open(filename, 'r')
        print("Connection established...")
        print()
        print("RECOVERED DATA:")

        data = file.read()
        print(data)
        print()
        file.close()
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


if __name__ == "__main__":
    recover_ancient_data()
