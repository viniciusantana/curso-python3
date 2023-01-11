# Seção 02: Python + VScode - preparando meu ambiente de desenvolvimento
- Instalação do Python e Vscode
- Configuração do VSCode
- compact folders
- vs code shortcuts (atalhos)
- extensão: code-runner
- extensão: python
- configurações adicionadas no vscode:
```
"explorer.compactFolders": false,
"code-runner.runInTerminal": true,
"code-runner.ignoreSelection": true,
"code-runner.executorMap": {
        "python": "cls ; python -u", <<< windows
        "python": "clear ; python -u", <<< linux
    },
"python.defaultInterpreterPath": "python",
```

## Aulas
- [x] 3. Introdução à seção
- [x] 4. Ubuntu 22 - Instalação básica do Python e o VS Code

```
sudo apt update -y
sudo apt upgrade -y
sudo apt install git curl build-essential -y
sudo apt install gcc make default-libmysqlclient-dev libssl-dev -y
sudo apt install python3.10-full python3.10-dev -y
```

- [x] 5. Ubuntu 22 - Instalação Complexa do Python e o VS Code (pyenv e zsh)
```
Anexo:
ambiente-dev-ubuntu-curso-python.sh
```
- [x] 6. Windows 11 - Instalando o Python e o VS Code
- [x] 7. macOS - Instalando o Python e o VS Code
- [x] 8. Para iniciantes: sobre as próximas aulas de configurações e instalações
- [x] 9. Para iniciantes: configurações VS Code (Parte 1)
- [x] 10. Para iniciantes: configurações VS Code (Parte 2)
- [x] 11. Para iniciantes: configurações VS Code (Parte 3)
- [x] 12. Para iniciantes: VS Code em Linux e Mac OS (assista mesmo se estiver em Windows)
