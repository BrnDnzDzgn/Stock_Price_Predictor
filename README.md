
## Create a virtual environment and kernel
1. Install Python 3.13.9 from python.org/downloads

2. Create virtual environment: `/usr/local/bin/python3.13 -m venv .stock_price`
3. Activate virtual environment: `source .stock_price/bin/activate`
4. Upgrade pip: `pip install --upgrade pip`
5. Install packages from requirements.txt: `pip install -r requirements.txt`

6. Install ipykernel: `pip install ipykernel`
7. Create Jupyter kernel: `python -m ipykernel install --user --name stock_price --display-name "AML_Stock_Price"`
8. Start Jupyter Lab: `jupyter lab`
9. In Jupyter Lab: Change kernel to "AML Tutorial (Python 3.13)"
10. For SSL issues: Set environment variable before starting Jupyter: `export PYTHONHTTPSVERIFY=0`


In this project 20 tech related stocks are investigated. These stocks are:
- Nvidia – NVDA
- Apple – AAPL
- Microsoft – MSFT
- Google – GOOGL
- Amazon – AMZN
- Tesla – TSLA
- AMD – AMD
- Intel – INTC
- Qualcomm – QCOM
- IBM – IBM
- Oracle – ORCL
- Salesforce – CRM
- Adobe – ADBE
- ServiceNow – NOW
- Uber – UBER
- HP – HPQ
- Electronic Arts – EA
- Cisco – CSCO
- Cloudflare – NET
- Analog Devices – ADI

