import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

def scrape_jobs(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    section_title="Engineering"
    section = soup.find('h3', string=section_title)
    
    if not section:
        print(f"Could not find section with title: {section_title}")
        return []
    
    # Find all job listings (you'll need to adjust this based on the specific website's HTML structure)
    job_listings = section.find_next_siblings('div', class_='opening')
    
    jobs = []
    for job in job_listings:
        title = job.find('a').text.strip()
        jobs.append({'title': title})
    
    return jobs

def save_to_csv(jobs, filename):
    keys = jobs[0].keys()
    with open(filename, 'w+', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(jobs)

def read_jobs_from_csv(filename):
    jobs = []
    try:
        with open(filename, 'r', newline='', encoding='utf-8') as input_file:
            csv_reader = csv.DictReader(input_file)
            for row in csv_reader:
                jobs.append(row)
        print(f"Successfully read {len(jobs)} job listings from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except csv.Error as e:
        print(f"Error reading CSV file: {e}")
    return jobs

def compare_job_arrays(array1, array2):
    set1 = set(frozenset(d.items()) for d in array1)
    set2 = set(frozenset(d.items()) for d in array2)
    
    only_in_array1 = set1 - set2
    only_in_array2 = set2 - set1
    
    print("Differences found:")
    
    if only_in_array1:
        print("\nNEW JOBS:")
        for job in only_in_array1:
            print(dict(job))
    
    if only_in_array2:
        print("\nJOBS REMOVED:")
        for job in only_in_array2:
            print(dict(job))
    
    if not only_in_array1 and not only_in_array2:
        print("No differences found. The arrays are identical.")


# Main execution
if __name__ == "__main__":
    filename = f"job_openings.csv"
    url = "https://boards.greenhouse.io/anthropic"  # Replace with the actual job board URL
    new_jobs = scrape_jobs(url)
    existing_jobs = read_jobs_from_csv(filename)

    compare_job_arrays(new_jobs, existing_jobs)

    if new_jobs:
        save_to_csv(new_jobs, filename)
        print(f"Scraped {len(new_jobs)} job openings and saved to {filename}")
    else:
        print("No job openings found.")