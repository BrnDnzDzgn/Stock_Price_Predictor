import os
import kagglehub
from kagglehub import KaggleDatasetAdapter

os.makedirs("dataset", exist_ok=True)

# Set the path to the file(s) you'd like to load
file_paths = [
    "stocks/NVDA.csv", 
    "stocks/AAPL.csv",
    "stocks/MSFT.csv",
    "stocks/GOOGL.csv",
    "stocks/AMZN.csv",
    "stocks/TSLA.csv", 
    "stocks/AMD.csv",
    "stocks/INTC.csv",
    "stocks/QCOM.csv",
    "stocks/IBM.csv",
    "stocks/ORCL.csv",
    "stocks/CRM.csv",
    "stocks/ADBE.csv",
    "stocks/NOW.csv",
    "stocks/UBER.csv",
    "stocks/HPQ.csv",
    "stocks/EA.csv",
    "stocks/CSCO.csv",
    "stocks/NET.csv",
    "stocks/ADI.csv",
]


for file_path in file_paths:
  # Load the latest version
  df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "jacksoncrow/stock-market-dataset",
    file_path,

    # documenation for more information:
    # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
  )
  filename = file_path.split("/")[-1]   # e.g. TECH.csv
  df.to_csv(f"dataset/{filename}", index=False)


print("Saved to dataset.")