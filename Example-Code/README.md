# Some Code Examples.

## Cross-RIR Resource Disposition Analysis

This repository contains [a Python script](analyse.py) for analyzing Cross-RIR resource disposition data by @shankarganesh.pj. The script fetches data from various sources such as the NRO statistics page, RouteViews, and REX (Resource Certification), parses the data, and performs basic analysis.

### Architecture

![high level architecture diagram](Architecture.png?raw=true "Architecture")

### Features

- Fetches and processes data from the NRO statistics page, RouteViews, and REX.
- Parses HTML content to extract relevant information.
- Periodically updates the analysis in real-time using the `schedule` library.
- Customizable for further data processing and analysis.

### Setup

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/cross-rir-analysis.git
    cd cross-rir-analysis
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:

    ```bash
    python analyze.py
    ```

### Customization

- Customize data parsing and processing functions in `analyze.py` according to your specific requirements and data formats.
- Modify the scheduling frequency in `analyze.py` based on your update interval preferences.

### Dependencies

- [requests](https://pypi.org/project/requests/): For fetching data from URLs.
- [beautifulsoup4](https://pypi.org/project/beautifulsoup4/): For parsing HTML content.
- [schedule](https://pypi.org/project/schedule/): For scheduling periodic tasks.

### Contributing

Contributions are welcome! Feel free to open issues or pull requests for any improvements or additional features.

### License

This project is licensed under the MIT.
