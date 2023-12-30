import telnetlib3
import asyncio

verbose = False

def vprint(str):
    if verbose: print(str)

async def simulate_telnet_user(host, username, password):
    try:
        # Connect to the Telnet server
        reader, writer = await telnetlib3.open_connection(host)

        # Read the login prompt and send the username
        await reader.readuntil(b"login: ")
        writer.write(username.encode('ascii') + b"\n")

        # Read the password prompt and send the password
        await reader.readuntil(b"Password: ")
        writer.write(password.encode('ascii') + b"\n")

        # Wait for a brief moment for the login process
        await asyncio.sleep(0.5)

        # Example: Sending a command after login (change this to suit your requirements)
        writer.write(b"ls\n")

        # Read and print the output after sending the command
        output = await reader.readuntil(b"$")
        vprint(output.decode('ascii'))

        # Close the Telnet connection
        writer.close()
        await writer.wait_closed()
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'your_username', 'your_password' with your Telnet server details
def generate_telnet_traffic(dstIP):
    asyncio.run(simulate_telnet_user(dstIP, 'pi', 'raspberry'))

if __name__ == "__main__":
    verbose = True
    generate_telnet_traffic("telehack.com")