class Parameters:
    # Initializations
    LOCATION:str = "Germany" 
    RESULTS_WANTED:int = 50
    COUNTRY_INDEED:str = "Germany"
    LEV_ONE_RECENT_DAYS:int = 7
    LEV_TWO_RECENT_DAYS:int = 14
    LEV_THREE_RECENT_DAYS:int = 30
    GEMINI2_MODEL= "google/gemini-2.0-flash-exp:free"

    SEARCH_TERMS: list[str] = [
        '"Azure ML"', '"AI Engineer"', '"data analyst"', '"analytics engineer"', '"Generative AI"', '"ai-engineer"',
        '"language models"', '"language models"', 'NLP', '"machine learning"', '"data analytics"', '"data analysis"', 
        '"data science"', '"large language models"', '"transformer models"', '"natural language generation"',
        '"data wrangling"', '"data preparation"', '"data modeling"', '"data mining"', '"NLP"', '"azure fabric"', 
        '"azure data factory"', '"artificial intelligence engineer"', 
        '"data scientist"', '"machine learning engineer"', '"data engineer"', '"data pipeline"', '"data visualization"',
        '"natural language processing"', '"deep learning"', '"artificial intelligence"', '"AI"', '"big data"', 
        '"RAG"', '"genai"', '"pandas"', '"mlops"', '"seaborn"', '"python"', '"streamlit"', '"langchain"', 
        '"openai"', '"deepseek"', '"ollama"',  '"LlamaIndex"', '"hugging face"',
        #'"pyspark"',  '"transformers"', '"Tensorflow"', '"PyTorch"', '"scikit-learn"', '"ETL"',    
        # '"numpy"', 'plotly', 'gradio', 'mlflow', 'matplotlib',  'bokeh', 'dash', 'shap', 'lime', 
        # '"Computer Science" and "Data Science" and "Data Analysis"'
    ]

    STREAMLIT_FILTERS: list[str] = [ 
        'site', 'state', 'city', 'company', 'lang', 'search_term'
    ]

    JOBS_SELECTED_COLUMNS: list[str] = ['date', 'uuid', 'status', 'title', 'company', 'location', 'lang', 'job_url', 'description']
    
    ROWS_FILTER: list[str] = [
        'praktikant', 'working student', 'werkstudent', 'abschlussarbeit', 'thesis', 
        'praktika', 'intern','internship', 'praktikum', 'dualer student', 'duales studium',
        'ausbildung', 'apprenticeship', 'student', 'aushilfe', 'Masterarbeit', 'bachelorarbeit', 
        'Minijob', 'Masterand', 'bachelorand', 'hilfskraft', 'studentische hilfskraft',
    ]

    COLUMNS_FILTER: list[str] = [
        'date', 'title', 'job_url', 'company', 'location', 'site', 'lang',  # 'job_type', 'job_url_direct',
        'city', 'state', 'description', 'search_term', 'uuid'
    ]

    COMPANY_FILTER: list[str] = [
        'BearingPoint', 'Michael Page', 'adesso SE', 'BridgingIT GmbH', 
        'indivHR', 'Lawrence Harvey', 'indivHR - We 💚 IT Recruiting',
        'univativ GmbH', 'The Stepstone Group', 'ALTEN Consulting Services',
        'SAP', 'Mayflower GmbH', 'Optimus Search', 'Crossover', 'The Recruitment 2.0 Group',
        'Cologne Intelligence', 'Cologne Intelligence GmbH', 'Mayflower',
        'The StepStone Group GmbH', 'TrioTech Recruitment', 'IntaPeople: STEM Recruitment',
        'IntaPeople', 'TrioTech', 'Optimus Search Limited', 'ALTEN Technology',
        'Yellow Brick Road', 'Goodman Masson Deutschland', 'diconium group', 'diconium',
        'U.S. Army', 'ControlExpert GmbH', 'ControlExpert', 'Manning Global AG', 
        'Alexander Thamm GmbH', 'Alexander Thamm', 'Alexander Thamm Consulting',
        'TechBiz Global GmbH', 'TechStarter', 'Mindrift', 
    ]
    
    


    # ALDI Süd
    # merck
    # NielsenIQ
    # Südzucker
    # Haufe Group
    # https://www.linkedin.com/jobs/view/4001979963
    # Döhler Group
    # Deufol SE
    # BAUR-Gruppe
    # DEKRA Germany
    # Grünenthal Group
    # Graf Hardenberg
    


#- Researching, defining and testing the data model to set up our data quality validation pipeline, via intense communication with experts of SAP/CRM systems and product owners. 
#- Data Engineering: developing our in house data engineering and data quality python package (Azure, PySpark, Git, Databricks) 
#- Data Quality Validation through business defined rules (python)
#- Data Visualisation of results (PowerBI) and maintenance of our dashboards
#- Coordinating activities with stakeholders in absence of our PO