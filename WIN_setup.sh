# Create a virtual environment
python -m venv psych_classification_venv

# Activate the virtual environment
source ./psych_classification_venv/Scripts/activate

# Install requirements
python -m pip install --upgrade pip
python -m pip install -r ./requirements.txt

# deactivate
deactivate

#rm -rf psych_classification