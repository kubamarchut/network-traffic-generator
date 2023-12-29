import requests

def generate_http_traffic(dstIP):
    try:
        url = 'http://' + dstIP  # Replace with your desired URL
        response = requests.get(url)
        print(url)
        if response.status_code == 200:
            return response.text  # Return the response content if successful
        else:
            return f"Request failed with status code: {response.status_code}"
    except requests.RequestException as e:
        return f"Request failed: {e}"


if __name__ == "__main__":
    # Example usage:
    result = generate_http_traffic("192.168.0.105")
    print(result)