from classes.furnace_io import FurnaceIO


def main():
    furnace = FurnaceIO(ip='192.168.1.250',
                        port='9003')

    if furnace.check_ping():
        print(furnace.get_current_data())


if __name__ == '__main__':
    main()
