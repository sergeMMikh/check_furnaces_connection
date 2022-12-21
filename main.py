from datetime import datetime
import socket
import subprocess
import time


class FurnaceData:

    def __init__(self, temperature: int, working_set_point: int):
        self.temperature = temperature
        self.working_set_point = working_set_point
        self.measured_at = datetime.now()

    def __str__(self):
        return f'Measuring time: {self.measured_at}\tT: {self.temperature}\tWSP: {self.working_set_point}'


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
                print(f'resource {self.ip} + is unavailable')
                return False

        except ...:
            print(f'{self.ip} - Invalid Hostname')
            return False

    def scan_cell(self, cell_n: int) -> str:

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((self.ip, int(self.port)))
            str_2_send = "Get:" + str(cell_n)
            print('->', str_2_send)
            sock.sendall(str_2_send.encode())
            time.sleep(0.01)
            str_get = sock.recv(16)
            print('<-', str_get)
            sock.close()
        return str_get.decode()

    def get_current_data(self):
        current_temperature = int(self.scan_cell(cell_n=1))
        sp = int(self.scan_cell(cell_n=2))
        return FurnaceData(temperature=current_temperature,
                           working_set_point=sp)


def main():
    furnace = FurnaceIO(ip='192.168.1.8',
                        port='9003')

    if furnace.check_ping():
        print(furnace.get_current_data())


if __name__ == '__main__':
    main()
