1. Create a Virtual Environment
python -m venv .venv

This creates a virtual environment folder named .venv.

2. Activate the Virtual Environment
PowerShell
.\.venv\Scripts\Activate.ps1


After activation, you'll see something like:
(.venv) PS C:\Projects\myproject>

3. Deactivate the Virtual Environment
deactivate

4. Install Packages
pip install requests
pip install pymongo
pip install flask

5. View Installed Packages
pip list
or
pip freeze

6. Save Dependencies
pip freeze > requirements.txt
pip list > requirements.txt
Example requirements.txt:
requests==2.32.5
pymongo==4.14.0

7. Install from requirements.txt
pip install -r requirements.txt

8. Upgrade a Package
pip install --upgrade requests

9. Uninstall a Package
pip uninstall requests
pip uninstall pymongo

10. Check Python Version
python --version

11. Check Pip Version
pip --version

12. Show Package Information
pip show requests
13. Remove the Virtual Environment
Deactivate first:
deactivate
Then delete the .venv folder:
Remove-Item -Recurse -Force .venv