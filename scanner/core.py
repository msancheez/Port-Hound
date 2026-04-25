import socket
import time
import concurrent.futures
from typing import List, Optional

def port_scan(target: str, port: int, timeout: float = 0.5) -> Optional[int]:

    """
    Tries to connect to a TCP port
    If it is open, returns it.
    """

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(timeout)
        try:
            if s.connect_ex((target, port)) == 0:
                return port
        except socket.error:
            pass

    return None

def run_scanner(target: str, max_port: int, workers: int) -> List[int]:

    """
    Returns a list of open ports
    """

    open_ports = []
    print(f"[*] Starting {target} scann (Port 1 - {max_port})...\n")
    start_time = time.time()

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        nxts = {executor.submit(port_scan, target, p): p for p in range(1, max_port + 1)}

        for nxt in concurrent.futures.as_completed(nxts):
            port = nxt.result()
            if port is not None:
                print(f"[*] Port {port} open")
                open_ports.append(port)

    print(f"\n[*] Scann ended succesfully ({time.time() - start_time:.2f} seconds)")
    print(f"[*] Total Open Ports: {len(open_ports)}")

    return sorted(open_ports)