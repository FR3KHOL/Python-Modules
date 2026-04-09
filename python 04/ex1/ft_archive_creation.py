def create_archive() -> None:
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")

    filename = "new_discovery.txt"
    print(f"Initializing new storage unit: {filename}")

    file = open(filename, "w")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee"
    ]

    for entry in entries:
        file.write(f"{entry}\n")
        print(entry)
    file.close()

    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


if __name__ == "__main__":
    create_archive()
