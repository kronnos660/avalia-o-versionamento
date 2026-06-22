import requests
import os


# --- FUNÇÃO DE UPLOAD ---
def fazer_upload_temporario(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        print(f"❌ Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
        return None

    print(f"📤 1. Fazendo upload da imagem '{caminho_arquivo}'...")

    url_servidor = "https://catbox.moe/user/api.php"

    try:
        with open(caminho_arquivo, 'rb') as arquivo:
            dados = {'reqtype': 'fileupload'}
            arquivos = {'fileToUpload': arquivo}
            resposta = requests.post(url_servidor, data=dados, files=arquivos)

        if resposta.status_code == 200:
            link_publico = resposta.text.strip()
            print(f"🔗 Upload concluído: {link_publico}")
            return link_publico
        else:
            print("❌ Erro no upload.")
            return None

    except Exception as e:
        print(f"❌ Erro: {e}")
        return None


# --- FUNÇÃO PRINCIPAL ---
def gerar_e_baixar_imagem():
    api_key = "91607257f4d42289951c93b809ed6472cf78eb1c66dc2dd9"
    template_id = "318d37f4f2"
    nome_arquivo_local = "S%3Fo_Paulo_2005.webp"

    # 1. Upload da imagem
    url_da_sua_imagem = fazer_upload_temporario(nome_arquivo_local)

    if not url_da_sua_imagem:
        print("❌ Upload falhou, encerrando...")
        return

    print("\n🎨 2. Enviando para o DynaPictures...")

    url_api = f"https://api.dynapictures.com/designs/{template_id}"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # ✅ AQUI ESTÁ A CORREÇÃO PRINCIPAL
    payload = {
        "format": "png",
        "params": [
            {
                "name": "Title",
                "text": "Agora a imagem vai carregar!"
            },
            {
                "name": "Logo 2",  # ⚠️ CONFIRA SE ESSE NOME ESTÁ CERTO NO TEMPLATE
                "imageUrl": url_da_sua_imagem
            }
        ]
    }

    try:
        response = requests.post(url_api, headers=headers, json=payload)
        response.raise_for_status()

        dados = response.json()
        imagem_url_final = dados.get('imageUrl')

        if not imagem_url_final:
            print("❌ API não retornou imagem.")
            print(dados)
            return

        print(f"🖼️ Imagem gerada: {imagem_url_final}")

        # 3. Download da imagem final
        print("\n⬇️ 3. Baixando imagem final...")

        resposta_download = requests.get(imagem_url_final)
        resposta_download.raise_for_status()

        with open("resultado.png", "wb") as arquivo:
            arquivo.write(resposta_download.content)

        print("🎉 SUCESSO! Arquivo salvo como 'resultado.png'")

    except requests.exceptions.RequestException as e:
        print(f"❌ Erro na API: {e}")
        if 'response' in locals():
            print(response.text)


# EXECUTAR
if __name__ == "__main__":
    gerar_e_baixar_imagem()