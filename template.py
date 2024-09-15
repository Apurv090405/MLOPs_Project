import os
from pathlib import Path

# Lists of files
list_of_files=[
    "./github/workflows/.gitkeep",
    "src/__init__.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_trainer.py",
    "src/components/model_evaluation.py",
    "src/pipeline/__init__.py",
    "src/pipeline/traning_pipeline.py",
    "src/pipeline/prediction_pipeline.py",
    "src/utils/__init__.py",
    "src/utils/utils.py",
    "src/logger/logging.py",
    "src/exception/exception",
    "testes/units/__init__.py",
    "testes/integration/__init__.py",
    "init_setup.sh",
    "requirementts.txt",
    "requirementts_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "experiment/experiments.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        #logging.info(f"Create the dir: {filedir} for file name: {filename} and the path is {filepath}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass # create an empty file


# .github/workflow folder --> for CI/CD
# experiments folder --> for small experimets inside one .ipynb file so samll experiments run in ipynb file
# src folder --> entire source code
# src/components folder --> 
# Machine learning: 2 types Supervised and unsupervised learning we have follow 2 pipeline 1. Model_traning pipeline and 2. validation pipline

# src/exception --> for exception handling
# src/logger --> for logging 
# src/pipeline --> manage all the pipeline
# src/testes/integration --> intergration releted testing
# src/testes/unit --> unit testing

# init_setup.sh --> all the setup initialized here
# pyproject.toml --> toml file
# setup.cfg --> configration file
# setup.py -->
# tox.ini --> tox file for test all the project in local dev. enviroment