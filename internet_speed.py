import psutil
import speedtest
from tabulate import tabulate
from pyfiglet import Figlet

def render_header():
    """
    Renders the header using Figlet with a slant font.
    """
    figlet = Figlet(font='slant')
    print(figlet.renderText('Internet Speed'))

class NetworkDetails:
    def __init__(self):
        self.parser = psutil.net_if_addrs()
        self.speed_parser = speedtest.Speedtest()  # Use correct capitalization for Speedtest class
        self.interfaces = self.get_interfaces()

    def get_interfaces(self):
        """
        Retrieves the network interface names.
        """
        interfaces = []
        for interface_name in self.parser.keys():  # Corrected parser attribute name
            interfaces.append(str(interface_name))
        return interfaces

    def __repr__(self):
        download_speed = f"{round(self.speed_parser.download() / 1_000_000, 2)} Mbps"
        upload_speed = f"{round(self.speed_parser.upload() / 1_000_000, 2)} Mbps"
        interfaces = ', '.join(self.interfaces)
        data = {
            "Interface": [interfaces],
            "Download": [download_speed],
            "Upload": [upload_speed]
        }
        table = tabulate(data, headers="keys", tablefmt="pretty")
        return table

if __name__ == "__main__":
    render_header()
    print(NetworkDetails())
