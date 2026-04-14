import os
import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table

console = Console()

class MHDAssistant:
    def __init__(self):
        self.location = "Surabaya"
        self.author = "Bang MHD"
        self.division = "Muslim Hacker Division"

    def get_ascii_banner(self):
        # Banner dibuat ramping agar tidak pecah di layar kecil
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
            
            # Tabel tanpa kotak (box=None) agar lurus di terminal kecil
            table = Table(box=None, padding=(0, 2))
            table.add_column("Ibadah", style="cyan")
            table.add_column("Waktu", style="bold yellow")
            
            for sholat in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
                table.add_row(sholat, timings[sholat])
            return table
        except:
            return "[bold red]Gagal koneksi, Bang![/bold red]"

    def run(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        # Cetak Banner tanpa Panel kotak
        console.print(self.get_ascii_banner())
        
        console.print(f"\n[bold green][+][/bold green] Status: [bold cyan]ONLINE[/bold cyan]")
        console.print("-" * 25) # Garis pembatas manual
        console.print(self.get_sholat_schedule())
        console.print("-" * 25)
        
        # Dalil dengan manual wrap (\n) agar tidak nabrak pinggir layar
        dalil = "[italic green]\"Sesungguhnya shalat itu adalah fardhu yang\nditentukan waktunya atas orang-orang yang beriman.\"\n(QS. An-Nisa: 103)[/italic green]"
        console.print(f"\n{dalil}")
        
        console.print("\n[bold white][0] Exit System[/bold white]")

if __name__ == "__main__":
    app = MHDAssistant()
    app.run()
