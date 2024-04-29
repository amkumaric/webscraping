from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from collections import Counter
import requests

url = 'http://quotes.toscrape.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}

req = Request(url, headers=headers)
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage, 'html.parser')

print(soup.title.text)

def scrape_quotes():
    base_url = "http://quotes.toscrape.com/page/{}/"
    authors = []
    quotes = []
    tags = []

    # Scrape the first 10 pages
    for page in range(1, 11):
        url = base_url.format(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            quote_tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            
            quotes.append(text)
            authors.append(author)
            tags.extend(quote_tags)
    
    return authors, quotes, tags

def analyze_data(authors, quotes, tags):
    # Author statistics
    author_counts = Counter(authors)
    most_quotes_author = max(author_counts, key=author_counts.get)
    least_quotes_author = min(author_counts, key=author_counts.get)
    
    # Print author statistics
    print("Author Statistics:")
    print(f"Most Quotes by: {most_quotes_author} with {author_counts[most_quotes_author]} quotes")
    print(f"Least Quotes by: {least_quotes_author} with {author_counts[least_quotes_author]} quotes")
    print("Counts by Author:")
    for author, count in author_counts.items():
        print(f"{author}: {count}")
    
    # Quote analysis
    quote_lengths = [len(quote) for quote in quotes]
    avg_quote_length = sum(quote_lengths) / len(quote_lengths)
    longest_quote = max(quotes, key=len)
    shortest_quote = min(quotes, key=len)
    
    # Print quote analysis
    print("\nQuote Analysis:")
    print(f"Average Length of Quotes: {avg_quote_length} characters")
    print(f"Longest Quote: '{longest_quote}'")
    print(f"Shortest Quote: '{shortest_quote}'")
    
    # Tag analysis
    tag_counts = Counter(tags)
    most_popular_tag = max(tag_counts, key=tag_counts.get)
    total_tags = len(tags)
    
    # Print tag analysis
    print("\nTag Analysis:")
    print(f"Most Popular Tag: {most_popular_tag} with {tag_counts[most_popular_tag]} occurrences")
    print(f"Total Tags Used: {total_tags}")
    print("Tag Counts:")
    for tag, count in tag_counts.items():
        print(f"{tag}: {count}")

    # Visualization using plotly.graph_objects
    # Top 10 authors
    top_authors = author_counts.most_common(10)
    fig_authors = go.Figure(go.Bar(x=[author for author, _ in top_authors], y=[count for _, count in top_authors]))
    fig_authors.update_layout(title='Top 10 Authors by Number of Quotes', xaxis_title='Author', yaxis_title='Number of Quotes')
    fig_authors.show()
    
    # Top 10 tags
    top_tags = tag_counts.most_common(10)
    fig_tags = go.Figure(go.Bar(x=[tag for tag, _ in top_tags], y=[count for _, count in top_tags]))
    fig_tags.update_layout(title='Top 10 Tags', xaxis_title='Tag', yaxis_title='Number of Occurrences')
    fig_tags.show()

authors, quotes, tags = scrape_quotes()
analyze_data(authors, quotes, tags)
