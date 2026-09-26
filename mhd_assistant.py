import os
import requests
from datetime import datetime
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.align import Align

console = Console()

class MHDAssistant:
    def __init__(self):
        self.location = "Surabaya"
        self.author = "Bang MHD"
        self.division = "Muslim Hacker Division"

    def get_ascii_banner(self):
        # Banner modern dengan efek gradient dan styling
        banner = """
╔═══════════════════════════════════════╗
║                                       ║
║    ███╗   ███╗██╗  ██╗██████╗      ║
║    ████╗ ████║██║  ██║██╔══██╗     ║
║    ██╔████╔██║███████║██║  ██║     ║
║    ██║╚██╔╝██║██╔══██║██║  ██║     ║
║    ██║ ╚═╝ ██║██║  ██║██████╔╝     ║
║    ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝      ║
║                                       ║
║  🕌 Muslim Hacker Division 🕌         ║
║  Surabaya Islamic Tech Community      ║
║                                       ║
╚═══════════════════════════════════════╝
        """
        return banner

    def get_sholat_schedule(self):
        try:
            url = f"https://api.aladhan.com/v1/timingsByCity?city={self.location}&country=Indonesia&method=2"
            response = requests.get(url).json()
            timings = response['data']['timings']
            
            # Tabel dengan styling modern
            table = Table(box=None, padding=(0, 2), show_header=True, header_style="bold magenta")
            table.add_column("🕐 Ibadah", style="cyan")
            table.add_column("⏰ Waktu", style="bold yellow")
            
            sholat_icons = {
                'Fajr': '🌅 Subuh',
                'Dhuhr': '☀️  Dzuhur',
                'Asr': '🌤️  Ashar',
                'Maghrib': '🌅 Maghrib',
                'Isha': '🌙 Isya'
            }
            
            for sholat in ['Fajr', 'Dhuhr', 'Asr', 'Maghrib', 'Isha']:
                table.add_row(sholat_icons[sholat], timings[sholat])
            return table
        except:
            return "[bold red]❌ Gagal koneksi, Bang![/bold red]"

    def run(self):
        os.system('clear' if os.name == 'posix' else 'cls')
        
        # Cetak Banner dengan Panel modern
        banner_text = self.get_ascii_banner()
        panel = Panel(
            banner_text,
            style="bold cyan",
            border_style="bright_cyan",
            padding=(1, 2)
        )
        console.print(panel)
        
        # Status line dengan animasi
        status_line = "[bold green]✓[/bold green] Status: [bold cyan]ONLINE[/bold cyan] | [bold yellow]⚡ Ready[/bold yellow]"
        console.print(Align.center(status_line))
        
        # Divider modern
        console.print("[bright_cyan]" + "═" * 50 + "[/bright_cyan]")
        
        # Jadwal Sholat
        console.print("\n[bold magenta]📍 Jadwal Sholat - Surabaya[/bold magenta]\n")
        console.print(self.get_sholat_schedule())
        
        # Divider
        console.print("\n[bright_cyan]" + "═" * 50 + "[/bright_cyan]")
        
        # Dalil dengan styling lebih bagus
        dalil = """
[bold green]📖 Dalil Al-Qur'an[/bold green]
[italic cyan]"Sesungguhnya shalat itu adalah fardhu yang
ditentukan waktunya atas orang-orang yang beriman."
(QS. An-Nisa: 103)[/italic cyan]
        """
        console.print(dalil)
        
        # Footer dengan informasi
        footer = "[bold white]───────────────────────────────────────────────[/bold white]\n"
        footer += "[dim]Developed by: Bang MHD | Muslim Hacker Division[/dim]\n"
        footer += "[bold white]───────────────────────────────────────────────[/bold white]\n"
        footer += "[bold yellow][0][/bold yellow] [bold white]Exit System[/bold white]"
        console.print(footer)

if __name__ == "__main__":
    app = MHDAssistant()
    app.run()
