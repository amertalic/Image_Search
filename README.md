# Search Image app

This is a small Python app designed to fetch images related to a user's query from Wikipedia and display them. The app uses the Kivy framework for the graphical user interface and leverages Wikipedia's API to retrieve relevant images.

## Features

- **User-Friendly Interface**: The app provides a simple interface where users can input a query, and the app fetches and displays related images from Wikipedia.

- **Random Search**: In case of a disambiguation error, where multiple options are available for the user's query, the app randomly selects one of the options and retrieves images for that selection.

- **Image Download**: The app downloads the first available image related to the user's query and stores it in a local directory for future use.

## Requirements

- Python 3.11
- Kivy framework
- Wikipedia API
- Requests library

## Installation

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the main app file:

```bash
python main.py
```

1. Enter a search query in the provided input field.
2. Press the "Search" button to fetch and display related images.
3. The first image will be downloaded and stored locally in the "storage" directory.
