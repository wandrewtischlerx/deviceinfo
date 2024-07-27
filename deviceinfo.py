import platform
import psutil # type: ignore
import socket
import os
import requests
from datetime import datetime
from colorama import Fore, Style, init



YELLOW = '\033[93m'
RESET = '\033[0m'

print(YELLOW + "\n  _____             _          _____        __      ")
print(" |  __ \           (_)        |_   _|      / _|     ")
print(" | |  | | _____   ___  ___ ___  | |  _ __ | |_ ___  ")
print(" | |  | |/ _ \ \ / / |/ __/ _ \ | | | '_ \|  _/ _ \ ")
print(" | |__| |  __/\ V /| | (_|  __/_| |_| | | | || (_) |")
print(" |_____/ \___| \_/ |_|\___\___|_____|_| |_|_| \___/ " + RESET)
print(f"\n{Fore.YELLOW}   Desenvolvido Por @WandrewTischler     {Fore.BLUE}v1.0{Fore.RESET}")


# Cores ANSI para formatação
GREEN = '\033[92m'
RESET = '\033[0m'

# URL da API para geolocalização
IPAPI_URL = "http://ip-api.com/json/"

def get_size(bytes, suffix="B"):
    """
    Converte bytes em formato legível (KB, MB, GB, etc.).
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
    return f"{bytes:.2f}Y{suffix}"

def get_ip_info():
    """
    Obtém informações de geolocalização com base no IP usando ip-api.
    """
    try:
        response = requests.get(IPAPI_URL)
        response.raise_for_status()  # Verifica se houve um erro HTTP
        data = response.json()
        
        ip_info = {
            'Endereço IP': data.get('query', 'Não disponível'),
            'País': data.get('country', 'Não disponível'),
            'Estado': data.get('regionName', 'Não disponível'),
            'Cidade': data.get('city', 'Não disponível'),
            'Provedor de Internet': data.get('isp', 'Não disponível'),
            'Coordenadas': f"{data.get('lat', 'Não disponível')}, {data.get('lon', 'Não disponível')}"
        }
        
        return ip_info
    except requests.RequestException as e:
        print("Erro ao fazer a solicitação para a API:", e)
        return {
            'Endereço IP': 'Não disponível',
            'País': 'Não disponível',
            'Estado': 'Não disponível',
            'Cidade': 'Não disponível',
            'Provedor de Internet': 'Não disponível',
            'Coordenadas': 'Não disponível'
        }

def get_cooler_rpm():
    """
    Obtém a rotação do cooler, se disponível.
    """
    try:
        # Tenta acessar sensores do sistema
        sensors = psutil.sensors_fans()
        if sensors:
            for fan_name, fan_info in sensors.items():
                if fan_info:
                    return f"{fan_info[0].current} RPM"  # Retorna a rotação do primeiro cooler
        return "Não disponível"
    except Exception as e:
        return "Não disponível"

def get_device_info():
    device_info = {}

    # Informações básicas do sistema
    device_info['\n\nNome do Dispositivo'] = platform.node()
    device_info['Sistema Operacional'] = platform.system()
    device_info['Versão do SO'] = platform.version()
    device_info['Arquitetura do SO'] = f"{platform.architecture()[0]} ({platform.architecture()[1]})"
    
    # Informações sobre o usuário
    device_info['Usuário'] = os.getlogin()

    # Informações sobre o hardware
    device_info['Processador'] = platform.processor()
    device_info['Número de Núcleos'] = psutil.cpu_count(logical=True)
    device_info['Frequência do CPU'] = f"{psutil.cpu_freq().current} MHz"
    device_info['Memória RAM Total'] = f"{psutil.virtual_memory().total / (1024**3):.2f} GB"

    # Informações sobre a bateria
    battery = psutil.sensors_battery()
    if battery:
        device_info['Status da Bateria'] = f"{battery.percent}%"
        device_info['Carregando'] = 'Sim' if battery.power_plugged else 'Não'
        if battery.secsleft == psutil.POWER_TIME_UNLIMITED:
            device_info['Tempo Restante'] = 'Carregando'
        elif battery.secsleft == psutil.POWER_TIME_UNKNOWN:
            device_info['Tempo Restante'] = 'Desconhecido'
        else:
            device_info['Tempo Restante'] = f"{battery.secsleft // 60} minutos"
    else:
        device_info['Status da Bateria'] = 'Não disponível'
        device_info['Carregando'] = 'Não aplicável'
        device_info['Tempo Restante'] = 'Não aplicável'

    # Informações sobre os discos
    partitions = psutil.disk_partitions()
    disk_info = []
    for partition in partitions:
        usage = psutil.disk_usage(partition.mountpoint)
        disk_info.append(f"{partition.device}: {get_size(usage.total)} (Usado: {get_size(usage.used)}, Livre: {get_size(usage.free)}, Sistema de Arquivos: {partition.fstype})")
    
    device_info['Discos'] = ', '.join(disk_info)
    
    # Informações de rede
    interfaces = psutil.net_if_addrs()
    network_info = []
    for iface, addrs in interfaces.items():
        for addr in addrs:
            if addr.family == socket.AF_INET:
                network_info.append(f"{iface}: {addr.address} (Máscara: {addr.netmask})")
    
    device_info['Interfaces de Rede'] = ', '.join(network_info) if network_info else 'Não disponível'

    # Data e hora local
    now = datetime.now()
    device_info['Data e Hora Local'] = now.strftime("%Y-%m-%d %H:%M:%S")

    # Informações sobre o cooler
    device_info['RPM do Cooler'] = get_cooler_rpm()

    return device_info

def print_device_info():
    info = get_device_info()
    ip_info = get_ip_info()

    for key, value in info.items():
        print(f"{key}: {GREEN}{value}{RESET}")

    print("\nInformações de Geolocalização:")
    for key, value in ip_info.items():
        print(f"{key}: {GREEN}{value}{RESET}")

    # Adiciona o link do Google Maps se as coordenadas estiverem disponíveis
    coordinates = ip_info.get('Coordenadas', 'Não disponível')
    if coordinates and coordinates != 'Não disponível':
        lat, lon = coordinates.split(', ')
        print(f"\nLink do Google Maps: {GREEN}https://www.google.com/maps?q={lat},{lon}{RESET}")

if __name__ == "__main__":
    print_device_info()
