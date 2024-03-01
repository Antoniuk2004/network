import psutil

from Interface import Interface


def calc_number_of_interfaces():
    network_stats = psutil.net_io_counters(pernic=True)
    return len(network_stats.values())


def get_list_of_interfaces():
    list_of_interfaces = []

    network_stats = psutil.net_io_counters(pernic=True)
    for index, key in enumerate(network_stats.keys()):
        value = network_stats[key]

        interface = Interface()
        interface.set_index(index)
        interface.set_name(key)
        interface.set_bytes_sent(value.bytes_sent)
        interface.set_bytes_received(value.bytes_recv)

        list_of_interfaces.append(interface)

    return list_of_interfaces
