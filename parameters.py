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
        'guidewire',
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
