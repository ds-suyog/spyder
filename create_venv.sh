# This script creates python venv at parent location of spyder, by using requirements.txt from config.
python3.10 -m venv venv
source venv/bin/activate
pip install -r ./config/requirements.txt
deactivate
