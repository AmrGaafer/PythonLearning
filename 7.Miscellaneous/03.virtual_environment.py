# --------------------------------------------------------------------------------------------------
# Virtual Environment:  Isolated environment that holds the pre-required packages for the project
#   Conventions:
#       the folder holding the virtual environments is called '.venv' or 'venv'
#       inside this folder create a folder for each virtual environment (eg. venv_name),
#       no other project files have to be inside that folder
#   
#   Creation:
#       Syntax: [in terminal] python3 -m venv venv_name         creates folder venv_name holding virtual environment
#       Syntax: [in terminal] adding '--system-site-packages'   creates folder venv_name holding virtual environment
#           Dirctory: venv_name\venv_name\Lib\site-packages     holds packages and setup tool of virtual environment
#           Dirctory: venv_name\venv_name\Scripts               holds opertating files [Windows]
#                     venv_name/venv_name/bin                   holds opertating files [Linux]
#
#   Activation:
#       Syntax: [in terminal] .\venv_name\Scripts\activate      [Windows]
#                             source venv_name/bin/activate     [Linux]
#   Browse packages:
#       Syntax: [in terminal] pip list          browses modules inside virtual environment after activation 
#                             pip list --local  browses modules inside virtual environment after activation
#                                               and locally installed      
#
#   Deactivation:
#       Syntax: [in terminal] deactivate
#
#   Delete:
#       Syntax: [in terminal] sudo rm -rf venv_name             'sudo' is optional
#
#   NOTE:       [in terminal] which python: shows which python is running currently
#
#   Run file with python from virtual environment:
#       Syntax: [in terminal] venv_name\Scripts\python.exe [file to be run]
#
#   Save virtual environment for future use:
#       Syntax: [in terminal] pip freeze > requirements.txt             prints installed requirements
#       Syntax: [in terminal] pip freeze --local > requirements.txt     prints only locally installed requirements
#   Install pre-saved requirements.txt:
#       Syntax: [in terminal] pip install -r requirements.txt
# --------------------------------------------------------------------------------------------------
