# 🚀 GAS API BR

![Flask](https://img.shields.io/badge/Flask-black?style=for-the-badge&logo=flask)
![Status](https://img.shields.io/badge/Status-Completed-green?style=for-the-badge)

## 📝 Description
A application that consumes CSV files with gas data and manages a
RESTful API built with Python and Flask, that feeds a data
analytics dashboard.

## 🚀 Technologies Used
- **Language:** Python 3.11
- **Framework:** Flask
- **Environment Management:** Venv
- **API Testing:** Postman

## 🏁 How to Run The Project Locally

Follow the steps below to run the project on your local machine.

### Prerequisites
- Python 3.9+ installed
- Git installed

### Step-by-Step
1. **Clone the repository:**
   ```bash
   git clone https://github.com/GuilhermeDorea/BrasilGasAPI.git

2. **Create the virtual and download the requirements in requirements.txt**

3. Download the data from the [gov site](https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/serie-historica-de-precos-de-combustiveis)
or use some of the exemples in data folder.

4. Change CSV_FILE for the desired file and run get_csv_data.py

5. Run api_manager.py in one terminal

6. Run dashboard.py in another terminal, paralel to api_manager.py, then
a Streamlit site will open in your main browser, ready for use.