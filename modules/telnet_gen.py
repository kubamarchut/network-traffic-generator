import telnetlib3
import asyncio
import sys

verbose = False

def vprint(str):
    if verbose: print(str)

async def simulate_telnet_user(host, username, password):
    try:
        # Connect to the Telnet server
        reader, writer = await telnetlib3.open_connection(host)

        # Read the login prompt and send the username
        await reader.readuntil(b"login: ")
        writer.write(username + "\n")

        # Read the password prompt and send the password
        await reader.readuntil(b"Password: ")
        writer.write(password + "\n")

        # Read and print the output after sending the command
        output = await reader.readuntil(b"$")
        vprint(output.decode('ascii'))

        writer.write("exit\n")
        await writer.drain()  # Wait for all data to be written
        writer.close()
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(f"An error occurred: {e} {exc_tb.tb_lineno}")

# Replace 'your_username', 'your_password' with your Telnet server details
def generate_telnet_traffic(dstIP):
    asyncio.run(simulate_telnet_user(dstIP, 'pi', 'raspberry'))


if __name__ == "__main__":
    verbose = True
    generate_telnet_traffic("192.168.0.105")