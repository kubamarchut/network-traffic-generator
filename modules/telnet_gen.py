import telnetlib
import time

verbose = False

def vprint(str):
    if verbose: print(str)

def simulate_telnet_user(host, username, password):
    try:
        # Connect to the Telnet server
        tn = telnetlib.Telnet(host)

        # Read the login prompt and send the username
        tn.read_until(b"login: ")
        tn.write(username.encode('ascii') + b"\n")

        # Read the password prompt and send the password
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

        # Wait for a brief moment for the login process
        time.sleep(0.5)

        # Example: Sending a command after login (change this to suit your requirements)
        tn.write(b"ls\n")

        # Read and print the output after sending the command
        vprint(tn.read_very_eager().decode('ascii'))

        # Close the Telnet connection
        tn.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_hostname', 'your_username', and 'your_password' with your FTP server details
def generate_telnet_traffic(dstIP):
    simulate_telnet_user(dstIP, 'pi', 'raspberry')

if __name__ == "__main__":
    verbose = True
    generate_telnet_traffic("192.168.0.105")
