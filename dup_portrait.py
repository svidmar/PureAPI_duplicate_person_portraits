import requests
import logging
from tqdm import tqdm

# API configuration
API_URL = "https://xyz.elsevierpure.com/ws/api/persons" # Replace with Pure instance URL
API_KEY = "MY_API_KEY"  # Replace with API key
PAGE_SIZE = 100  # Number of items to fetch per page

# Setup logging
LOG_FILE = "persons_with_multiple_photos.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')

def fetch_persons(offset, size):
    """Fetch a page of persons from the Pure API."""
    try:
        response = requests.get(
            API_URL,
            headers={
                "accept": "application/json",
                "api-key": API_KEY
            },
            params={"offset": offset, "size": size}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error fetching data at offset {offset}: {e}")
        return None

def process_person(person):
    """Check if a person has multiple profile photos with the target URI."""
    photos = person.get("profilePhotos", [])
    matching_photos = [photo for photo in photos if photo.get("type", {}).get("uri") == "/dk/atira/pure/person/personfiles/portrait"]
    if len(matching_photos) > 1:
        logging.info(f"Person {person['uuid']} has {len(matching_photos)} profile photos with the specified URI.")
        return person["uuid"]
    return None

def main():
    # Initial fetch to determine the total number of persons
    initial_response = fetch_persons(0, 1)
    if not initial_response:
        print("Failed to fetch initial data. Exiting.")
        return

    total_count = initial_response.get("count", 0)
    print(f"Total persons to process: {total_count}")

    # Progress bar
    with tqdm(total=total_count, desc="Processing persons") as progress_bar:
        offset = 0
        persons_with_multiple_photos = []

        while offset < total_count:
            response = fetch_persons(offset, PAGE_SIZE)
            if not response:
                print(f"Skipping offset {offset} due to error.")
                offset += PAGE_SIZE
                progress_bar.update(PAGE_SIZE)
                continue

            items = response.get("items", [])
            for person in items:
                result = process_person(person)
                if result:
                    persons_with_multiple_photos.append(result)

            offset += PAGE_SIZE
            progress_bar.update(len(items))

    print(f"Processing complete. {len(persons_with_multiple_photos)} persons found with multiple profile photos.")
    print(f"Check the log file '{LOG_FILE}' for details.")

if __name__ == "__main__":
    main()
