Select Rows and Columns
=======================

.. figure:: crew.png

.. card::
   :shadow: lg

   **Find your Crew**

   As the captain of a high-speed exploration vessel, you rely on your officers to keep everything running smoothly. 
   Your ship’s systems process massive streams of data at incredible speed, and your crew roster is no exception.
   Somewhere in the ship’s data core lies the list of your five trusted officers, but the display panel only shows raw data files.
   Who are the officers serving on your ship?

   To recognize your officers again, you’ll need to load the crew roster :download:`crew.csv` using Polars and inspect the data.

----

Show column names
-----------------

You may want to access column names as a Python list.
This is also useful to check what types the names are.

.. code:: python

   df.columns

----

Select a column
---------------

A single column is returned as a `pd.Series`:

.. code:: python

   df['id']

----

Select multiple columns
-----------------------

Multiple columns require double square brackets.
The inner one is a list of column names:

.. code:: python

   df[['black_spots', 'white_spots']]

----

Select columns by position
--------------------------

The slice() method selects rows by position.
slice(10, 10) returns 10 rows starting from row 10.
The column slice df.columns[1:4] selects columns 2–4, which are then returned using select().

.. code:: python

   df.slice(10,10).select(df.columns[1:4])

----

Select rows by position
-----------------------

You can select rows by position using the slice() method.
The first argument specifies the starting row, and the second argument specifies the number of rows to return.

.. code:: python

   df.slice(10, 10)

----

Select rows by column value (Polars equivalent of index selection)
-------------------------------------------------------------------

In Polars, DataFrames don't have indices like Pandas. Instead, filter rows based on column values directly.
This is useful for selecting rows where a column matches a specific value, e.g.

.. code:: python

   df.filter(pl.col('ears') == 'pink')

----

Filter by value
---------------

This is very powerful selection logic that is applied to all rows simultaneously.

The notation with double square brackets looks a bit weird first.
It is easier to understand if you know the inner expression results in a boolean mask that is used to filter the rows of the `DataFrame`.

.. code:: python

   df.filter(pl.col('ears') == 'pink'))

   df.filter(pl.col('black_spots') < 3)

   df.filter(pl.col('black_spots').is_between(3, 7))

   df.filter((pl.col('black_spots') < 3) & (pl.col('white_spots') > 7))

Note that you have to use the **binary operators** `&`, `|` to combine multiple conditions.
The **logical operators** `and`, `or` will not work.

----

Select random rows
------------------

.. code:: python

   df.sample(7)

----

.. figure:: space_panda.jpeg

Challenge
---------

.. card::
   :shadow: lg

   Select rows from the crew roster :download:`crew.csv` to find your five officers.
   You have a couple of hints:
   
   * all of your officers have **at least 12 white spots**.
   * three of your officers have **exactly 9 black spots**.
   * none of your officers has **white ears** or **black ears**.
   * the **Helmspanda** (responsible for steering the ship) has the **id 247**.
   * the **Data Science Officer** (responsible for DS of course) has **more than 18 white spots. They also have their ears dyed in indigo**.
   * the **Paw Plant** (responsible for the reactor and engines) has more white spots than the Pandalorian.
   * the **Pandalorian** (responsible for weapons and tactics) has an **unknown ear color**. They wear a helmet all the time.
   * the **Bamboo Chef** (responsible for nutrition) has **their ears dyed in chartreuse. They have fewer white spots than the paw plant**.
   
   **Identify all five of them.**

.. dropdown:: How many white spots do your officers have in total?
   :animate: fade-in

   There should be exactly 79.

----

.. dropdown:: How was the crew data generated?
   :animate: fade-in

   Below you find the code to generate the data in :download:`crew.csv`:

   The generator uses ``np.random.seed(42)``, so it is deterministic and reproduces the same file content.

   .. literalinclude:: crew_generator.py
