import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

data_dir = BASE_DIR

# Find all Excel files in TESLA folder
excel_files = list(data_dir.glob("*.xlsx"))

if not excel_files:
    raise FileNotFoundError(f"No .xlsx files found in {data_dir}")

# Read and combine
dfs = []
for file in excel_files:
    df = pd.read_excel(file)
    df["source_file"] = file.name
    dfs.append(df)

# Combine
combined_df = pd.concat(dfs, ignore_index=True)

# Save output in TESLA folder
output_path = data_dir / "combined_tesla.xlsx"
combined_df.to_excel(output_path, index=False)

print(f"Combined {len(excel_files)} files → {output_path}")
