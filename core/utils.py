import sys
import rich
from rich.console import Console
from rich.text import Text
console = Console(force_terminal=True)
from core.history import ChatMemory
import requests
from rich.table import Table
from rich.columns import Columns
import json
import os
import datetime
CONFIG_FILE = "config.json"


def load_config():
    default_config = {
        "model": "openai/gpt-oss-20b:free",
        "provider_name": "openrouter"
    }

    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            saved = json.load(f)
            default_config.update(saved)
    return default_config


def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)



def handle_slash_command(user_input, memory, current_config, provider):
    command_parts = user_input.split(maxsplit=1)
    cmd = command_parts[0].lower()
    arg = command_parts[1] if len(command_parts) > 1 else None



    if cmd == "/exit":
        console.print("[bold blue]Thanks for using multi-llm-cli by @ad2486![/bold blue]")
        sys.exit()



    elif cmd == "/clear":
        memory.clear()
        console.print("[bold red]🧹 Chat history cleared![/bold red]")
        return True



    elif cmd == "/model":
        models = provider.get_available_models()
        console.print("[bold blue]Available models:[/bold blue]")

        for i, m in enumerate(models[:20]):
            console.print(f"{i} - {m}")

        choice = console.input("[blue]Select model ID or name[/blue]\n> ").strip()

        if not choice or choice.lower() in ["cancel", "none", "n"]:
            console.print("[yellow]Model unchanged.[/yellow]")
            return True

        if choice.isdigit():
            idx = int(choice)
            if 0 <= idx < len(models):
                new_model = models[idx]
            else:
                console.print(f"[bold red]❌ ID {idx} not in the list![/bold red]")
                return True

        else:
            if choice in models:
                new_model = choice
            else:
                console.print(f"[bold red]❌ Model '{choice}' wasn't found in the provider![/bold red]")
                return True

        current_config["model"] = new_model
        save_config(current_config)
        console.print(f"[bold green]✅ Model defined: {new_model}[/bold green]")

        return True



    elif cmd == "/system":

        if arg:
            memory.set_system_prompt(arg)
            current_config["system_prompt"] = arg
            save_config(current_config)
            console.print(f"[bold yellow]⚙️ Persistent personality defined![/bold yellow]")

        else:
            current = memory.system_prompt if memory.system_prompt else "Null"
            console.print(f"[bold yellow]Active prompt:[/bold yellow] {current}")

        return True



    elif cmd == "/export":
        last_msg = memory.get_last_assistant_message()

        if not last_msg:
            console.print("[bold red]❌ No AI answer to export![/bold red].")
            return True

        if arg:
            filename = arg if arg.endswith(".md") else f"{arg}.md"
        else:
            filename = f"export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.md"

        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(last_msg)

            console.print(f"[bold green]📄 Answer exported with success to:[/bold green] {filename}")

        except Exception as e:
            console.print(f"[bold red]❌ Error at export:[/bold red] {e}")

        return True



    elif cmd == "/import":
        if not arg:
            console.print("[bold red]❌ Specify the file path. Ex: /import script.py[/bold red]")
            return True

        if not os.path.exists(arg):
            console.print(f"[bold red]❌ file not found: {arg}[/bold red]")
            return True

        try:
            with open(arg, "r", encoding="utf-8") as f:
                content = f.read()

            import_msg = f"--- FILE CONTENT ({arg}) ---\n\n{content}\n\n--- FILE END ---"
            memory.add_message("user", import_msg)

            console.print(f"[bold green]📥 File '{arg}' imported to the context![/bold green]")
            console.print("[dim]Now you can ask questions about its content.[/dim]")

        except Exception as e:
            console.print(f"[bold red]❌ Error while reading file:[/bold red] {e}")

        return True



    elif cmd == "/provider":
        valid_providers = ["openrouter", "groq", "google"]

        if not arg:
            current = current_config.get("provider_name", "undefined")
            console.print(f"[bold yellow]🔌 Current provider:[/bold yellow] {current}")
            console.print(f"[blue]Available:[/blue] {valid_providers}")

        elif arg in valid_providers:
            current_config["provider_name"] = arg
            save_config(current_config)
            console.print(f"[bold green]🔌 Provider changed to: {arg}[/bold green]")

        else:
            console.print(f"[bold red]❌ Invalid Provider![/bold red] Available: {valid_providers}")

        return True


    return False

