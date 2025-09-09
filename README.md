# Einstieg

Einstieg is a location-based chat application that connects users who are within close proximity—specifically, within 500 meters. This app is designed to help people meet and interact with others nearby, making it ideal for use at events, on public transport, in parks, or any place where people gather and might want to connect.

## Features

- **Proximity Messaging:** Users can privately message others who are physically nearby (within approximately 500 meters).
- **Event Networking:** Ideal for conferences, concerts, or festivals to meet and connect with new people in your vicinity.
- **Privacy First:** Only users within the defined proximity can discover and message each other.
- **Simple API:** Built with FastAPI for easy integration and scalability.

## Use Cases

- **Events:** Attendees can connect and chat with others at the same venue.
- **Public Transport:** Commuters can interact with fellow passengers.
- **Parks & Public Spaces:** Meet new people in your immediate vicinity.

## Getting Started

### Prerequisites

- Python 3.13 or higher
- [FastAPI](https://fastapi.tiangolo.com/)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/einstieg.git
    cd einstieg
    ```

2. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows: .venv\Scripts\activate
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
    Or, if using `pyproject.toml`:
    ```bash
    pip install .
    ```

### Running the Application

Start the FastAPI server:
