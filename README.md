## Full Setup (Contributors) - Prerequisites 

### :warning: :warning: MAKE SURE YOU ARE USING PYTHON 3.11 :warning: :warning:
:warning: :warning: Only well-tested on MacOS :warning: :warning:

Before you begin, make sure you have the following installed:

- [Brew (if you're on a Mac)](https://brew.sh/)
- [Poetry](https://python-poetry.org/docs/#installation)
    - `brew install poetry`
- [node](https://nodejs.org/en/download/)
- [Docker](https://docs.docker.com/engine/install/)
  

Note: Our setup script does these two for you, but they are here for reference.
- [Python 3.11](https://www.python.org/downloads/)
    - `poetry env use 3.11`
- [PostgreSQL 14](https://www.postgresql.org/download/) (if you're on a Mac, setup script will install it for you if you have homebrew installed)
    - `brew install postgresql`

## Setup (Contributors)
1. Clone the repository and navigate to the root directory
1. Open Docker Desktop (Works for Windows, macOS, and Linux) or run Docker Daemon
1. Run the setup script to install the necessary dependencies and setup your environment
    ```bash
    ./setup.sh
    ```
1. Start the server
    ```bash
    ./run_skyvern.sh
    ```
1. You can start sending requests to the server, but we built a simple UI to help you get started. To start the UI, run the following command:
    ```bash
    ./run_ui.sh
    ```
1. Navigate to `http://localhost:8080` in your browser to start using the UI