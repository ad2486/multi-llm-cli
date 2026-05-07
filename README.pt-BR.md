# Multi LLM CLI

🇧🇷 Português | 🇺🇸 [English](README.md)

```text
███╗   ███╗██╗   ██╗██╗  ████████╗██╗      ██╗     ██╗     ███╗   ███╗       ██████╗██╗     ██╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║      ██║     ██║     ████╗ ████║      ██╔════╝██║     ██║
██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║     ██║     ██╔████╔██║█████╗██║     ██║     ██║
██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║     ██║     ██║╚██╔╝██║╚════╝██║     ██║     ██║
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ███████╗███████╗██║ ╚═╝ ██║      ╚██████╗███████╗██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚══════╝╚══════╝╚═╝     ╚═╝       ╚═════╝╚══════╝╚═╝
                                                                                    by @ad2486
```

Uma CLI modular para terminal com suporte a múltiplos provedores de IA.

## Funcionalidades

* 🌐 Suporte a múltiplos provedores (OpenRouter, Groq e Google), com planos de expansão
* 💬 Conversas multi-turno com histórico de mensagens
* 🎨 Renderização de Markdown no terminal
* ⚙️ Prompt de sistema configurável
* 🔄 Troca de modelos durante a conversa
* 📥 Importação de arquivos diretamente para o contexto da conversa
* 💾 Configuração persistente entre sessões
* 📚 Listagem e seleção dinâmica de modelos

## Requisitos

* Python 3.10+
* Uma chave de API (pelo menos uma é necessária, dependendo do provedor utilizado)

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/ad2486/multi-llm-cli.git
cd multi-llm-cli
```

2. Crie um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. Crie seu arquivo `.env` baseado no exemplo:

```bash
cp .env.example .env
```

4. Adicione suas chaves de API ao `.env`:

```env
OPENROUTER_API_KEY=
GROQ_API_KEY=
GOOGLE_API_KEY=
```

5. Execute a CLI:

```bash
python main.py
```

## Uso

Digite sua mensagem e pressione Enter para conversar. Você também pode usar os seguintes comandos:

| Comando                | Descrição                                                |
| ---------------------- | -------------------------------------------------------- |
| `/model`               | Lista os modelos disponíveis e permite trocar para outro |
| `/export <nome>`       | Exporta a última resposta da IA para um arquivo `.md`    |
| `/import <arquivo>`    | Importa um arquivo para fornecer contexto ao modelo      |
| `/system <prompt>`     | Altera o prompt de sistema                               |
| `/provider <provider>` | Troca o provedor atual                                   |
| `/clear`               | Limpa o histórico da conversa                            |
| `/exit`                | Fecha a CLI                                              |

## Sobre

Olá! Eu sou **Arthur Duarte**, um estudante brasileiro do ensino médio apaixonado por programação.

Atualmente estou aprendendo HTML/CSS/JS para trabalhos freelance fullstack, e já desenvolvi projetos backend com Python e Flask. Meu objetivo é cursar Ciência da Computação e trabalhar como desenvolvedor.

Essa CLI foi um dos meus primeiros projetos Python voltados para uso real, criada para aprender sobre integração com APIs, estruturação de projetos e aplicações de terminal.

* 🐙 GitHub: [@ad2486](https://github.com/ad2486)

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

