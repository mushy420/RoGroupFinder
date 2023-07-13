RoGroupFinder
==============
(NOT WORKING)
Overview
--------
RoGroupFinder is a Python-based tool to find Roblox groups with a specific keyword in their description and at least one classic clothing asset. The tool consists of a command-line script (`RoGroupFinder.py`) and a graphical user interface (`gui.py`).

Installation Guide
-------------------
1. Install Python 3:
   - If you don't have Python 3 installed on your system, follow the installation guide from [pypi.org](https://realpython.com/installing-python/).

2. Install the required Python packages:
   - Open your terminal or command prompt and run the following commands:


pip3 install requests pip3 install beautifulsoup4 pip3 install ratelimiter


3. Download the scripts:
   - Download the `RoGroupFinder.py` and `gui.py` scripts from the GitHub repository and save them to a folder on your computer.

Usage
-----
1. Launch the graphical user interface:
   - Open your terminal or command prompt, navigate to the folder where you saved the `RoGroupFinder.py` and `gui.py` scripts, and run the following command:


python3 gui.py


2. Enter the search criteria:
   - In the graphical user interface, enter the start and end group IDs, as well as the keyword you want to search for in the group description.

3. Start the search:
   - Click the "Search" button to find the groups matching the criteria.

4. View the results:
   - The found group IDs will be displayed in the output section of the GUI.

Notes
-----
The RoGroupFinder tool implements rate limiting to avoid getting blocked by the server for sending too many requests in a short period of time. The rate limiting is set to one request per second, which is a general guideline for web scraping.

License
-------
This project is licensed under the MIT License. See the LICENSE file for details.
