# Chunck 2


## Setup

```bash

:: Install Python libraries

cd " backend"

:: Create environment
python -m venv env    

::: Start environment
..\env\scripts\activate  

::: Install Web server
pip install uvicorn

::: Install API
pip install fastapi

::: Install database bridge
pip install sqlalchemy

:::: Restart web server
uvicorn src.main:app --reload
```

## 2. Azure Function using the Azure portal
- Set up the function with [Function Premium](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-function-app-portal) or other because of the missing edition mode in the portal for Flex-Consumption Plan.
- Exclude legacy Consumption Plan since Python is unsupported

## 3. CosmosDB table using the Azure portal
See how to set up a database [Azure CosmosDB Table for Python](https://learn.microsoft.com/en-us/azure/cosmos-db/table/quickstart-python)