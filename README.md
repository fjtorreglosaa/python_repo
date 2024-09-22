# How to create a Virtual Environment?
python -m venv venv

# How to activate a Virtual Enviroment?
For Windows: env\Scripts\activate
For Unix or MacOS: source venv/bin/activate

# How to deactivate a Virtual Environment?
deactivate

# How to install the packages for this project:
pip install -r requirements.txt

# How to run our FastAPI?
uvicorn main:app --reload