
Copiar código
# SteamGridDB Game Covers Downloader

Este repositório contém um script Python para baixar capas de jogos usando a API do SteamGridDB.

## Requisitos

- Python 3.x
- Biblioteca `requests`
- Biblioteca `python-steamgriddb`

Você pode instalar as dependências usando pip:

```bash
pip install requests python-steamgriddb
Configuração
Obtenha uma chave de API: Você pode gerar uma chave de API no SteamGridDB.

Substitua a chave de API: No script download_covers.py, substitua YOUR_API_KEY pela sua chave de API do SteamGridDB.

Configure os caminhos das pastas:

roms_folder: Pasta onde os arquivos ROMs estão localizados.
covers_folder: Pasta onde as capas serão salvas.
python
Copiar código
roms_folder = "/caminho/para/a/pasta/roms"
covers_folder = "/caminho/para/a/pasta/capas"
Uso
Execute o script para baixar as capas dos jogos:

bash
Copiar código
python download_covers.py
O script irá:

Buscar o nome dos jogos a partir dos arquivos ROMs na pasta especificada.
Procurar e baixar as capas correspondentes do SteamGridDB.
Salvar as capas na pasta configurada.
Exemplo de Código
Aqui está um exemplo básico de como usar a API do SteamGridDB para buscar e baixar capas:

python
Copiar código
from steamgrid import SteamGridDB
import requests

api_key = "YOUR_API_KEY"
sgdb = SteamGridDB(api_key)

def search_game_cover(game_name):
    result = sgdb.search_game(game_name)
    if not result:
        return None
    return result[0].id

def download_image(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)

def get_cover_url(game_id):
    grids = sgdb.get_grids_by_gameid([game_id])
    if not grids:
        return None
    return grids[0].url
Contribuições
Sinta-se à vontade para contribuir com melhorias, relatórios de bugs ou novas funcionalidades. Envie um pull request ou abra uma issue no GitHub.

Licença
Este projeto está licenciado sob a MIT License.

Contato
Para dúvidas ou sugestões, entre em contato em seu-email@exemplo.com.

csharp
Copiar código

Você pode ajustar o conteúdo conforme necessário, especialmente a seção de contato e a licença, para refletir as informações específicas do seu projeto. Se precisar de mais ajustes, estou aqui para ajudar!
