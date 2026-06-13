from langchain_core.tools import tool
import os
import pandas as pd

UPLOAD_DIR = "uploads"


def load_dataframe(filename: str) -> pd.DataFrame:
    """Load dataframe from uploaded file."""

    file_path = os.path.join(UPLOAD_DIR, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"File {filename} not found in {UPLOAD_DIR}"
        )

    if filename.endswith(".csv"):
        return pd.read_csv(file_path)

    elif filename.endswith((".xlsx", ".xls")):
        return pd.read_excel(file_path)

    raise ValueError(
        "File must end with .csv, .xlsx, or .xls"
    )


@tool
def create_basic_details(filename: str) -> dict:
    """
    Analyze an uploaded CSV or Excel dataset and return
    rows, columns, column names, data types,
    missing values, duplicate rows, and sample rows.
    """

    df = load_dataframe(filename)

    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "column_names": df.columns.tolist(),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
        "duplicate_rows": int(df.duplicated().sum()),
        "sample_rows": df.head(10).to_dict(orient="records")
    }