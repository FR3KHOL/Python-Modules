import importlib.util


def check_deps() -> bool:
    packages = ['pandas', 'numpy', 'matplotlib']
    missing = []
    for pkg in packages:
        if importlib.util.find_spec(pkg) is None:
            missing.append(pkg)
    if missing:
        print("Welcome to the Real World of Data Engineering")
        print(f"Missing dependencies: {', '.join(missing)}")
        print("Install via pip: pip install -r requirements.txt")
        print("Or via Poetry: poetry install")
        return False
    return True


def run_analysis() -> None:
    import pandas as pd  # type: ignore
    import numpy as np  # type: ignore
    import matplotlib  # type: ignore
    import matplotlib.pyplot as plt  # type: ignore

    print("LOADING STATUS: Loading programs...")
    print("Checking dependencies:")
    print(f"[OK] pandas ({pd.__version__})")
    print(f"[OK] numpy ({np.__version__})")
    print(f"[OK] matplotlib ({matplotlib.__version__})")
    print("Data manipulation ready")
    print("Numerical computation ready")
    print("Visualization ready")

    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    data = np.random.rand(1000)
    df = pd.DataFrame(data, columns=['Matrix Data'])

    print("Generating visualization...")
    plt.figure()
    df.plot(title="Matrix Signal Distribution")
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    if check_deps():
        run_analysis()


if __name__ == "__main__":
    main()
