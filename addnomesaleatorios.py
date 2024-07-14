import requests
import random
import names
import string
from bs4 import BeautifulSoup

# URL do endpoint de cadastro
url = "http://127.0.0.1:5000/talentos"

# Lista de cargos relacionados a desenvolvimento de software
cargos = [
    "Desenvolvedor(a) Backend",
    "Desenvolvedor(a) Frontend",
    "Desenvolvedor(a) Full Stack",
    "Engenheiro(a) de Software",
    "Analista de Sistemas",
    "Desenvolvedor(a) Mobile",
    "Engenheiro(a) de Dados",
    "Cientista de Dados",
    "DevOps",
    "Administrador(a) de Sistemas"
]

# Lista de áreas de formação
areas = ['exatas', 'humanas', 'ciencias', 'tecnologia', 'outras']

# Função para gerar um email aleatório
def generate_random_email(nome):
    return nome.lower().replace(" ", ".") + str(random.randint(1, 1000)) + "@example.com"

# Função para gerar um telefone aleatório
def generate_random_phone():
    return ''.join(random.choices(string.digits, k=10))

# Função para gerar dados de cadastro aleatórios
def generate_random_talento():
    nome = names.get_full_name()
    status_trabalho = random.choices(['empregado', 'desempregado'], weights=[0.7, 0.3], k=1)[0]
    return {
        "nome": nome,
        "idade": random.randint(20, 60),
        "profissao": random.choice(cargos) if status_trabalho == 'empregado' else '',
        "objetivos": "Objetivo exemplo",
        "status_trabalho": status_trabalho,
        "area_formacao": random.choice(areas),
        "cargo_pretendido": random.choice(cargos),  # Assuming single value for simplicity
        "cidade": "Cidade " + names.get_last_name(),
        "bairro": "Bairro " + names.get_last_name(),
        "email": generate_random_email(nome),
        "telefone": generate_random_phone(),
        "github": "https://github.com/" + nome.lower().replace(" ", ""),
        "linkedin": "https://linkedin.com/in/" + nome.lower().replace(" ", "")
    }

# Função para obter o token CSRF
def get_csrf_token(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    csrf_token = soup.find('input', {'name': 'csrf_token'})['value']
    return csrf_token

# Criar uma sessão para manter cookies
session = requests.Session()

# Loop para criar 10 cadastros aleatórios
for _ in range(10):
    talento_data = generate_random_talento()
    try:
        talento_data['csrf_token'] = get_csrf_token(session, url)  # Adiciona o token CSRF aos dados do formulário
        response = session.post(url, data=talento_data)
        if response.status_code == 200:
            print(f"Cadastro de {talento_data['nome']} realizado com sucesso!")
        else:
            print(f"Erro ao cadastrar {talento_data['nome']}: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Ocorreu um erro ao cadastrar {talento_data['nome']}: {str(e)}")
