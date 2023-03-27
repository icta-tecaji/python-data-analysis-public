# Procesiranje velikih datasetov - pomnilnik

## Vsebina
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
    - Processing Chunks
    - Counting Across Chunks
    - Batch Processing
    - Optimizing Performance
    - Counting Unique Values
    - Combining Chunks Using GroupBy
- Analizing big files with Pandas and SQLite
    - Computing Primarily in SQL
    - Computing Primarily in Pandas
    - Reading in SQL Results Using Chunks
- Vaja: Primer analize velikega dataseta
- More file formats

## Viri
- [Tutorial: Using Pandas with Large Data Sets in Python](https://www.dataquest.io/blog/pandas-big-data/)
- [How to handle large datasets in Python with Pandas and Dask](https://towardsdatascience.com/how-to-handle-large-datasets-in-python-with-pandas-and-dask-34f43a897d55)
- [Why is Python so slow?](https://hackernoon.com/why-is-python-so-slow-e5074b6fe55b)
- [Why Python is Slow: Looking Under the Hood](https://jakevdp.github.io/blog/2014/05/09/why-python-is-slow/)
- [Make working with large DataFrames easier, at least for your memory](https://towardsdatascience.com/make-working-with-large-dataframes-easier-at-least-for-your-memory-6f52b5f4b5c4)
- [“Large data” work flows using pandas](https://stackoverflow.com/questions/14262433/large-data-work-flows-using-pandas)
- [Why and How to Use Pandas with Large Data](https://towardsdatascience.com/why-and-how-to-use-pandas-with-large-data-9594dda2ea4c)
- [4 Strategies to Deal With Large Datasets Using Pandas](https://www.codementor.io/guidotournois/4-strategies-to-deal-with-large-datasets-using-pandas-qdw3an95k)
