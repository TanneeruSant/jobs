import time
from jobspy import scrape_jobs
import pandas as pd

search_terms = ['Azure ML', 'python', 'data analyst', 'analytics engineer', 'Generative AI', 'RAG'
                'data scientist', 'pyspark', 'data visualization']

#search_terms = ['java']
# Indeed
df_jobs = []
#old_data = pd.read_csv('jobs.csv')


def collect_data():
    for search_term in search_terms:
        jobs = scrape_jobs(
            site_name=["indeed"],
            search_term=search_term,
            location="Germany",
            results_wanted=80,
            country_indeed='Germany'  # only needed for indeed / glassdoor
        )
        jobs['search_term'] = search_term
        df_jobs.append(jobs)
        time.sleep(30)

    # Linkedin
    for search_term in search_terms:
        jobs = scrape_jobs(
            site_name=["linkedin"],
            search_term=search_term,
            location="Germany",
            results_wanted=40,
            country_indeed='Germany'  # only needed for indeed / glassdoor
        )
        jobs['search_term'] = search_term
        df_jobs.append(jobs)
        time.sleep(30)

    # Linkedin
    for search_term in search_terms:
        jobs = scrape_jobs(
            site_name=["glassdoor"],
            search_term=search_term,
            location="Germany",
            results_wanted=40,
            country_indeed='Germany'  # only needed for indeed / glassdoor
        )
        jobs['search_term'] = search_term
        df_jobs.append(jobs)
        time.sleep(30)

    merged_df = pd.concat(df_jobs, ignore_index=True)
    #all_jobs = pd.concat([old_data,merged_df], ignore_index=True)
    all_jobs = merged_df
    all_jobs =all_jobs.drop_duplicates()
    all_jobs.to_parquet('jobs.parquet')
    #all_jobs.to_csv('jobs.csv', index=False)


def main():
    collect_data()


if __name__ == "__main__":
    main()