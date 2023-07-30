

# DVD Rental ETL Project

This project is an Extract, Transform, Load (ETL) system for the DVD rental database. It extracts data from the DVD rental database, performs necessary transformations, and loads the transformed data into a target destination.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [ETL Process](#etl-process)
- [Data Sources](#data-sources)
- [Transformations](#transformations)
- [Destination](#destination)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to extract data from the DVD rental database, transform it into a suitable format, and load it into a target destination. The main goal is to provide a clean and structured dataset that can be used for various analytics and reporting purposes.

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/dvd-rental-etl.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up the necessary configurations (database credentials, target destination, etc.) in the configuration file.

## Usage

Once the project is installed, you can run the ETL process by executing the main script. Here's an example:

```bash
python etl.py
```

Make sure to update the configuration file with the correct database credentials and target destination before running the script.

## ETL Process

The ETL process consists of three main steps:

1. Extraction: Data is extracted from the DVD rental database using SQL queries.
2. Transformation: The extracted data is transformed to meet specific requirements. This may include cleaning, filtering, aggregating, and enriching the data as needed.
3. Loading: The transformed data is loaded into a target destination, such as a data warehouse, CSV files, or a relational database.

## Data Sources

The data for this project is sourced from the DVD rental database. The database contains various tables related to DVD rentals, including customers, films, rentals, payments, etc. The database schema can be found in the `schema.sql` file.

## Transformations

During the transformation process, several data manipulations are performed to ensure the data is in a suitable format. Some of the transformations applied in this project include:

- Cleaning and standardizing data formats.
- Handling missing or null values.
- Joining and aggregating data from multiple tables.
- Deriving new features or calculations.

For detailed information on the transformations applied, refer to the `transform.py` module.

## Destination

The transformed data is loaded into a target destination, which can be customized based on your requirements. In this project, we have chosen to load the data into a PostgreSQL database. However, you can modify the code and configure it to load the data into a different destination, such as a data warehouse or CSV files.

## Dependencies

This project has the following dependencies:

- Python 3.x
- Pandas
- psycopg2 (for connecting to PostgreSQL)
- Other dependencies listed in the `requirements.txt` file

## Contributing

Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---


