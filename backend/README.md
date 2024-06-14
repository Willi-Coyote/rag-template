# About Backend

## Steps to set up python backend project using poetry:
1. Run 
```pip install poetry```
2. Direct to backend folder and run 
```poetry init```
This should create a pyproject.toml file in the backend folder.
3. Create a ```.venv``` folder
4. Run 
```poetry config virtualenvs.in-project true```
This will set the property to create the files related to virtual environment within the backend folder.
5. Run ```poetry install```. This step should create files within the ```.venv``` folder.
6. Next step is to create a new Python Interpreter in Pycharm <br/>
Go to File -> Settings -> Project -> Python Interpreter -> Add New Local Interpreter -> Poetry Environment -> Select the python.exe file in the .venv folder under Existing Environment <br/>