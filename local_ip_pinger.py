import subprocess
import signal
import time

def collect_ips(filename):
    #collect all the ipv4s on the local network on powershell, write to ips.txt

    try:
        cmd = 'Get-NetNeighbor | Where-Object { $_.AddressFamily -eq "IPv4" } > ' + filename

        powershell_config = ['powershell', '-Command', cmd]


        result = subprocess.run(powershell_config, capture_output=True, text=True)
        content = result.stdout

        print('result; ', result)

    except subprocess.CalledProcessError as e:
        print('failed to write ips to file')



def ping_host(host, timeout):
    try:
        # Start the ping process
        ping_process = subprocess.Popen(['ping', '-n', '4', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        # Wait for the process to finish or timeout
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                # Timeout exceeded, kill the process
                ping_process.kill()
                raise TimeoutError(f"Ping to {host} timed out after {timeout} seconds")

            # Check if the process has finished
            return_code = ping_process.poll()
            if return_code is not None:
                break

            time.sleep(0.1)  # Wait for a short interval before checking again

        # Process has finished, retrieve output
        stdout, stderr = ping_process.communicate()
        if ping_process.returncode == 0:
            print(stdout.decode('utf-8'))
        else:
            print(stderr.decode('utf-8'))

    except TimeoutError as e:
        print(e)

def ping_all(filename):
    with open(filename, 'r') as file:

        for line in file:
            
            line_bytes = line.encode('utf-8')  # Convert to bytes
            cleaned_bytes = line_bytes.replace(b'\x00', b'')  # Replace null byte in bytes
            cleaned_line = cleaned_bytes.decode('utf-8')  # Convert back to string

            words = cleaned_line.split()

            if (len(words) > 0):
                try:
                    ping_host(words[1], 1)
                except IndexError as e:
                    print('Out of bounds index on array; ', words)


filename = 'ips.txt'
collect_ips(filename)
ping_all(filename)


        
    