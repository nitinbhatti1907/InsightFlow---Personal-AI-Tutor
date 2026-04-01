from __future__ import annotations

import re
from difflib import get_close_matches
from typing import Any

from app.seed_data import COURSE, TOPICS


TOPIC_MAP = {topic["id"]: topic for topic in TOPICS}
GENERATED_TOPIC_MAP: dict[str, dict[str, Any]] = {}

DOMAIN_KEYWORDS = {
    "python",
    "pandas",
    "numpy",
    "matplotlib",
    "seaborn",
    "jupyter",
    "notebook",
    "dataframe",
    "series",
    "csv",
    "excel",
    "dataset",
    "analysis",
    "analytics",
    "data cleaning",
    "cleaning",
    "missing values",
    "null values",
    "visualization",
    "plot",
    "chart",
    "histogram",
    "boxplot",
    "scatterplot",
    "line plot",
    "bar chart",
    "eda",
    "exploratory",
    "groupby",
    "merge",
    "join",
    "pivot",
    "aggregation",
    "filtering",
    "statistics",
    "correlation",
    "outlier",
    "descriptive statistics",
    "data wrangling",
}

CATEGORY_LIBRARY: dict[str, dict[str, Any]] = {
    "python-basics": {
        "keywords": ["python", "syntax", "loop", "function", "list", "dictionary", "tuple", "set"],
        "learning_objectives": [
            "Understand the Python building blocks used in analysis notebooks",
            "Write small reusable steps for data tasks",
            "Read and debug simple analysis code more confidently",
        ],
        "core_concepts": [
            "Variables and data types",
            "Lists, dictionaries, and loops",
            "Functions for repeated logic",
            "Basic debugging and readable code",
        ],
        "analogy": "Think of Python basics as the grammar you need before writing full analysis stories in code.",
        "examples": [
            "Store column names in a list and loop through them",
            "Write a small function to clean repeated text patterns",
            "Use a dictionary to map short codes to readable labels",
        ],
        "common_mistakes": [
            "Mixing up indentation levels",
            "Writing repeated code instead of a function",
            "Using the wrong data structure for the task",
        ],
        "resources": [
            {
                "title": "Python Tutorial",
                "url": "https://docs.python.org/3/tutorial/",
                "type": "Documentation",
                "summary": "The official tutorial explains Python syntax, control flow, functions, and core data structures clearly.",
            },
            {
                "title": "Real Python - Python Basics",
                "url": "https://realpython.com/learning-paths/python-basics/",
                "type": "Blog / Guided path",
                "summary": "A beginner-friendly route for building Python confidence before heavier data-analysis work.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Which Python structure stores key-value pairs?",
                "options": ["List", "Dictionary", "Tuple", "Set"],
                "correct_index": 1,
                "explanation": "A dictionary stores key-value pairs like {'city': 'Toronto'}.",
            },
            {
                "question": "Why are functions useful in analysis code?",
                "options": [
                    "They remove the need for data",
                    "They make repeated logic reusable",
                    "They automatically plot results",
                    "They replace every loop",
                ],
                "correct_index": 1,
                "explanation": "Functions package repeated logic into a reusable step.",
            },
            {
                "question": "What is a common beginner source of Python errors?",
                "options": ["Wrong indentation", "Too many comments", "Too many print calls", "Using lowercase names"],
                "correct_index": 0,
                "explanation": "Python uses indentation to define code blocks, so incorrect spacing often breaks code.",
            },
        ],
        "learn_more_sections": [
            "How to write small reusable helper functions for notebooks",
            "When to use dictionaries versus lists in analysis work",
            "How to read traceback messages faster while debugging",
        ],
    },
    "numpy": {
        "keywords": ["numpy", "array", "vectorization", "broadcasting", "ndarray"],
        "learning_objectives": [
            "Understand why arrays are used for numerical work",
            "Apply vectorized operations instead of repeated loops",
            "Read array shapes and indexing more confidently",
        ],
        "core_concepts": [
            "NumPy arrays",
            "Vectorization",
            "Array shape and indexing",
            "Aggregations such as mean, sum, min, and max",
        ],
        "analogy": "NumPy arrays are like neatly arranged trays of numbers that can be updated all at once.",
        "examples": [
            "Add a constant to every value in an array",
            "Calculate average weekly sales from a numeric list",
            "Filter values above a threshold without writing a manual loop",
        ],
        "common_mistakes": [
            "Confusing Python lists with NumPy arrays",
            "Ignoring array shape when slicing",
            "Using loops when vectorized operations are simpler",
        ],
        "resources": [
            {
                "title": "NumPy User Guide",
                "url": "https://numpy.org/doc/stable/user/",
                "type": "Documentation",
                "summary": "The official guide explains arrays, indexing, broadcasting, and common mathematical operations.",
            },
            {
                "title": "Kaggle Python Course",
                "url": "https://www.kaggle.com/learn/python",
                "type": "Practice resource",
                "summary": "Short hands-on notebooks help learners connect array operations to real tasks.",
            },
        ],
        "quiz_bank": [
            {
                "question": "What is a major NumPy advantage over plain Python lists for numerical work?",
                "options": ["Automatic charts", "Faster vectorized operations", "No indexing needed", "No imports needed"],
                "correct_index": 1,
                "explanation": "NumPy is optimized for numerical computing and supports vectorized operations.",
            },
            {
                "question": "What does array shape describe?",
                "options": ["File owner", "Data type color", "Array dimensions", "Chart style"],
                "correct_index": 2,
                "explanation": "Shape tells you the dimensions of the array, such as rows and columns.",
            },
            {
                "question": "Which example is vectorized?",
                "options": ["for x in arr: total += x", "arr + 5", "print(arr)", "open('data.csv')"],
                "correct_index": 1,
                "explanation": "Adding directly to an array applies the operation to all elements at once.",
            },
        ],
        "learn_more_sections": [
            "How broadcasting works with different array shapes",
            "When vectorization is clearer than a loop",
            "How NumPy supports pandas and machine learning workflows",
        ],
    },
    "pandas": {
        "keywords": ["pandas", "dataframe", "series", "csv", "column", "row", "iloc", "loc"],
        "learning_objectives": [
            "Load and inspect table-shaped data with confidence",
            "Select rows and columns correctly",
            "Perform common transformation steps using pandas",
        ],
        "core_concepts": [
            "Series and DataFrame",
            "Reading CSV files",
            "Selecting with loc and iloc",
            "Filtering and creating new columns",
        ],
        "analogy": "A pandas DataFrame is like a programmable spreadsheet that responds to code instead of manual clicking.",
        "examples": [
            "Load a CSV file and inspect the first rows",
            "Filter records that meet a condition",
            "Create a new calculated column from two existing columns",
        ],
        "common_mistakes": [
            "Using iloc when label-based selection is needed",
            "Ignoring column data types before analysis",
            "Forgetting that chained operations can become hard to read",
        ],
        "resources": [
            {
                "title": "Pandas Getting Started",
                "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html",
                "type": "Documentation",
                "summary": "The official intro tutorials cover reading data, selecting columns, filtering, and transforming tables.",
            },
            {
                "title": "Real Python - pandas Learning Path",
                "url": "https://realpython.com/learning-paths/pandas-data-science/",
                "type": "Blog / Guided path",
                "summary": "A practical set of pandas explanations with strong coding examples and intuition.",
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
                "question": "Why inspect data types before analysis?",
                "options": [
                    "To improve color themes",
                    "Wrong types can produce incorrect calculations",
                    "Pandas requires all strings",
                    "It reduces row count",
                ],
                "correct_index": 1,
                "explanation": "A numeric column stored as text can break calculations or filtering.",
            },
        ],
        "learn_more_sections": [
            "How groupby summarizes categories",
            "When loc is clearer than chained indexing",
            "How to design readable transformation pipelines",
        ],
    },
    "cleaning": {
        "keywords": ["clean", "cleaning", "missing", "null", "duplicate", "imputation", "outlier", "wrangling"],
        "learning_objectives": [
            "Recognize common data-quality issues before analysis",
            "Choose safe first steps for handling missing or inconsistent values",
            "Document cleaning choices so results stay explainable",
        ],
        "core_concepts": [
            "Missing values",
            "Duplicates and inconsistent formats",
            "Type conversion and validation",
            "Documenting assumptions during cleaning",
        ],
        "analogy": "Data cleaning is like preparing ingredients before cooking, because weak preparation affects every step after it.",
        "examples": [
            "Check which columns contain missing values",
            "Standardize messy text labels before grouping",
            "Remove or review duplicated records before summarizing results",
        ],
        "common_mistakes": [
            "Dropping rows too early without understanding why values are missing",
            "Changing formats without checking downstream effects",
            "Cleaning the data but not explaining the decisions made",
        ],
        "resources": [
            {
                "title": "Pandas Missing Data Guide",
                "url": "https://pandas.pydata.org/docs/user_guide/missing_data.html",
                "type": "Documentation",
                "summary": "The official pandas guide explains missing-value detection, filling, and safe handling patterns.",
            },
            {
                "title": "Kaggle Data Cleaning Course",
                "url": "https://www.kaggle.com/learn/data-cleaning",
                "type": "Practice resource",
                "summary": "Short lessons and notebooks show how to handle missing values, duplicates, and inconsistent text fields.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Why should missing values be checked before running analysis?",
                "options": [
                    "They always improve accuracy",
                    "They can distort calculations or hide data-quality problems",
                    "They automatically create charts",
                    "They convert text to numbers",
                ],
                "correct_index": 1,
                "explanation": "Missing values can change counts, averages, and patterns if they are ignored.",
            },
            {
                "question": "Which pandas method is commonly used to detect missing values?",
                "options": ["df.isnull()", "df.plot()", "df.rename()", "df.sort_values()"],
                "correct_index": 0,
                "explanation": "df.isnull() helps identify missing values across the DataFrame.",
            },
            {
                "question": "What is a safer first step before dropping rows with missing data?",
                "options": [
                    "Delete everything immediately",
                    "Inspect which columns and how many rows are affected",
                    "Convert all values to strings",
                    "Only change the chart type",
                ],
                "correct_index": 1,
                "explanation": "You should first understand where the missing values occur and how much data would be lost.",
            },
        ],
        "learn_more_sections": [
            "When to fill missing values versus remove records",
            "How to document cleaning choices in reports and notebooks",
            "How outlier checks and type validation support trustworthy analysis",
        ],
    },
    "grouping": {
        "keywords": ["groupby", "aggregate", "aggregation", "pivot", "summarize", "summary", "merge", "join"],
        "learning_objectives": [
            "Summarize records by category or group",
            "Understand when joins are needed before aggregation",
            "Read grouped output clearly and explain what it means",
        ],
        "core_concepts": [
            "groupby and aggregation",
            "Common summary metrics such as count, mean, sum",
            "Merge and join basics",
            "Pivot-style summaries",
        ],
        "analogy": "Grouping is like sorting many receipts into labeled stacks before calculating totals for each stack.",
        "examples": [
            "Find total sales by city",
            "Calculate average marks by department",
            "Merge customer and order tables before creating summaries",
        ],
        "common_mistakes": [
            "Grouping before checking duplicate records",
            "Using the wrong join type and losing important rows",
            "Reporting totals without explaining the grouping key",
        ],
        "resources": [
            {
                "title": "Pandas Group By: split-apply-combine",
                "url": "https://pandas.pydata.org/docs/user_guide/groupby.html",
                "type": "Documentation",
                "summary": "The official guide explains grouping, aggregation, and transformation patterns in pandas.",
            },
            {
                "title": "Pandas Merge, Join, and Concatenate",
                "url": "https://pandas.pydata.org/docs/user_guide/merging.html",
                "type": "Documentation",
                "summary": "A solid reference for combining tables before grouped analysis or reporting.",
            },
        ],
        "quiz_bank": [
            {
                "question": "What is the main purpose of groupby in pandas?",
                "options": ["To delete columns", "To summarize data by categories", "To create images", "To install packages"],
                "correct_index": 1,
                "explanation": "groupby helps summarize data by one or more categories.",
            },
            {
                "question": "Why might a merge be needed before aggregation?",
                "options": [
                    "To add unrelated fonts",
                    "To combine needed columns from different tables",
                    "To avoid using data",
                    "To disable summaries",
                ],
                "correct_index": 1,
                "explanation": "Merging brings needed information together before you calculate grouped results.",
            },
            {
                "question": "What is a common grouped metric?",
                "options": ["mean", "browser", "folder", "palette"],
                "correct_index": 0,
                "explanation": "mean is one of the standard aggregation metrics used with grouped data.",
            },
        ],
        "learn_more_sections": [
            "How multiple grouping keys change the output structure",
            "When a left join is safer than an inner join",
            "How to communicate grouped results clearly in reports",
        ],
    },
    "visualization": {
        "keywords": ["visualization", "plot", "chart", "graph", "matplotlib", "seaborn", "histogram", "bar", "line", "scatter", "boxplot"],
        "learning_objectives": [
            "Choose a chart that matches the analysis question",
            "Read patterns and communicate them clearly",
            "Avoid common visualization mistakes that confuse the audience",
        ],
        "core_concepts": [
            "Matching chart types to questions",
            "Axis labels and titles",
            "Comparisons, distributions, and trends",
            "Readable styling and interpretation",
        ],
        "analogy": "A chart is like a visual summary sentence, because it should make the main pattern easier to understand immediately.",
        "examples": [
            "Use a bar chart to compare categories",
            "Use a line chart to show change over time",
            "Use a histogram to inspect a distribution",
        ],
        "common_mistakes": [
            "Choosing a chart type that does not fit the question",
            "Missing labels or unclear titles",
            "Adding too much decoration and hiding the message",
        ],
        "resources": [
            {
                "title": "Matplotlib Tutorials",
                "url": "https://matplotlib.org/stable/tutorials/index.html",
                "type": "Documentation",
                "summary": "The official tutorials explain foundational plotting ideas, from line charts to more detailed customization.",
            },
            {
                "title": "Seaborn Tutorials",
                "url": "https://seaborn.pydata.org/tutorial.html",
                "type": "Documentation",
                "summary": "Seaborn makes statistical plotting more accessible and helps create cleaner charts with less code.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Which chart is commonly used to show change over time?",
                "options": ["Line chart", "Pie chart only", "Text file", "Folder tree"],
                "correct_index": 0,
                "explanation": "Line charts are commonly used to show patterns and trends across time.",
            },
            {
                "question": "Why do axis labels matter?",
                "options": ["They make the chart background darker", "They explain what the viewer is looking at", "They remove the data", "They increase file size only"],
                "correct_index": 1,
                "explanation": "Labels help viewers understand what each axis represents.",
            },
            {
                "question": "What is a common visualization mistake?",
                "options": ["Using a clear title", "Choosing a chart that does not match the question", "Adding readable labels", "Checking scale carefully"],
                "correct_index": 1,
                "explanation": "The chart type should fit the question, otherwise the message becomes misleading or unclear.",
            },
        ],
        "learn_more_sections": [
            "How to compare distributions with boxplots and histograms",
            "When seaborn is more convenient than base matplotlib",
            "How to explain chart findings in plain language beneath the figure",
        ],
    },
    "statistics": {
        "keywords": ["statistics", "mean", "median", "mode", "std", "standard deviation", "variance", "correlation", "distribution"],
        "learning_objectives": [
            "Understand descriptive statistics used in exploratory analysis",
            "Interpret center, spread, and relationships between variables",
            "Know where simple summary metrics can be misleading",
        ],
        "core_concepts": [
            "Mean, median, and mode",
            "Variance and standard deviation",
            "Correlation",
            "Distribution awareness",
        ],
        "analogy": "Statistics are like a compact report card for a dataset, because they summarize important patterns without showing every row.",
        "examples": [
            "Compare mean and median for a skewed income column",
            "Measure spread in test scores using standard deviation",
            "Check whether two numeric variables move together using correlation",
        ],
        "common_mistakes": [
            "Using only one metric and ignoring the full distribution",
            "Treating correlation as proof of causation",
            "Ignoring outliers that shift the mean strongly",
        ],
        "resources": [
            {
                "title": "NumPy Statistics Basics",
                "url": "https://numpy.org/doc/stable/reference/routines.statistics.html",
                "type": "Documentation",
                "summary": "Official references for common statistical routines used with numerical arrays.",
            },
            {
                "title": "Khan Academy - Statistics and Probability",
                "url": "https://www.khanacademy.org/math/statistics-probability",
                "type": "Learning resource",
                "summary": "Clear explanations of center, spread, distributions, and interpretation.",
            },
        ],
        "quiz_bank": [
            {
                "question": "Which measure is often less sensitive to extreme outliers?",
                "options": ["Mean", "Median", "Variance", "Range only"],
                "correct_index": 1,
                "explanation": "The median is often more robust to extreme values than the mean.",
            },
            {
                "question": "What does standard deviation describe?",
                "options": ["File format", "Spread of values around the mean", "Chart color", "Database speed"],
                "correct_index": 1,
                "explanation": "Standard deviation measures how spread out the values are around the mean.",
            },
            {
                "question": "Why should correlation be interpreted carefully?",
                "options": ["Because it proves causation", "Because it does not automatically prove causation", "Because it removes outliers", "Because it only works for text"],
                "correct_index": 1,
                "explanation": "Correlation can show association, but it does not by itself prove one variable causes another.",
            },
        ],
        "learn_more_sections": [
            "How skewness affects mean and median interpretation",
            "Why visualizing a distribution helps statistics make more sense",
            "How correlation fits into exploratory analysis instead of final proof",
        ],
    },
    "eda": {
        "keywords": ["eda", "exploratory", "exploration", "inspect", "profiling", "understand dataset"],
        "learning_objectives": [
            "Explore a dataset before drawing conclusions",
            "Use summaries and charts to spot patterns and issues",
            "Build a repeatable first-pass analysis workflow",
        ],
        "core_concepts": [
            "Dataset overview",
            "Data types and missing values",
            "Summary statistics",
            "Quick charts for trends and distributions",
        ],
        "analogy": "EDA is like walking through a new neighborhood before choosing the best route, because you first need to see the landscape.",
        "examples": [
            "Check dataset shape and column types",
            "Summarize numeric columns before deeper modeling",
            "Visualize a few core variables to find patterns or anomalies",
        ],
        "common_mistakes": [
            "Jumping into conclusions before inspecting data quality",
            "Using too many charts without a guiding question",
            "Skipping notes about what patterns were observed",
        ],
        "resources": [
            {
                "title": "Pandas Intro Tutorials",
                "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html",
                "type": "Documentation",
                "summary": "A solid starting point for reading data, inspecting structures, and building first-pass summaries.",
            },
            {
                "title": "Seaborn Tutorial",
                "url": "https://seaborn.pydata.org/tutorial.html",
                "type": "Documentation",
                "summary": "Helpful for creating quick visual checks during exploratory analysis.",
            },
        ],
        "quiz_bank": [
            {
                "question": "What is the main purpose of exploratory data analysis?",
                "options": ["To skip understanding the data", "To understand patterns, quality issues, and useful questions before deeper analysis", "To delete all rows", "To replace every model"],
                "correct_index": 1,
                "explanation": "EDA helps you understand the dataset before making stronger claims or decisions.",
            },
            {
                "question": "Which is a good first EDA step?",
                "options": ["Ignore column types", "Inspect dataset shape and missing values", "Only export to PDF", "Delete all outliers immediately"],
                "correct_index": 1,
                "explanation": "Basic structural checks are an important first step in EDA.",
            },
            {
                "question": "Why combine statistics and charts during EDA?",
                "options": ["Because one view may miss patterns the other can reveal", "Because charts automatically clean data", "Because statistics remove labels", "Because it avoids interpretation"],
                "correct_index": 0,
                "explanation": "Statistics and charts complement each other during exploration.",
            },
        ],
        "learn_more_sections": [
            "How to create a repeatable EDA checklist for assignments",
            "Which charts quickly reveal skew, spread, and outliers",
            "How to turn EDA findings into focused next-step questions",
        ],
    },
    "general": {
        "keywords": [],
        "learning_objectives": [
            "Understand the requested topic inside a Python data-analysis workflow",
            "Connect the topic to practical notebook tasks",
            "Know what to study next after the first explanation",
        ],
        "core_concepts": [
            "Role of the topic in analysis workflow",
            "Common Python tools involved",
            "Typical beginner bottlenecks",
            "Next-step practice ideas",
        ],
        "analogy": "Treat the topic like one station in a longer analysis pipeline, because each station affects the quality of the final answer.",
        "examples": [
            "Connect the topic to a small CSV-based notebook task",
            "Explain where this idea appears in a normal analysis workflow",
            "Use a tiny example before moving to full datasets",
        ],
        "common_mistakes": [
            "Trying to memorize the topic without connecting it to workflow",
            "Skipping small practice examples",
            "Moving ahead without checking whether the result is logically believable",
        ],
        "resources": [
            {
                "title": "Pandas Getting Started",
                "url": "https://pandas.pydata.org/docs/getting_started/intro_tutorials/index.html",
                "type": "Documentation",
                "summary": "A strong general starting point for many data-analysis topics in Python.",
            },
            {
                "title": "Kaggle Micro-Courses",
                "url": "https://www.kaggle.com/learn",
                "type": "Practice resource",
                "summary": "Short guided lessons that help learners practice Python data-analysis ideas quickly.",
            },
        ],
        "quiz_bank": [
            {
                "question": "What is a good first step when learning a new analysis topic?",
                "options": ["Start with a tiny example and connect it to workflow", "Memorize every term without context", "Skip the data", "Only read headings"],
                "correct_index": 0,
                "explanation": "Small examples make the topic easier to understand and apply.",
            },
            {
                "question": "Why is workflow context important in data analysis?",
                "options": ["Because each step affects the trustworthiness of the final result", "Because it changes keyboard layout", "Because it removes the need for Python", "Because it disables feedback"],
                "correct_index": 0,
                "explanation": "Analysis quality depends on how steps connect together, not just isolated definitions.",
            },
            {
                "question": "What usually helps more than rereading alone?",
                "options": ["One small hands-on practice task", "Closing the notebook", "Ignoring errors", "Skipping explanations"],
                "correct_index": 0,
                "explanation": "A short practical task usually deepens understanding faster than passive rereading.",
            },
        ],
        "learn_more_sections": [
            "How to connect the topic to a real notebook task",
            "Which prerequisite ideas should be reviewed first",
            "How to explain the topic in plain language to another learner",
        ],
    },
}


def list_topics() -> list[dict[str, Any]]:
    return [
        {
            "id": topic["id"],
            "title": topic["title"],
            "difficulty": topic["difficulty"],
            "duration": topic["duration"],
            "tags": topic["tags"],
            "learning_objectives": topic["learning_objectives"],
        }
        for topic in TOPICS
    ]


ALL_TOPICS_LABELS = [topic["title"].lower() for topic in TOPICS]
ALL_TOPICS_IDS = [topic["id"] for topic in TOPICS]


def normalize_text(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().lower())


def titleize_query(query: str) -> str:
    cleaned = re.sub(r"\s+", " ", query.strip())
    if not cleaned:
        return "Custom Data Analysis Topic"
    return cleaned[:1].upper() + cleaned[1:]


def in_course_scope(topic_query: str) -> bool:
    lowered = normalize_text(topic_query)
    if any(keyword in lowered for keyword in DOMAIN_KEYWORDS):
        return True

    category_key = detect_category(topic_query)
    return category_key != "general"


def detect_category(topic_query: str) -> str:
    lowered = normalize_text(topic_query)
    best_category = "general"
    best_score = 0

    for category, config in CATEGORY_LIBRARY.items():
        score = sum(1 for keyword in config["keywords"] if keyword in lowered)
        if score > best_score:
            best_score = score
            best_category = category

    return best_category


def build_custom_topic(topic_query: str) -> dict[str, Any]:
    category_key = detect_category(topic_query)
    category = CATEGORY_LIBRARY[category_key]
    title = titleize_query(topic_query)
    topic_id = title

    topic = {
        "id": topic_id,
        "title": title,
        "difficulty": "Adaptive",
        "duration": "15-30 min",
        "tags": sorted({"custom", "data-analysis", "python", *category["keywords"][:4]}),
        "learning_objectives": category["learning_objectives"],
        "core_concepts": category["core_concepts"],
        "starter_explanation": (
            f"{title} is a valid topic inside Data Analysis with Python because it affects how learners explore data, reason about results, or write analysis code. "
            f"The first goal is to understand what it does in the workflow before trying a bigger notebook task."
        ),
        "expanded_explanation": (
            f"{title} should be understood as part of a practical Python analysis workflow, not as an isolated definition. "
            f"A learner should connect it to real tasks such as reading data, cleaning issues, summarizing patterns, or communicating results. "
            f"When the idea is practiced with a small dataset first, it becomes easier to explain, debug, and reuse in assignments."
        ),
        "analogy": category["analogy"],
        "examples": [
            *category["examples"],
            f"Create one small notebook cell that demonstrates {title.lower()} on a sample dataset.",
        ],
        "practice_activity": (
            f"Create a short notebook around {title.lower()}. Use a tiny CSV or DataFrame, apply one relevant step, then explain what changed and why it matters."
        ),
        "common_mistakes": category["common_mistakes"],
        "resources": category["resources"],
        "quiz_bank": category["quiz_bank"],
        "learn_more_sections": [
            *category["learn_more_sections"],
            f"How to explain {title.lower()} clearly in an assignment or class discussion",
        ],
        "category_key": category_key,
        "is_custom": True,
    }

    GENERATED_TOPIC_MAP[topic_id] = topic
    return topic


def get_topic_or_match(topic_id: str | None, topic_query: str | None) -> tuple[dict[str, Any], str | None]:
    if topic_query and topic_query.strip():
        lowered = normalize_text(topic_query)
        for topic in TOPICS:
            tags_text = " ".join(topic["tags"]).lower()
            title_text = topic["title"].lower()
            if lowered in title_text or lowered in tags_text or title_text in lowered:
                return TOPIC_MAP[topic["id"]], topic_query

        choices = ALL_TOPICS_LABELS + ALL_TOPICS_IDS
        match = get_close_matches(lowered, choices, n=1, cutoff=0.45)
        if match:
            matched_value = match[0]
            for topic in TOPICS:
                if matched_value in {topic["title"].lower(), topic["id"]}:
                    return TOPIC_MAP[topic["id"]], topic_query

        if in_course_scope(topic_query):
            return build_custom_topic(topic_query), topic_query

        raise ValueError(
            "That custom topic does not look related to Data Analysis with Python. Try something like missing values, pandas merge, EDA, NumPy arrays, data visualization, correlation, or groupby."
        )

    if topic_id:
        if topic_id in TOPIC_MAP:
            return TOPIC_MAP[topic_id], None
        if topic_id in GENERATED_TOPIC_MAP:
            return GENERATED_TOPIC_MAP[topic_id], None

    return TOPICS[0], topic_query


LEVEL_GUIDANCE = {
    "beginner": {
        "tone": "Use simple explanations, minimal jargon, and one clear example at a time.",
        "depth": "Focus on what the concept is, why it matters, and one safe first practice step.",
    },
    "intermediate": {
        "tone": "Assume the learner already knows the basics and can connect ideas between tools.",
        "depth": "Balance intuition with practical workflow decisions and likely interview or assignment use cases.",
    },
    "advanced": {
        "tone": "Use more precise language and connect the concept to tradeoffs, edge cases, and real workflow quality.",
        "depth": "Go beyond the definition and explain interpretation, limitations, and quality considerations.",
    },
}

STYLE_GUIDANCE = {
    "visual": "Organize the answer so the learner can imagine patterns, tables, charts, or flow clearly.",
    "hands-on": "Make the explanation action-oriented with steps, small tasks, and code-thinking guidance.",
    "reading": "Give a structured explanation with definitions, examples, and concise paragraphs.",
    "exam-prep": "Highlight what a learner should remember, what a professor may ask, and where mistakes happen.",
}

DETAIL_GUIDANCE = {
    "quick": 1,
    "standard": 2,
    "deep": 3,
}


def get_course_overview() -> dict[str, Any]:
    return {**COURSE, "topics_count": len(TOPICS)}


def get_topic_by_id(topic_id: str) -> dict[str, Any]:
    if topic_id in TOPIC_MAP:
        return TOPIC_MAP[topic_id]
    if topic_id in GENERATED_TOPIC_MAP:
        return GENERATED_TOPIC_MAP[topic_id]
    raise KeyError(topic_id)


def _section(title: str, body: str, bullets: list[str] | None = None, accent: str = "info") -> dict[str, Any]:
    return {"title": title, "body": body, "bullets": bullets or [], "accent": accent}


def _build_focus_message(level: str, style: str, detail: str) -> str:
    return (
        f"This response is tailored for a {level} learner with a {style} preference and {detail} depth. "
        f"{LEVEL_GUIDANCE[level]['tone']} {STYLE_GUIDANCE[style]}"
    )


def _build_sections(topic: dict[str, Any], level: str, style: str, detail: str) -> list[dict[str, Any]]:
    count = DETAIL_GUIDANCE[detail]

    sections = [
        _section(
            "What this topic means",
            topic["starter_explanation"] if count == 1 else topic["expanded_explanation"],
            [topic["analogy"]],
            "primary",
        ),
        _section(
            "Why it matters in Data Analysis with Python",
            (
                f"In this course, {topic['title']} matters because it supports practical analysis tasks like cleaning data, "
                f"summarizing patterns, or communicating findings. {LEVEL_GUIDANCE[level]['depth']}"
            ),
            topic["learning_objectives"],
            "success",
        ),
        _section(
            "Core concepts to focus on",
            (
                f"Start with the most important building blocks before trying bigger projects. "
                f"{STYLE_GUIDANCE[style]}"
            ),
            topic["core_concepts"],
            "warning",
        ),
    ]

    if count >= 2:
        sections.append(
            _section(
                "Simple examples",
                "Use these examples to connect the idea to realistic beginner-to-intermediate analysis work.",
                topic["examples"],
                "secondary",
            )
        )
        sections.append(
            _section(
                "Practice task",
                topic["practice_activity"],
                [
                    "Try the task with a tiny dataset first.",
                    "Explain your logic in comments or notes.",
                    "Check if your result is logically believable before finishing.",
                ],
                "primary",
            )
        )

    if count >= 3:
        sections.append(
            _section(
                "Common mistakes and bottlenecks",
                "These are the points where learners usually get stuck and where educators can adapt support quickly.",
                topic["common_mistakes"],
                "danger",
            )
        )
        sections.append(
            _section(
                "How an educator can use this",
                (
                    "An instructor can use this generated explanation as a fresh supplementary explanation, then use the quiz score, learner feedback, and repeated topic demand "
                    "to identify whether the topic needs more examples, a slower pace, or stronger prerequisite review."
                ),
                [
                    "Track which topics learners request most",
                    "Compare ratings and quiz scores to spot difficult topics",
                    "Add targeted exercises when the same bottleneck keeps appearing",
                ],
                "success",
            )
        )

    return sections


def generate_learning_content(
    topic_id: str | None,
    topic_query: str | None,
    proficiency_level: str,
    learning_style: str,
    detail_mode: str,
    include_resources: bool,
    include_quiz: bool,
) -> dict[str, Any]:
    topic, matched_from_query = get_topic_or_match(topic_id, topic_query)
    sections = _build_sections(topic, proficiency_level, learning_style, detail_mode)

    resources = topic["resources"] if include_resources else []
    quiz = []
    if include_quiz:
        quiz = [
            {
                "question": item["question"],
                "options": item["options"],
                "explanation": item["explanation"],
            }
            for item in topic["quiz_bank"]
        ]

    return {
        "topic_id": topic["id"],
        "topic_title": topic["title"],
        "matched_from_query": matched_from_query,
        "focus_message": _build_focus_message(proficiency_level, learning_style, detail_mode),
        "sections": sections,
        "resource_summaries": resources,
        "quiz": quiz,
        "next_step_prompt": (
            f"If you want deeper coverage after this first explanation, use Learn More for {topic['title']} to unlock advanced notes, a mini-project, and reflection prompts."
        ),
    }


def generate_learn_more(topic_id: str, proficiency_level: str, learning_style: str) -> dict[str, Any]:
    topic = get_topic_by_id(topic_id)
    deeper_sections = [
        _section(
            "Deeper topics to explore next",
            (
                f"For a {proficiency_level} learner, the next stage is not only understanding {topic['title']} but also using it with confidence in notebooks, assignments, and project reports."
            ),
            topic["learn_more_sections"],
            "primary",
        ),
        _section(
            "How to study this topic more effectively",
            (
                f"Because your preference is {learning_style}, continue with a study method that matches that style instead of only rereading notes."
            ),
            [
                "Rebuild one example from memory",
                "Explain the logic in your own words after coding",
                "Compare your output with an expected business or classroom meaning",
            ],
            "secondary",
        ),
    ]

    mini_project = (
        f"Mini-project idea: Build a short notebook on {topic['title']} using a small CSV dataset. Include loading the data, one transformation or calculation step, "
        f"a short explanation of your result, and one quiz question you would ask another learner."
    )

    reflection_questions = [
        f"What part of {topic['title']} still feels confusing, and why?",
        "Which step would you teach differently if you were the instructor?",
        "What evidence would show that you truly understand this topic instead of only recognizing it?",
    ]

    return {
        "topic_id": topic["id"],
        "topic_title": topic["title"],
        "deeper_sections": deeper_sections,
        "mini_project": mini_project,
        "reflection_questions": reflection_questions,
    }


def resolve_topic_title(topic_id: str) -> str:
    topic = TOPIC_MAP.get(topic_id) or GENERATED_TOPIC_MAP.get(topic_id)
    if topic:
        return topic.get("title", topic_id)
    return topic_id
