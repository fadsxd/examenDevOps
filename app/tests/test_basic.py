import pytest
from main import app

@pytest.fixture
def client():
    """Configura el cliente de pruebas de Flask"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_status_v1(client):
    """Verifica que el endpoint GET /api/v1 funcione correctamente"""
    response = client.get('/api/v1/')
    data = response.get_json()
    
    # Validaciones limpias de Python
    assert response.status_code == 200
    assert data['status'] == "success"
    assert data['modulo'] == 3
    assert "message" in data