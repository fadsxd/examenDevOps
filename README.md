
### 1. Instalación de dependencias
pip install -r app/requirements.txt

### 2. Levantar el Endpoint
python app/main.py

**URL del Servicio:** http://127.0.0.1:5000/api/v1/

### 3. Ejecutar Pruebas Unitarias
python -m pytest app/tests/test_basic.py

---

##  (Terraform)

Para desplegar los recursos necesarios en AWS:

- terraform init
- terraform apply

---

##  (Ansible)

Para automatizar la configuración del servidor y el despliegue de la aplicación:

- ansible-playbook -i inventory playbook.yml

