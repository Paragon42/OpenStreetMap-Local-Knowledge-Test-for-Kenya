# OpenStreetMap Local Knowledge Test for Kenya

This project aims to examine the local knowledge contributions in OpenStreetMap (OSM) for Kenya in the year 2022. It focuses on key aspects such as places, amenities, and healthcare facilities, investigating the count of contributors and their usernames. This repository contains Python scripts leveraging the powerful Osmium library and the Ohsome API for data extraction and analysis.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8 or later
- Python libraries: 
  - osmium
  - pandas
  - requests

You can install the necessary libraries using pip:
```shell
pip install osmium pandas requests
```

### Running the Scripts

1. **Contributor Extraction:** The script `contributor_extraction.py` uses the Osmium library to parse the OSM full history dump for Kenya, filtering out contributions related to places, amenities, and healthcare made in 2022. The output is a list of contributor usernames and their respective contribution counts.

2. **Local Knowledge Extraction:** The script `local_knowledge_extraction.py` employs the Ohsome API to fetch data related to places, amenities, and healthcare from the OSM database for Kenya. The results include various statistics about the contributions.

### Output

The outputs of these scripts are CSV files containing the extracted data. You can import these CSV files into your preferred data analysis or visualization tool for further study.

## Built With

- [Python](https://www.python.org/) - The scripting language used.
- [Osmium](https://osmcode.org/pyosmium/) - A Python library for processing OSM data.
- [Ohsome API](https://api.ohsome.org/v1/swagger-ui.html) - API used to fetch OSM data.

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Authors

- Your Name - Initial work

See also the list of [contributors](https://github.com/your/repo/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Acknowledgments

- Thanks to the OSM community for providing the valuable data that made this analysis possible.

---

Feel free to modify this README to better suit your project. Good documentation helps others understand, use, and contribute to your project. Happy coding!
