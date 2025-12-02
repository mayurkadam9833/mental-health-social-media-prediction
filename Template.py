import os 
import logging 
from pathlib import Path 

# logging config for folder structure creation 
logging.basicConfig(level=logging.INFO,format="[%(asctime)s : %(message)s]")

# project name
project_name="mental_health_prediction" 

# list files and directories required for project 
list_of_files=[
    f"src/{project_name}/__init__.py", 
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py", 
    f"src/{project_name}/utils/common.py", 
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py", 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/config_entity.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml", 
    "schema.yaml", 
    "main.py", 
    "app.py",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

# loop through list of files list to create project folder structure
for file_path in list_of_files: 
    file_path=Path(file_path)                         # define file path
    file_dir,file_name=os.path.split(file_path)       # split file path and file

    # create directory if not exists
    if file_dir != "": 
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"create {file_dir}")
    
    # create file if not exists
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0): 
        with open(file_path,"w")as file: 
            pass 
            logging.info(f"create empty {file_name} at {file_path}")
    
    # if file is already exists 
    else: 
        logging.info(f"{file_name} is already exists")
