import requests
from bs4 import BeautifulSoup
import csv

URL = "https://www.donneesquebec.ca/foire-aux-questions/"


def crawl_faq():
    # Send a GET request to the URL
    response = requests.get(URL)

    # Check if the request was successful
    if response.status_code == 200:
        # Get the HTML content from the response
        html_content = response.text

        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Find all the question-answer pairs
        qa_pairs = soup.find_all("div", class_="elementor-toggle-item")
        extracted_pairs = []
        # Extract and print the question-answer pairs
        for pair in qa_pairs:
            question = pair.find("a", class_="elementor-toggle-title").text.strip()
            answer = pair.find("div", class_="elementor-tab-content").text.strip()
            extracted_pairs.append((question, answer))
        return extracted_pairs
    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")


def to_csv(data: list[tuple[str, str]]):
    with open("src/misc/faq.csv", "w", newline="", encoding="utf8") as file:
        writer = csv.writer(file)
        writer.writerow(["Question", "Reponse"])
        writer.writerows(data)


def main():
    to_csv(crawl_faq())


if __name__ == "__main__":
    main()
