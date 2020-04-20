# IoT Fundamentals: Analitika podatkov v Python-u (public)

Gradiva tečaja Analitika podatkov v Pythonu

## Vsebina

### Del 1: Uvod v analitiko podatkov in priprava okolja
- Vloga podatkov
- What is Data?
- Data Engineer, Data Analyst, Data Scientist — What’s the Difference?
- Overview of the data science process
- Priprava okolja
- Learning the basics of the Unix shell
- Python
- Anaconda
- Git
- Jupyter Notebooks

### Del 2: Uvod v NumPy
- Understanding Data Types in Python
- How Vectorization Makes Code Faster
- Numpy library
- Introduction to Ndarrays
- Priprava podatkov za delo
- Array Shapes
- Selecting and Slicing Rows and Items from ndarrays
- Selecting Columns and Custom Slicing ndarrays
- Vector Math
- Calculating Statistics For 1D ndarrays
- Calculating Statistics For 2D ndarrays
- Reading CSV files with NumPy
- Datatypes
- Boolean Indexing
- Assigning Values
- Adding Rows and Columns to ndarrays
- Computation on NumPy Arrays: Universal Functions
- Copying Data
- Primer: Which is the most popular airport?
- Primer: Calculating Statistics for Trips on Clean Data

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
