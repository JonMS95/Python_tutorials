'''
This Python module will use a third-party package managed by pip in script pip_usage.sh file.
Execute fellow shell file first.
'''

import requests

def main():
    response = requests.get("https://api.github.com")
    print(response.status_code)

if __name__ == "__main__":
    main()