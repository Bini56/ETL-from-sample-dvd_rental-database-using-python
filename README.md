<!DOCTYPE html>
<html>
<head>
    <title>DVD Rental ETL Project</title>
</head>
<body>
    <h1>DVD Rental ETL Project</h1>

    <h2>Table of Contents</h2>
    <ul>
        <li><a href="#introduction">Introduction</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
        <li><a href="#etl-process">ETL Process</a></li>
        <li><a href="#data-sources">Data Sources</a></li>
        <li><a href="#transformations">Transformations</a></li>
        <li><a href="#destination">Destination</a></li>
        <li><a href="#dependencies">Dependencies</a></li>
        <li><a href="#contributing">Contributing</a></li>
        <li><a href="#license">License</a></li>
    </ul>

    <h2 id="introduction">Introduction</h2>
    <p>This project is an Extract, Transform, Load (ETL) system for the DVD rental database. It extracts data from the DVD rental database, performs necessary transformations, and loads the transformed data into a target destination.</p>

    <h2 id="installation">Installation</h2>
    <p>To run this project locally, follow these steps:</p>
    <ol>
        <li>Clone the repository: <code>git clone https://github.com/your-username/dvd-rental-etl.git</code></li>
        <li>Install the required dependencies: <code>pip install -r requirements.txt</code></li>
        <li>Set up the necessary configurations (database credentials, target destination, etc.) in the configuration file.</li>
    </ol>

    <h2 id="usage">Usage</h2>
    <p>Once the project is installed, you can run the ETL process by executing the main script. Here's an example:</p>
    <pre><code>python etl.py</code></pre>
    <p>Make sure to update the configuration file with the correct database credentials and target destination before running the script.</p>

    <h2 id="etl-process">ETL Process</h2>
    <p>The ETL process consists of three main steps:</p>
    <ol>
        <li>Extraction: Data is extracted from the DVD rental database using SQL queries.</li>
        <li>Transformation: The extracted data is transformed to meet specific requirements. This may include cleaning, filtering, aggregating, and enriching the data as needed.</li>
        <li>Loading: The transformed data is loaded into a target destination, such as a data warehouse, CSV files, or a relational database.</li>
    </ol>

    <h2 id="data-sources">Data Sources</h2>
    <p>The data for this project is sourced from the DVD rental database. The database contains various tables related to DVD rentals, including customers, films, rentals, payments, etc. The database schema can be found in the <code>schema.sql</code> file.</p>

    <h2 id="transformations">Transformations</h2>
    <p>During the transformation process, several data manipulations are performed to ensure the data is in a suitable format. Some of the transformations applied in this project include:</p>
    <ul>
        <li>Cleaning and standardizing data formats.</li>
        <li>Handling missing or null values.</li>
        <li>Joining and aggregating data from multiple tables.</li>
        <li>Deriving new features or calculations.</li>
    </ul>
    <p>For detailed information on the transformations applied, refer to the <code>transform.py</code> module.</p>

    <h2 id="destination">Destination</h2>
    <p>The transformed data is loaded into a target destination, which can be customized based on your requirements. In this project, we have chosen to load the data into a PostgreSQL database. However, you can modify the code and configure it to load the data into a different destination, such as a data warehouse or CSV files.</p>

    <h2 id="dependencies">Dependencies</h2>
    <p>This project has the following dependencies:</p>
    <ul>
        <li>Python 3.x</li>
        <li>Pandas</li>
        <li>psycopg2 (for connecting to PostgreSQL)</li>
        <li>Other dependencies listed in the <code>requirements.txt</code> file</li>
    </ul>

    <h2 id="contributing">Contributing</h2    <p>Contributions to this project are welcome. If you have any suggestions, improvements, or bug fixes, feel free to open an issue or submit a pull request.</p>

    <h2 id="license">License</h2>
    <p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
</body>
</html>
