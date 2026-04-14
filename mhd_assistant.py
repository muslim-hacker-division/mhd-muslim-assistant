import os
import requests
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

class MHDAssistant:
    def __init__(self):
        self.location = "Surabaya"
        self.author = "MHD"
        self.division = "Muslim Hacker Division"

    def get_ascii_banner(self):
        # Banner dibuat lebih ramping agar muat di layar Termux HP
        banner = """
  __  __ _   _ ____  
 |  \/  | | | |  _ \ 
 | |\/| | |_| | | | |
 | |  | |  _  | |_| |
 |_|  |_|_| |_|____/ 
        """
        return f"[bold green]{banner}[/bold green]\n[bold white]{self.division}[/bold white]"

    def get_sholat_schedule(self):
        try:
            url = f"https://api.aladhan.com/v1/timingsByCity?city={self.location}&country=Indonesia&method=2"
            response = requests.get(url).json()
            timings = response['data']['timings']
            
            table = Table(title=f"Jadwal Sholat - {self.location}", style="green", expand=True)
            table.add_column("Ibadah", style="cyan", justify="left")
            table.add_column("Waktu", style="bold yellow", justify="right")
            table.add_row("Fajr", timings['Fajr'])
            table.add_row("Dhuhr", timings['Dhuhr'])
            table.add_row("Asr", timings['Asr'])
            table.add_row("Maghrib", timings['Maghrib'])
            table.add_row("Isha", timings['Isha'])
            return table
        except:
            return "[bold red]Gagal koneksi, Bang![/bold red]"

    def run(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        # Panel disesuaikan agar rapi di layar kecil maupun besar
        console.print(Panel(self.get_ascii_banner(), border_style="green", padding=(0, 2)))
        
        console.print(f"\n[bold green][+][/bold green] Status: [bold cyan]ONLINE[/bold cyan]")
        console.print(self.get_sholat_schedule())
        
        # Update Dalil QS. An-Nisa: 103
        dalil = "[bold green]\"Sesungguhnya shalat itu adalah fardhu yang ditentukan waktunya atas orang-orang yang beriman.\"\n(QS. An-Nisa: 103)[/bold green]"
        console.print(Panel(dalil, title="[bold white]Nasihat Hari Ini[/bold white]", border_style="cyan"))
        
        console.print("\n[bold white][0] Exit System[/bold white]")

if __name__ == "__main__":
    app = MHDAssistant()
    app.run()