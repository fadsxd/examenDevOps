
pip install -r app/requirements.txt
python app/main.py
Local: http://127.0.0.1:5000/api/v1/
python -m pytest tests/test_basic.py

terraform init
terraform apply
ansible-playbook -i inventory playbook.yml