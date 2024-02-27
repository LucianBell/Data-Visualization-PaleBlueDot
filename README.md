![Header image for Pale Blue Dot Hackathon](/header_image.jpg)
==============================

## What is the Pale Blue Dot Visualization Challenge

This challenge was designed to engage data science learners and practitioners in using data to understand and improve quality of life on Earth through analysis and visualization. As detailed below, in this challenge, quality of life on Earth is captured by the Sustainable Development Goals and the data used to understand and track progress towards those goals will be publicly available U.S. Earth observation data.

## What is this project/entry?

Our project is a **visual that shows how climate and public policies affect agriculture in Brazil.** It uses data from **IBGE (Brazilian Institute of Geography and Statistics) and NASA Copernicus** to show **agricultural production, crop health, soil moisture, and temperature in each state of Brazil**. The visual also shows the domino effect of government interventions, which can benefit farmers and consumers by increasing crop resilience, reducing greenhouse gas emissions, and preventing environmental degradation. Our project is motivated by our personal experience with the benefits of PRONAF, a program that offers credit to family farmers.

## Who is in this team?

Short answer:  Amanda Soares, Lucian Bellini, Rian Fiore da Câmara, Thays Costa.
Long answer: We are four people, from three different states, who share a common and challenging reality. We have seen first-hand the difficulties that local farmers face when the weather and other factors damage their crops. When our families go through these crises, they turn to PRONAF(National Program to Strengthen Family Farming), but sometimes it doesn't take into account the damage caused by drought in some regions. That's why we decided to give more power to the people who have been mitigating these problems and helping our families for years. We want to ensure that when the weather thwarts farmers' efforts, they receive the financial support they need.

## What is our goal with this?

The sustainable development goal we hope to promote is zero hunger, which aims to end hunger, achieve food security and improve nutrition, and promote sustainable agriculture. Our project also contributes to other goals, such as clean water and sanitation, and climate action.

## How to run the project?

Enter the command `streamlit run src/visualization/streamlit/main.py`

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io

--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
