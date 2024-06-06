#iteradores especiais
# yield - pausa a execução do gerador e retorna na proxima chamada
# não armazenam todos os valores na memória # uma vez que o item gerado é consumido, não pode ser acessado novamente
import requests
def fetch_products(api_url, max_pages = 100):
    page = 1
    while page <= max_pages:
        response = requests.get(f"{api_url}?page={page}")
        data = response.json()
        for product in data['products']:
            yield product
        if 'next_page' not in data:
            break
        
        page += 1
        
for product in fetch_products("http://api.example.com/products"):
    print(product)