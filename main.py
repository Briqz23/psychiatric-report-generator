import subprocess

def main():
    try:
        subprocess.run(["./install_dependencies.sh"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erro ao instalar as dependências: {e}")
        return

if __name__ == "__main__":
    main()
