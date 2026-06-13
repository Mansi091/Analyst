from langchain_core.tools import tool
import os
import pandas as pd

from tools.upload_tool_data import load_dataframe


CLEANED_DIR = "cleaned_data"
os.makedirs(CLEANED_DIR, exist_ok=True)


@tool
def apply_cleaning(filename: str) -> dict:
    """
    Apply automatic cleaning on a dataset:
    - Fill numeric missing values using median
    - Fill categorical missing values using mode
    - Remove duplicate rows
    - Save cleaned dataset
    """

    df = load_dataframe(filename)

    actions_applied = []

    #filling missing values
    for column in df.columns:

        if df[column].isnull().sum() == 0:
            continue

        #numerical columns
        if pd.api.types.is_numeric_dtype(df[column]):
            median_value = df[column].median()

            df[column] = df[column].fillna(median_value)

            actions_applied.append(
                f"Filled missing values in '{column}' using median ({median_value})"
            )

        #categorical columns
        else:
            mode_value = df[column].mode()

            if not mode_value.empty:
                mode_value = mode_value[0]

                df[column] = df[column].fillna(mode_value)

                actions_applied.append(
                    f"Filled missing values in '{column}' using mode ({mode_value})"
                )

    #removing duplicates
    duplicate_count = int(df.duplicated().sum())

    if duplicate_count > 0:
        df = df.drop_duplicates()

        actions_applied.append(
            f"Removed {duplicate_count} duplicate rows"
        )

    #saving cleaned dataset
    cleaned_filename = f"cleaned_{filename}"

    cleaned_path = os.path.join(
        CLEANED_DIR,
        cleaned_filename
    )

    if filename.endswith(".csv"):
        df.to_csv(cleaned_path, index=False)

    else:
        df.to_excel(cleaned_path, index=False)

    return {
        "message": "Cleaning completed successfully",
        "cleaned_filename": cleaned_filename,
        "rows_after_cleaning": int(df.shape[0]),
        "columns": int(df.shape[1]),
        "actions_applied": actions_applied
    }