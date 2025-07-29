import subprocess
import platform
import ipaddress
import threading
from queue import Queue

def ping(host):
    """
    Ping host. Return True if alive, False otherwise.
    """
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, '1', host]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

def worker(q, live_hosts):
    while not q.empty():
        ip = q.get()
        if ping(str(ip)):
            live_hosts.append(str(ip))
        q.task_done()

def network_scan(network):
    live_hosts = []
    q = Queue()
    # Add hosts to queue
    for ip in ipaddress.IPv4Network(network):
        q.put(ip)

    threads = []
    for _ in range(100):  # 100 threads
        t = threading.Thread(target=worker, args=(q, live_hosts))
        t.daemon = True
        t.start()
        threads.append(t)

    q.join()
    return live_hosts

def main():
    print("Network Scanner")
    network = input("Enter network (e.g., 192.168.1.0/24): ").strip()
    try:
        live_hosts = network_scan(network)
        if live_hosts:
            print(f"\nLive hosts found ({len(live_hosts)}):")
            for host in live_hosts:
                print(host)
        else:
            print("No live hosts found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
