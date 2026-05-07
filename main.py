import typer
from rich.console import Console
from rich.markdown import Markdown
from rich.text import Text
from dotenv import load_dotenv
import colorsys

from providers.openrouter import OpenRouterProvider
from providers.groq import GroqProvider
from providers.google import GoogleProvider
from core.history import ChatMemory
from core.utils import handle_slash_command, load_config

load_dotenv()
console = Console(force_terminal=True)
app = typer.Typer()

PROVIDER_CLASSES = {
    "openrouter": OpenRouterProvider,
    "groq": GroqProvider,
    "google": GoogleProvider
}

config = load_config()
memory = ChatMemory(system_prompt=config.get("system_prompt", ""))
current_provider_name = config.get("provider_name", "openrouter")
provider = PROVIDER_CLASSES[current_provider_name]()


BANNER = r""" 
------------------------------------------------------------------------------------------------

███╗   ███╗██╗   ██╗██╗  ████████╗██╗      ██╗     ██╗     ███╗   ███╗       ██████╗██╗     ██╗
████╗ ████║██║   ██║██║  ╚══██╔══╝██║      ██║     ██║     ████╗ ████║      ██╔════╝██║     ██║
██╔████╔██║██║   ██║██║     ██║   ██║█████╗██║     ██║     ██╔████╔██║█████╗██║     ██║     ██║
██║╚██╔╝██║██║   ██║██║     ██║   ██║╚════╝██║     ██║     ██║╚██╔╝██║╚════╝██║     ██║     ██║
██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║      ███████╗███████╗██║ ╚═╝ ██║      ╚██████╗███████╗██║
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝      ╚══════╝╚══════╝╚═╝     ╚═╝       ╚═════╝╚══════╝╚═╝
                                                                                    by @ad2486                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
------------------------------------------------------------------------------------------------         
"""


def print_nyan_banner(text):
    lines = text.splitlines()
    for i, line in enumerate(lines):

        hue = (i * 0.2) % 1.0
        rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)

        color_hex = "#{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )

        console.print(line, style=color_hex, soft_wrap=True)





@app.command()
def main():

    global provider, current_provider_name


    console.clear()
    print_nyan_banner(BANNER)
    console.print(f"[blue]Multi-LLM CLI loaded![/blue] (Model: {config['model']})")
    console.print(
        "Write [bold magenta]/exit[/bold magenta] to quit or [bold magenta]/model[/bold magenta] to change the model.\n")

    while True:
        try:
            model_display = config["model"].split('/')[-1]
            prompt_text = f"[bold magenta]({model_display})[/bold magenta] [bold cyan]❯ [/bold cyan]"
            user_input = console.input(prompt_text).strip()

            if not user_input:
                continue

            if handle_slash_command(user_input, memory, config, provider):

                if config["provider_name"] != current_provider_name:
                    current_provider_name = config["provider_name"]
                    provider = PROVIDER_CLASSES[current_provider_name]()
                    console.print(f"[bold cyan]🔄 Provider switched to: {current_provider_name}[/bold cyan]")

                continue

            memory.add_message("user", user_input)

            with console.status("[bold blue]Consulting AI..."):
                response = provider.ask(config["model"], memory.get_context())

            memory.add_message("assistant", response)

            console.print("\n" + "─" * 20)
            console.print(Markdown(response))
            console.print("─" * 20 + "\n")

        except KeyboardInterrupt:
            # Trata o Ctrl+C de forma elegante
            console.print("\n[yellow]Exiting...[/yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]❌ Error:[/bold red] {e}")


if __name__ == "__main__":
    app()


