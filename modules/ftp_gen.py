from ftplib import FTP

verbose = False

def vprint(str):
        if verbose: print(str)

def simulate_ftp_interaction(hostname, username, password):
    try:
        # Connect to the FTP server
        ftp = FTP(hostname)
        ftp.login(user=username, passwd=password)

        # List the current directory
        ftp.retrlines('LIST')

        # Change directory (e.g., to 'example_dir')
        ftp.cwd('example_dir')

        # List contents of the changed directory
        ftp.retrlines('LIST')

        # Close the FTP connection
        ftp.quit()
        print("FTP interaction completed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_hostname', 'your_username', and 'your_password' with your FTP server details
def generate_ftp_traffic(dstIP):
    simulate_ftp_interaction(dstIP, 'anonymous', 'anonymous')

if __name__ == "__main__":
    verbose = True
    generate_ftp_traffic("192.168.0.105")