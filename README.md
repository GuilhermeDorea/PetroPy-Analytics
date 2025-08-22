#  PetroPy Analytics

![Last commit](https://img.shields.io/badge/Last_commit-august_2025-yellow?style=for-the-badge) ![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-blue?style=for-the-badge) ![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask) ![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas) ![Streamlit](https://img.shields.io/badge/Streamlit-black?style=for-the-badge&logo=streamlit)

## Description
An application that processes historical fuel price data from Brazil (provided by ANP) and serves it through a RESTful API built with Python and Flask. The project also includes a data analytics dashboard made with Streamlit that consumes this API to display interactive charts.

## Data problem
During a domestic trip in Brazil, I observed a significant difference in fuel prices between my home state, Bahia, and the country's economic center, São Paulo. This inspired me to analyze these variations on a national scale. The primary data source was a large CSV file from the ANP (National Petroleum Agency) containing over 500,000 rows of historical price collections. Handling this volume of data required an efficient data pipeline. The implemented architecture involved:

1. An ETL (Extract, Transform, Load) script using the Pandas library to parse the large CSV, clean the data, and load it into a structured SQLite database.

2. A RESTful API built with Python and Flask, designed for scalability and to serve the processed data from the database.

3.  data analytics dashboard developed with Streamlit, which consumes the API to provide interactive visualizations.

## Conclusions
The analysis revealed a price variation of up to R$1.30 per liter for regular gasoline between the most expensive state (Acre) and the cheapest states.
This significant variation suggests that regional factors have a greater impact on the final consumer price than the nationally-set price from the main producer (Petrobras). The primary driver of this difference is likely the state-level tax policies, particularly the ICMS (Imposto sobre Circulação de Mercadorias e Serviços), which varies from one state to another. Other contributing factors may include local distribution logistics and retail market competition.


## Technologies Used
* **Backend:** Python 3.11, Flask, Flask-SQLAlchemy
* **Data Processing:** Pandas
* **Dashboard:** Streamlit
* **Database:** SQLite
* **Environment:** Venv

## How to Run The Project Locally

Follow the steps below to run the project on your local machine.

### Prerequisites
- Python 3.9+
- Git 

### Step-by-Step
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/GuilhermeDorea/BrasilGasAPI.git](https://github.com/GuilhermeDorea/BrasilGasAPI.git)
    cd BrasilGasAPI
    ```

2.  **Create and activate the virtual environment:**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate on Windows
    .\venv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Prepare the data:**
    * Download the historical data from the official [ANP website](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis).
    * Place the desired CSV file inside the `/data` folder.
    * Open the `get_csv_data.py` file and update the `CSV_FILE_PATH` variable to match the name of your file.

5.  **Run the ETL script to populate the database:**
    * This script will read the CSV, process the data, and create the `database.db` file.
    ```bash
    python get_csv_data.py
    ```

6.  **Run the Flask API server:**
    * Open a **new terminal**.
    * Activate the virtual environment again (`.\venv\Scripts\activate`).
    * Start the API:
    ```bash
    flask run
    ```
    * The API will be running at `http://127.0.0.1:5000`. Leave this terminal open.

7.  **Run the Streamlit Dashboard:**
    * Open a **third terminal** (or use the one from step 5).
    * Activate the virtual environment (`.\venv\Scripts\activate`).
    * Start the dashboard:
    ```bash
    streamlit run dashboard.py
    ```
    * A new tab will open in your browser with the dashboard, ready to use.