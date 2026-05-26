import pandas as pd


def load_data(file_path, separator='|'):
    """
    Load insurance dataset safely.
    """

    try:
        df = pd.read_csv(file_path, sep=separator)

        print("Data loaded successfully.")
        print("Shape:", df.shape)

        return df

    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except Exception as e:
        print(f"Error loading data: {e}")