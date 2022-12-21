import socket
import subprocess
import time

from classes.furnace_data import FurnaceData


class FurnaceIO:

    def __init__(self, ip: str, port: str):
        self.ip = ip
        self.port = port

    def check_ping(self) -> bool:
        try:
            response = subprocess.check_output(f"ping -n 1 {self.ip}",
                                               shell=True).decode("cp866")

            if "TTL" in response:
                print(f'resource {self.ip} is available,')
                return True
            else:
                print(f'resource {self.ip} is unavailable')
                return False

        except ...:
            print(f'{self.ip} - Invalid Hostname')
            return False

    def scan_cell(self, cell_n: int) -> str:

        try:
            with socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM) as sock:
                sock.connect((self.ip, int(self.port)))
                str_2_send = "Get:" + str(cell_n)
                print('->', str_2_send)
                sock.sendall(str_2_send.encode())
                time.sleep(0.01)
                str_get = sock.recv(16)
                print('<-', str_get)
                sock.close()
            return str_get.decode().strip(';')
        except ...:
            return "Error"

    def get_current_data(self) -> FurnaceData or str:

        data_str = self.scan_cell(cell_n=1)

        if data_str == "Error":
            return data_str

        current_temperature = int(data_str)

        data_str = self.scan_cell(cell_n=2)

        if data_str == "Error":
            return data_str

        sp = int(data_str)

        return FurnaceData(temperature=current_temperature,
                           working_set_point=sp)
