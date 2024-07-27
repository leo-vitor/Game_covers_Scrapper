from steamgrid import SteamGridDB, MimeType, ImageType
import os
import requests

# Caminhos das pastas
roms_folder = "Pasta contendo suas roms"
covers_folder = "Pasta onde as imagens ficarão"

# Inicializa SteamGridDB com a chave de API
api_key = "sua chave api da steamgriddb"
sgdb = SteamGridDB(api_key)


# Função para buscar a capa do jogo no SteamGridDB
def search_game_cover(game_name):
    try:
        print(f"Pesquisando jogo: {game_name}")
        result = sgdb.search_game(game_name)
        if not result:
            return None
        return result[0].id
    except Exception as e:
        print(f"Erro ao buscar jogo {game_name}: {e}")
        return None


# Função para baixar a capa do jogo
def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        if response.status_code == 200:
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(1024):
                    file.write(chunk)
        else:
            print(f"Falha ao baixar a imagem de {url}")
    except Exception as e:
        print(f"Erro ao baixar a imagem de {url}: {e}")


def get_cover_url(game_id):
    try:
        grids = sgdb.get_grids_by_gameid([game_id])
        if not grids:
            print(f"Nenhuma capa encontrada para o game ID {game_id}")
            return None
        return grids[0].url
    except Exception as e:
        print(f"Erro ao obter URL da capa para game ID {game_id}: {e}")
        return None


def main():
    # Certifique-se de que a pasta de capas existe
    if not os.path.exists(covers_folder):
        os.makedirs(covers_folder)

    # Percorre todos os arquivos na pasta de ROMs
    for rom_file in os.listdir(roms_folder):
        rom_name, rom_ext = os.path.splitext(rom_file)

        # Procura a capa do jogo
        game_id = search_game_cover(rom_name)

        if game_id:
            cover_url = get_cover_url(game_id)
            if cover_url:
                cover_path = os.path.join(covers_folder, f"{rom_name}.png")
                download_image(cover_url, cover_path)
                print(f"Capa baixada para: {rom_name}")
            else:
                print(f"Não foi possível encontrar uma capa para o jogo {rom_name}")
        else:
            print(f"Não foi possível encontrar uma capa para o jogo {rom_name}")

    print("Processo concluído.")


if __name__ == "__main__":
    main()
