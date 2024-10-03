# Data Analysis and Visualization in Python
Python is a powerful tool nowadays used as industry standard for data science. It is also relatively easy to use. This tutorial is by no means an exhaustive set of usecases, its purpose is merely to demonstrate some of the many useful features of python and its libraries. In the following paragraphs we will learn how to load, process and visualise our data with some standard libraries like:

1. **Numpy** - Array (vectors, matrices, etc.) manipulation - addition, multiplication and other operations between arrays, applying functions to arrays and much more,

2. **Matplotlib** - plotting and saving images of many kinds,

3. **Scipy** - fitting, extremization of functions, statistics, etc.,

4. **Pandas** - data input and output.

Sometimes when many files spread across several directories are used, **Pathlib** can be very useful for their management. The general structure of a python file will look the following way:


## Loading data from files 
Depending on the complexity of our dataset, several approaches can be used. Rarely ever is the standard python *open()* function an optimal choice. When a simple csv file with only number inputs is to be loaded, *numpy.genfromtxt()* is a good option. It converts space separated data into a numpy array which can then be further manipulated. For larger datasets or more complex datatypes pandas offers several read-type functions (among which *read_csv()* is an option as well). Let's now try loading a simple shopping list.

```python
--8<-- "python_tutorial/groceries.py"
```
As you can see all dependencies are imported at the beginning of the document, then function definitions are implemented and last comes the main body of the code (in this case the executing if statement). The output of the above code is the following:

???+ success "Output"
    ```
    ['chleb', 'mleko', 'vejce', 'maslo', 'jablka', 'banany', 'rajcata', 'paprika', 'kureci', 'testoviny'] 1310
    ```

## Plotting data
Now let's try a larger dataset. For our training data we can use i.e. the average temperature in the Czech Republic in the last ~25 years. Loading is the same as before 