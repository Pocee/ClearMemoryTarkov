import psutil
import time
import subprocess

def is_program_running(program_name):
    """Verifica si el programa dado está en ejecución."""
    for process in psutil.process_iter(attrs=['name']):
        if process.info['name'].lower() == program_name.lower():
            return True
    return False

def clear_standby_memory(exe_path):
    """Limpiando memoria (está el Tarkov abierto)."""
    print(f"Vacíando la memoria en espera usando {exe_path}...")
    subprocess.run([exe_path], check=True)

def main():
    program_name = "escapefromtarkov.exe"
    standby_clearer_exe = "C:\\EmptyStandbyList\\EmptyStandbyList.exe" 
    check_interval = 200

    while True:
        if is_program_running(program_name):
            clear_standby_memory(standby_clearer_exe)
        time.sleep(check_interval)

if __name__ == "__main__":
    main()