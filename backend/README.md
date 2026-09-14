# Chunck 2


## Setup

```bash

:: Install Python libraries

cd " backend"

:: Create isolate virtual environment 
python -m venv env    

::: Start environment
..\env\scripts\activate  

::: Install Web Server API
pip install uvicorn

::: Install API Framework
pip install fastapi

::: Install database module
pip install sqlalchemy
```



## Usage

```bash
cd "backend"

::: Start the python virtual environment
env\scripts\activate  

:::: Restart web server api
uvicorn main:app --reload

```
### Web Browser
- For checking if the API is online

`
http://127.0.0.1:8000/

`

- For testing the Counter API

`

`

### Command Line

```powershell
 Invoke-WebRequest -uri  http://127.0.0.1:8000/
```





## 2. Azure Function using the Azure portal
- Set up the function with [Function Premium](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal) or other because of the missing edition mode in the portal for Flex-Consumption Plan.
- Exclude legacy Consumption Plan since Python is unsupported

## 3. CosmosDB table using the Azure portal
See how to set up a database [Azure CosmosDB Table for Python](https://learn.microsoft.com/en-us/azure/cosmos-db/table/quickstart-python)