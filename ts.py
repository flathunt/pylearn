import requests
import json
import time
import os
import subprocess

# Function to set terminal color
def set_terminal_color(fg, bg):
    subprocess.call(['setterm', '--term', 'linux', '--background', bg, '--foreground', fg])

# Function to reset terminal color to default
def reset_terminal_color():
    set_terminal_color('white', 'black')

# Function to fetch tube status
def fetch_tube_status(api_url, tube_lines):
    response = requests.get(api_url + tube_lines + '/Disruption')
    if response.status_code == 200:
        return json.loads(response.text)
    return None

# Main function
def main():
    tube_lines_api = 'https://api.tfl.gov.uk/'
    tube_lines = ''  # Define the tube lines variable here, or read from a file

    try:
        while True:
            status = fetch_tube_status(tube_lines_api, tube_lines)
            if status:
                for disruption in status:
                    line = disruption['description'].split()[0].lower()
                    # Define color mapping for tube lines
                    color_mapping = {
                        'piccadilly': ('white', 'blue'),
                        'central': ('white', 'red'),
                        'northern': ('black', 'white'),
                        'district': ('black', 'green')
                    }
                    fg, bg = color_mapping.get(line, ('white', 'black'))
                    set_terminal_color(fg, bg)
                    print("\n" + disruption['description'])
                    reset_terminal_color()
                    time.sleep(2)
            else:
                reset_terminal_color()
                time.sleep(30)
    except KeyboardInterrupt:
        reset_terminal_color()
        print("\nExiting...")

if __name__ == "__main__":
    main()
