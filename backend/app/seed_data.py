COURSE = {
    "id": "data-analysis-python",
    "title": "Data Analysis with Python Learning Assistant",
    "subtitle": "A course-bounded AI suggestion generator for topic-focused learning, summaries, and quizzes.",
    "description": (
        "This system is intentionally bounded to one course: Data Analysis with Python. "
        "Instead of repeating uploaded lecture notes, it generates fresh learning content, "
        "suggests curated external resources, summarizes them, and builds quiz-based practice."
    ),
    "personas": ["Student", "Educator"],
    "value_points": [
        "Generate new explanations for a requested topic",
        "Recommend curated blogs and summarize them",
        "Adapt to level, learning style, and detail depth",
        "End each learning session with a quiz and feedback",
        "Offer a learn-more expansion after the first answer",
    ],
}

TOPICS = [
    {
        "id": "python-basics-for-data",
        "title": "Python Basics for Data Analysis",
        "difficulty": "Beginner",
        "duration": "45-60 min",
        "tags": ["python", "syntax", "lists", "dictionaries"],
        "learning_objectives": [
            "Understand variables, lists, dictionaries, and loops",
            "Read and transform small data collections",
            "Build confidence before moving into pandas and NumPy",
        ],
        "core_concepts": [
            "Variables and data types",
            "Lists, tuples, dictionaries",
            "Loops and conditional logic",
            "Functions for reusable analysis steps",
        ],
        "starter_explanation": (
            "Python gives data analysts a readable way to load, inspect, clean, and summarize data. "
            "Before using powerful libraries, learners must understand how Python stores values, "
            "loops through records, and groups information in lists and dictionaries."
        ),
        "expanded_explanation": (
            "A strong data analysis workflow starts with simple Python thinking: store values, repeat actions, "
            "and organize records in structured containers. When a learner understands variables, loops, and functions, "
            "they can later understand pandas columns, NumPy arrays, and automated transformations much more easily."
        ),
        "analogy": "Think of Python basics as learning the kitchen tools before cooking a full recipe.",
        "examples": [
            "Count how many students scored above 80 using a loop",
            "Store subject names and marks in a dictionary",
            "Write a function that converts percentages into pass/fail labels",
        ],
        "practice_activity": "Create a small dictionary of five products and prices, then calculate the average price.",
        "common_mistakes": [
            "Mixing list indexes with dictionary keys",
            "Forgetting indentation inside loops and functions",
            "Overwriting variables with the wrong data type",
        ],
        "resources": [
            {
                "title": "Python Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
                "type": "Documentation",
                "summary": "The official tutorial introduces Python syntax, control flow, functions, and data structures in a structured way.",
            },
            {
                "title": "Python Basics for Data Science",
                "url": "https://realpython.com/learning-paths/python-basics/",
                "type": "Blog / Guided path",
                "summary": "A beginner-friendly route for learning core Python ideas that transfer directly into data tasks.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Which Python structure stores key-value pairs?",
                "options": ["List", "Dictionary", "Tuple", "Set"],
                "correct_index": 1,
                "explanation": "A dictionary stores data as key-value pairs, such as {'name': 'Ana'}.",
            },
            {
                "question": "Why are functions useful in data analysis scripts?",
                "options": [
                    "They reduce file size",
                    "They repeat logic in a reusable way",
                    "They replace all loops",
                    "They automatically clean data",
                ],
                "correct_index": 1,
                "explanation": "Functions help you package repeated logic so the same analysis step can be reused cleanly.",
            },
            {
                "question": "What is the most common reason a loop fails in beginner Python code?",
                "options": ["Too many variables", "Wrong indentation", "Too many comments", "Missing import pandas"],
                "correct_index": 1,
                "explanation": "Python relies on indentation to define blocks, so incorrect indentation often breaks loops.",
            },
        ],
        "learn_more_sections": [
            "How list comprehensions simplify repeated transformations",
            "When to use tuples instead of lists",
            "How to design small utility functions for analysis notebooks",
        ],
    },
    {
        "id": "numpy-foundations",
        "title": "NumPy Foundations",
        "difficulty": "Beginner",
        "duration": "60 min",
        "tags": ["numpy", "arrays", "vectorization"],
        "learning_objectives": [
            "Understand arrays and numeric computation",
            "Compare loops with vectorized operations",
            "Perform fast element-wise analysis",
        ],
        "core_concepts": [
            "NumPy arrays",
            "Vectorized computation",
            "Array shape and indexing",
            "Aggregation functions like mean and sum",
        ],
        "starter_explanation": (
            "NumPy is the numeric engine behind many Python data tools. It lets analysts work with arrays efficiently, "
            "especially when they need to calculate statistics, reshape values, or perform repeated mathematical operations."
        ),
        "expanded_explanation": (
            "Instead of writing many slow Python loops, NumPy lets analysts operate on entire arrays at once. "
            "That idea, called vectorization, makes code both shorter and faster. It becomes especially useful when working "
            "with measurements, sensor data, or any structured numerical dataset."
        ),
        "analogy": "NumPy arrays are like organized trays where each slot holds a value in a consistent pattern.",
        "examples": [
            "Compute the average score for an entire class",
            "Add 5 bonus marks to every value in an array",
            "Filter all values above a threshold",
        ],
        "practice_activity": "Create a NumPy array of weekly sales and calculate total, average, min, and max.",
        "common_mistakes": [
            "Confusing Python lists with NumPy arrays",
            "Ignoring array shape when slicing",
            "Using loops when vectorization is simpler",
        ],
        "resources": [
            {
                "title": "NumPy User Guide",
                "url": "https://numpy.org/doc/stable/user/",
                "type": "Documentation",
                "summary": "The official NumPy guide explains arrays, broadcasting, indexing, and common mathematical operations.",
            },
            {
                "title": "NumPy Tutorial",
                "url": "https://www.kaggle.com/learn/python",
                "type": "Practice resource",
                "summary": "Hands-on notebooks help learners see how arrays and calculations work on real data examples.",
            },
        ],
        "quiz_bank": [
            {
                "question": "What is one key advantage of NumPy over plain Python lists for numerical work?",
                "options": ["More comments", "Faster vectorized operations", "Automatic charts", "No need for indexing"],
                "correct_index": 1,
                "explanation": "NumPy is optimized for numerical computing and supports vectorized operations across arrays.",
            },
            {
                "question": "What does array shape tell you?",
                "options": ["The file type", "The data owner", "The dimensions of the array", "The chart style"],
                "correct_index": 2,
                "explanation": "Shape tells you how many rows, columns, or dimensions the array has.",
            },
            {
                "question": "Which operation is vectorized?",
                "options": ["for x in arr: total += x", "arr + 5", "print(arr)", "open('file.csv')"],
                "correct_index": 1,
                "explanation": "Adding a number directly to an array applies the operation to all elements at once.",
            },
        ],
        "learn_more_sections": [
            "Broadcasting with arrays of different shapes",
            "When NumPy is preferred over Python loops",
            "How arrays connect to pandas and machine learning workflows",
        ],
    },
    {
        "id": "pandas-core",
        "title": "Pandas for Tabular Data",
        "difficulty": "Intermediate",
        "duration": "75 min",
        "tags": ["pandas", "dataframe", "csv", "series"],
        "learning_objectives": [
            "Load and inspect tabular data with pandas",
            "Select rows and columns confidently",
            "Perform filtering and transformation steps",
        ],
        "core_concepts": [
            "Series and DataFrame",
            "Reading CSV files",
            "Selecting with loc and iloc",
            "Filtering and creating new columns",
        ],
        "starter_explanation": (
            "Pandas is the most common library for handling table-shaped data in Python. "
            "It allows analysts to read files, inspect columns, filter records, create calculated fields, and summarize data quickly."
        ),
        "expanded_explanation": (
            "A pandas DataFrame acts like a smart spreadsheet inside Python. It gives analysts a structured way to work with rows, columns, data types, "
            "missing values, and calculations. Because real-world datasets are rarely clean, pandas becomes the core tool for practical data analysis work."
        ),
        "analogy": "A DataFrame is like a programmable spreadsheet that responds to code instead of manual clicking.",
        "examples": [
            "Load a CSV file and inspect the first five rows",
            "Filter all customers with purchases above 100",
            "Create a revenue column from price multiplied by quantity",
        ],
        "practice_activity": "Load a small CSV dataset and create a new column called total_cost using quantity and unit_price.",
        "common_mistakes": [
            "Using iloc when labels are needed",
            "Forgetting that operations may return a copy",
            "Ignoring column data types before analysis",
        ],
        "resources": [
            {
                "title": "Pandas Getting Started",
                "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html",
                "type": "Documentation",
                "summary": "The official intro tutorials walk through reading data, selecting columns, filtering, and transforming tables.",
            },
            {
                "title": "Real Python - pandas Tutorials",
                "url": "https://realpython.com/learning-paths/pandas-data-science/",
                "type": "Blog / Guided path",
                "summary": "A practical set of pandas explanations with a strong focus on real coding examples and intuition.",
            },
        ],
        "quiz_bank": [
            {
                "question": "What is a pandas DataFrame best described as?",
                "options": ["A charting library", "A tabular data structure", "A database server", "A Python loop"],
                "correct_index": 1,
                "explanation": "A DataFrame stores tabular data in rows and columns.",
            },
            {
                "question": "Which function commonly loads CSV data into pandas?",
                "options": ["pd.load_csv()", "pd.open()", "pd.read_csv()", "pd.file()"],
                "correct_index": 2,
                "explanation": "pd.read_csv() is the standard pandas function for reading CSV files.",
            },
            {
                "question": "Why should you inspect data types before analyzing a DataFrame?",
                "options": [
                    "To improve color themes",
                    "Because wrong types can produce incorrect calculations",
                    "Because pandas requires all strings",
                    "To reduce row count",
                ],
                "correct_index": 1,
                "explanation": "A numeric column stored as text can break calculations or filtering.",
            },
        ],
        "learn_more_sections": [
            "Using groupby to summarize categories",
            "Difference between loc and iloc with simple examples",
            "How to chain filtering and new-column creation cleanly",
        ],
    },
    {
        "id": "data-cleaning",
        "title": "Data Cleaning and Preparation",
        "difficulty": "Intermediate",
        "duration": "75-90 min",
        "tags": ["cleaning", "missing-values", "duplicates", "transformation"],
        "learning_objectives": [
            "Identify dirty or inconsistent data",
            "Handle missing values, duplicates, and formatting issues",
            "Prepare a dataset for analysis and visualization",
        ],
        "core_concepts": [
            "Missing values",
            "Duplicates",
            "Standardizing formats",
            "Type conversion and outlier awareness",
        ],
        "starter_explanation": (
            "Real datasets usually contain missing values, duplicates, inconsistent labels, and formatting problems. "
            "Data cleaning is the step where analysts make the dataset trustworthy enough for meaningful analysis."
        ),
        "expanded_explanation": (
            "Data cleaning is not just about removing bad rows. It is about deciding how to treat incomplete, inconsistent, and unusual data so that the final analysis matches reality as closely as possible. "
            "Good cleaning decisions improve every chart, metric, and model that comes later."
        ),
        "analogy": "Cleaning data is like preparing ingredients before cooking. If the ingredients are wrong, the final dish will also be wrong.",
        "examples": [
            "Fill missing ages with a median value",
            "Remove duplicate customer records",
            "Convert date strings into true datetime values",
        ],
        "practice_activity": "Take a messy dataset and create a checklist for missing values, duplicates, and type fixes before any analysis.",
        "common_mistakes": [
            "Dropping rows too quickly without checking impact",
            "Using a mean for strongly skewed data",
            "Ignoring inconsistent text labels like 'NY' and 'New York'",
        ],
        "resources": [
            {
                "title": "Pandas Missing Data Guide",
                "url": "https://pandas.pydata.org/docs/user_guide/missing_data.html",
                "type": "Documentation",
                "summary": "The official guide explains detecting, filling, and analyzing missing values in pandas.",
            },
            {
                "title": "Data Cleaning with Python",
                "url": "https://realpython.com/python-data-cleaning-numpy-pandas/",
                "type": "Blog",
                "summary": "A practical explanation of common cleaning operations with Python examples and real data intuition.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Why is data cleaning important before visualization?",
                "options": ["It changes the chart colors", "It prevents misleading results", "It removes all rows", "It replaces Python"],
                "correct_index": 1,
                "explanation": "If the underlying data is inconsistent or incomplete, the visualization can be misleading.",
            },
            {
                "question": "Which issue is a formatting inconsistency?",
                "options": ["Missing value", "Duplicate row", "'CA' and 'California' used in the same column", "A numeric mean"],
                "correct_index": 2,
                "explanation": "Those two labels may refer to the same category but are stored differently.",
            },
            {
                "question": "What is one risk of dropping every row with a missing value?",
                "options": ["You may lose too much useful data", "The file becomes larger", "Charts stop working forever", "Python becomes slower"],
                "correct_index": 0,
                "explanation": "Dropping all missing rows can remove important information and bias the dataset.",
            },
        ],
        "learn_more_sections": [
            "Strategies for imputing missing values",
            "When to remove outliers versus keep them",
            "How cleaning decisions should be documented for reproducibility",
        ],
    },
    {
        "id": "eda-visualization",
        "title": "Exploratory Data Analysis and Visualization",
        "difficulty": "Intermediate",
        "duration": "90 min",
        "tags": ["eda", "matplotlib", "seaborn", "visualization"],
        "learning_objectives": [
            "Use descriptive statistics to understand a dataset",
            "Choose suitable charts for different variables",
            "Explain trends, patterns, and outliers clearly",
        ],
        "core_concepts": [
            "Distribution analysis",
            "Categorical and numeric plots",
            "Correlation awareness",
            "Storytelling with charts",
        ],
        "starter_explanation": (
            "Exploratory Data Analysis, or EDA, helps analysts understand what is inside a dataset before making strong conclusions. "
            "It combines summary statistics with visual inspection to reveal patterns, relationships, and unusual values."
        ),
        "expanded_explanation": (
            "EDA is where analysts move from raw data to understanding. Histograms, bar charts, scatter plots, and box plots help reveal spread, skew, relationships, and outliers. "
            "A good analyst does not just draw charts; they explain what each chart means and what decisions it supports."
        ),
        "analogy": "EDA is like walking through a new city before choosing the best route. You observe first, then decide.",
        "examples": [
            "Use a histogram to study exam score distribution",
            "Use a scatter plot to inspect relationship between study time and marks",
            "Use a box plot to identify outliers in monthly sales",
        ],
        "practice_activity": "Pick one numeric and one categorical column, then justify which charts best communicate their patterns.",
        "common_mistakes": [
            "Using the wrong chart for the data type",
            "Adding too many colors or visual clutter",
            "Describing a pattern without checking scale or outliers",
        ],
        "resources": [
            {
                "title": "Matplotlib Tutorials",
                "url": "https://matplotlib.org/stable/tutorials/index.html",
                "type": "Documentation",
                "summary": "The official Matplotlib tutorials explain how to build charts from simple to advanced levels.",
            },
            {
                "title": "Seaborn Tutorial",
                "url": "https://seaborn.pydata.org/tutorial.html",
                "type": "Documentation",
                "summary": "Seaborn helps create cleaner statistical visualizations with less code and strong defaults.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Which chart is often used to inspect the distribution of a numeric variable?",
                "options": ["Histogram", "Pie chart", "Flowchart", "Tree map"],
                "correct_index": 0,
                "explanation": "A histogram shows how numeric values are distributed across ranges.",
            },
            {
                "question": "What is a common purpose of a scatter plot?",
                "options": ["Show code syntax", "Inspect relationship between two numeric variables", "Store text labels", "Replace missing values"],
                "correct_index": 1,
                "explanation": "Scatter plots help you examine whether two numeric variables move together in some pattern.",
            },
            {
                "question": "Why is EDA done before final conclusions?",
                "options": ["To avoid understanding the data", "To explore patterns and potential issues first", "To skip cleaning", "To remove all features"],
                "correct_index": 1,
                "explanation": "EDA helps analysts build understanding before they report or model anything important.",
            },
        ],
        "learn_more_sections": [
            "How to match chart choice to question type",
            "Reading box plots without confusion",
            "Turning EDA findings into short written insights",
        ],
    },
    {
        "id": "statistics-for-analysis",
        "title": "Statistics for Data Analysis",
        "difficulty": "Advanced",
        "duration": "90-120 min",
        "tags": ["statistics", "mean", "variance", "correlation", "sampling"],
        "learning_objectives": [
            "Interpret descriptive statistics with confidence",
            "Understand variability and relationships",
            "Use statistical thinking to support analysis decisions",
        ],
        "core_concepts": [
            "Mean, median, mode",
            "Variance and standard deviation",
            "Correlation versus causation",
            "Sampling and bias awareness",
        ],
        "starter_explanation": (
            "Statistics helps analysts move from raw numbers to meaningful interpretation. "
            "Measures like mean and standard deviation summarize central tendency and spread, while correlation helps inspect relationships between variables."
        ),
        "expanded_explanation": (
            "Data analysis becomes stronger when numerical summaries are interpreted correctly. "
            "The mean can describe a typical value, but skewed data might make the median more appropriate. Standard deviation gives a sense of spread, and correlation can suggest relationships, though not direct cause."
        ),
        "analogy": "Statistics is like the dashboard of a car - it does not tell the whole journey, but it gives critical signals about performance.",
        "examples": [
            "Compare mean and median income in a skewed dataset",
            "Use standard deviation to compare consistency between two classes",
            "Interpret a positive correlation between study hours and scores",
        ],
        "practice_activity": "Given two small datasets, explain which measure of center is more reliable and why.",
        "common_mistakes": [
            "Treating correlation as proof of causation",
            "Ignoring outliers when interpreting averages",
            "Using a mean when the distribution is heavily skewed",
        ],
        "resources": [
            {
                "title": "Python Statistics Fundamentals",
                "url": "https://realpython.com/python-statistics/",
                "type": "Blog",
                "summary": "A practical explanation of descriptive statistics and how to compute them in Python.",
            },
            {
                "title": "SciPy Statistics Tutorial",
                "url": "https://docs.scipy.org/doc/scipy/tutorial/stats.html",
                "type": "Documentation",
                "summary": "The SciPy tutorial introduces statistical functions and the reasoning behind them.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Which measure is less affected by strong outliers?",
                "options": ["Mean", "Median", "Standard deviation", "Variance"],
                "correct_index": 1,
                "explanation": "The median is more robust because it depends on order, not the size of extreme values.",
            },
            {
                "question": "What does standard deviation describe?",
                "options": ["The file format", "How spread out values are", "The chart title", "The number of categories"],
                "correct_index": 1,
                "explanation": "Standard deviation measures how much values vary around the mean.",
            },
            {
                "question": "What is the safest interpretation of correlation?",
                "options": ["One variable definitely causes the other", "The variables may move together", "The data is clean", "The sample is perfect"],
                "correct_index": 1,
                "explanation": "Correlation suggests association, not guaranteed causation.",
            },
        ],
        "learn_more_sections": [
            "Choosing between mean and median in skewed data",
            "Reading variance and standard deviation in plain language",
            "Explaining correlation responsibly in reports",
        ],
    },
]
