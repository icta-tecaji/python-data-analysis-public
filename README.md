# Analitika 1: Analitika podatkov v Python-u (public)

Repozitorji za primere in gradiva tečaja Analitika podatkov v Python-u.

## Termini
01. (pon) 23.1.
02. (pon) 30.1.
03. (pon) 06.2.
04. (pon) 13.2.
05. (pon) 20.2.
06. (sre) 01.3.
07. (pon) 06.3.
08. (sre) 15.3.
09. (pon) 20.3.
10. (pon) 27.3. 
11. (pon) 03.4. - Izpit

## Zagon 
### Linux (Ubuntu 20)
- Po potrebi namestimo git in Python:
    - https://git-scm.com/book/en/v2/Getting-Started-Installing-Git
- Prenesemo repozitoriji: `git clone https://github.com/icta-tecaji/python-analitika-public.git`
- Namestimo Python venv: `apt install python3.8-venv`
- Ustvarimo virtualno okolje: `python3 -m venv .venv`
- Aktiviramo virtualno okolje: `source .venv/bin/activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`
- Remote access (before running the notebook):
    - Generate the config file: `jupyter notebook --generate-config`
    - Add the following lines to the conifg:
        - `c.NotebookApp.allow_origin = '*'`
        - `c.NotebookApp.ip = '0.0.0.0'`

### Windows 10
- Po potrebi namestimo git in Python:
    - https://git-scm.com/download/win
    - https://www.python.org/downloads/windows/
- Prenesemo repozitoriji: `git clone https://github.com/icta-tecaji/python-analitika-public.git`
- Ustvarimo virtualno okolje: `python -m venv .venv`
- Aktiviramo virtualno okolje: `.venv\Scripts\activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`

### Mac OS
- Po potrebi namestimo git in Python:
    - https://git-scm.com/download/mac
    - https://www.python.org/downloads/macos/
- Prenesemo repozitoriji: `git clone https://github.com/icta-tecaji/python-analitika-public.git`
- Ustvarimo virtualno okolje: `python3 -m venv .venv`
- Aktiviramo virtualno okolje: `source .venv/bin/activate`
- Namestimo vse potrebne knjižnice: `pip install -r requirements.txt`
- Zagon Jupyter Notebooks: `jupyter notebook`
- Odpremo v brskalniku: `http://<IP>:8888/?token=<TOKEN>`

## Vsebina
### Del 1: Uvod v analitiko podatkov in priprava okolja
- Vloga podatkov
- What is Data?
- Data Engineer, Data Analyst, Data Scientist — What’s the Difference?
- Overview of the data science process
- Priprava okolja
- Jupyter Notebooks

### Del 2: Uvod v NumPy
- Understanding Data Types in Python
- Example: Data analysis in pure Python
- How Vectorization Makes Code Faster
- Numpy library
- Introduction to Ndarrays
- Reading CSV files with NumPy
- Array Shapes
- Selecting and Slicing Rows and Items from ndarrays
- Selecting Columns and Custom Slicing ndarrays
- Vector Math
- Calculating Statistics For 1D ndarrays
- Calculating Statistics For 2D ndarrays
- Datatypes
- Boolean Indexing
- The meaning of shapes in NumPy
- Assigning Values
- Adding Rows and Columns to ndarrays
- Computation on NumPy Arrays: Universal Functions
- Subarrays as no-copy views
- Copying Data

### Del 3: Uvod v Pandas
- Understanding pandas and NumPy
- About pandas
- Importing pandas
- Introduction to the Data
- Introducing Pandas Objects - Data Structures
- Introducing DataFrames
- Pandas Data Selection - indexing
- Vectorized Operations
- Series Data Exploration Methods
- Method Chaining
- Dataframe Exploration Methods
- Assignment with pandas
- Using Boolean Indexing with pandas Objects
- Creating New Columns
- Top Performers by Country
- Reading CSV files with pandas
- Using iloc to select by integer position
- Using pandas methods to create boolean masks
- Working with Integer Labels
- Pandas Index Alignment
- Boolean Operators
- Sorting Values
- Using Loops with pandas
- Primer: Calculating Return on Assets by Country
- Understanding SettingwithCopyWarning in pandas

### Del 4: Priprava in čiščenje podatkov
- Get the data - Reading CSV Files with Encodings
- Cleaning Column Names
- Converting String Columns to Numeric
- Renaming Columns
- Extracting Values from Strings
- Correcting Bad Values - map() method
- Introduction to Missing Data
    - Trade-Offs in Missing Data Conventions
    - Missing Data in Pandas
    - None: Pythonic missing data
    - NaN: Missing numerical data
    - NaN and None in Pandas
    - Operating on Null Values
        - Detecting null values
        - Dropping null values
        - Filling null values
- Dropping Missing Values
- Filling Missing Values
- Removing Duplicates
- Replacing Values
- Dropping Columns
- Vaja          
- Save clean data to CSV file
- Analiza

### Del 5: Prikazovanje podatkov - osnovno
- Representation Of Data 
- Introduction To The Data
- Introduction to matplotlib
- Axis Ticks
    - Fixing Axis Ticks
    - Adding Axis Labels And A Title
- Matplotlib Classes
- Grid Positioning
- Adding Data
- Formatting And Spacing
- Comparing Across More Years
- Overlaying Line Charts
- Adding A Legend
- Introduction to the data
- Bar Plots
    - Creating Bars
    - Aligning Axis Ticks And Labels
    - Horizontal Bar Plot
- Scatter plot
    - Switching axes
    - Benchmarking correlation
- Histogram
    - Frequency Distribution
    - Binning
    - Histogram In Matplotlib
    - Comparing histograms
    - Quartiles
- Box Plot
    - Multiple Box Plots
    
### Del 6: Prikazovanje podatkov - napredno
- Improving Plot Aesthetics
    - Introduction To The Data
    - Data-Ink Ratio
    - Hiding Tick Marks
    - Hiding Spines
    - Comparing data with multiple plots
- Color, Layout, and Annotations
    - Color
    - Setting Line Color Using RGB
    - Setting Line Width
    - Improve the Layout and Ordering
    - Replacing the Legend With Annotations
- Visualization with pandas
    - df.plot
    - Plotting Version 1: .plot plots the index against every column
    - Plotting Version 2: .plot(x='col1') plots against a single specific column
    - Plotting Version 3: .plot(x='col1', y='col2') plots one specific column against another specific column
- Seaborn
    - Introduction to Seaborn
    - Introduction to the Data Set
    - Creating Histograms In Seaborn
    - Generating A Kernel Density Plot
    - Modifying The Appearance Of The Plots
    - Conditional Plots
    - Adding A Legend

### Del 7: Uvoz podatkov
- Text encoding: ASCII, Unicode, and others
    - Unicode and UTF-8
- Reading and Writing Data with pandas
    - CVS files
        - Primer 1: seaslug.txt
        - Primer 2: FOOD_DES.txt
        - Primer 3: MplsStops.csv
        - Primer 4: iperf.txt
    - JSON files
        - Orient options
        - Primer: ocenas.json
        - Primer: temperatures.json
        - Primer: cities.json
        - Primer: transactions.json
        - Primer: all_hour_geo.json
        - Primer: rates.json
    - Python Pickle Format
    - Excel files
     
### Del 8: Agregacija, združevanje in tranformacija podatkov
- Data Aggregation
    - Introduction to the Data
    - Aggregate Data with Loops
    - GroupBy Operation
        - Creating GroupBy Objects
        - Exploring GroupBy Objects
        - Common Aggregation Methods
        - Aggregating Specific Columns
        - Agg() Method
        - Computing Multiple and Custom Aggregations
    - Pivot Tables
- Combining Data
    - Combining Dataframes with the Concat Function
    - Joining Dataframes with the Merge Function
        - Joining on Columns
        - Left Joins
        - Join on Index
    - Primer: Combine Data and Create a Visualization
- Transforming Data
    - Map and Apply Methods (Element-wise)
    - Applymap Method (Element-wise to Multiple Columns)
    - Apply Method (along an Axis)
    - Melt Function
    - Primer: Aggregate the Data and Create a Visualization
    
### Del 9: Priprava in čiščenje podatkov - napredno
- Working With Strings In Pandas
    - Data
    - Using Apply to Transform Strings
    - Vectorized String Methods
        - Exploring Missing Values with Vectorized String Methods
- Regular Expressions in Pandas
    - The Regular Expression Module
    - Finding Specific Words in Strings
    - Using Regular Expressions to Select Data
    - Import new dataset
    - Quantifiers
    - Character Classes
    - Raw strings
    - Extracting Substrings from a Series
    - Using Flags to Modify Regex Patterns
    - Primer: Create a frequency table of the different capitalizations of SQL
    - Primer: Versions of Python
    - Primer: Extracting URL Parts
        - Using Named Capture Groups
    - Primer: Clean a String Column, Aggregate the Data, and Plot the Results
- Working With Missing Data
    - Introduction
    - Identifying Missing Values
    - Correcting Data Cleaning Errors that Result in Missing Values
    - Visualizing Missing Data
    - Using Data From Additional Sources to Fill in Missing Values
    - Identifying Duplicates Values
    - Correcting Duplicates Values
    - Handle Missing Values by Dropping Columns
    - Analyzing Missing Data
    - Handling Missing Values with Imputation
    - Dropping Rows
- Identifying Hidden Missing Data
    - Primer: Happiness 2015
    - Primer: Diabetes
        - Analyzing missingness percentage
- Andvance Visualization of Missing Data
    - Missingness Patterns
- Handle Missing Values
    - Dropping Rows
    - Imputation Techniques
        - Mean & median imputation
        - Mode and constant imputation
        - Visualize imputations

### Del 10: Timeseries 
- Dates and Times in Python
    - Native Python dates and times: datetime
    - Native Python dates and times: dateutil
- Typed arrays of times: NumPy's datetime64
- Dates and times in pandas: best of both worlds
    - Pandas Time Series: Indexing by Time
    - Pandas Time Series Data Structures
    - Regular sequences
- The data
    - Getting the data
- Time series data structures
- Creating a time series DataFrame
- Time-based indexing
- Visualizing time series data
- Customizing time series plots
- Seasonality
- Frequencies
- Resampling
- Rolling windows
- Trends

### Del 11: Web Scraping
- What Is Web Scraping?
    - Why Web Scraping for Data Science?
- Network complexity
- HTTP
- HTTP in Python: The Requests Library
- HTML and CSS
    - Hypertext Markup Language: HTML
- Using Your Browser as a Development Tool
- The Beautiful Soup Library
- Web APIs
    - Primer uporabe APIja
- Import data from web - pandas
- Web Scraping using pandas
- Primeri
    - Scraping and Visualizing IMDB Ratings
    - Scraping Fast Track data
    
### Del 12: Categorical Data
- Background and Motivation
- Categorical Type in pandas
- Better performance with categoricals
- Categorical Methods
- Example: Using The Pandas Category Data Type
    - Data Preparation
    - Performance
    - Watch Outs
    - General Guidelines
    
### Del 13: Delo s podatkovnimi bazami in SQL
- Introduction to Databases
- Data
- SQLite - Commands
    - Formatting Output
    - Querying the database schema
- Introduction to SQL
    - SELECT
    - Filtering Rows Using WHERE
    - Multiple Filter Criteria Using AND
    - Returning One of Several Conditions With OR
    - Grouping Operators With Parentheses
    - Ordering Results Using ORDER BY
- Work with the SQLite database using Python
    - Connecting to the Database
        - Closing the Database Connection
        - SQLite Python: Creating a New Database
    - Introduction to Cursor Objects and Running a Query
        - Shortcut for Running a Query
        - SQLite Python: Querying Data
    - Fetching a Specific Number of Results
- SQLAlchemy
    - Installation
    - SQLAlchemy version
    - Connecting
        - Database Urls
    - Execute SQL statements
- Working with databases and Pandas
    - Importing data from database
        - read_sql_table
        - read_sql_query
    - Writing a DataFrame to a SQL database
        - to_sql
        - SQL data types
    - Primer: Uvoz podatkov iz CSV dokumenta v SQL bazo
- Dodatna orodja

### Del 14: Procesiranje velikih datasetov - pomnilnik
- Introduction & Data
- Measuring the memory usage of a Pandas DataFrame
    - The Internal Representation of a Dataframe
    - Dataframe Memory Footprint
        - Numbers (int, float) and other fixed-size objects
        - Example: moma dataset - float clomun
        - Object Columns (arbitrarily-sized objects)
    - Getting memory usage by type
- Optimizing Dataframe Memory Footprint
    - Dropping columns
    - Optimizing Numeric Columns with Smaller Subtypes
        - Integer Columns
        - Float Columns
    - Converting To DateTime
    - Converting to Categorical
    - Sparse columns
    - Example: Selecting Types While Reading the Data In
- Processing Dataframes in Chunks
- Analizing big files with Pandas and SQLite
- Vaja: Primer analize velikega dataseta

### Del 15: Procesiranje velikih datasetov - hitrost
- CPU Bound Programs
- I/O Bound Programs
- Optimizing Python Code with pandas
- PRIMER: Pohitritev pandas kode
