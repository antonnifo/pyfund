import sys
from urllib.request import urlopen

def fetch_words(url):
    """fetch a list of words from URL.
    
    Args:
        url: the url of UTF-8 text document.

    Returns:
        a list of string containing the words from the documents. 

    """

    with urlopen(url) as story:
        story_words = []
        for line in story:
            line_words = line.decode('utf-8').split()
            for word in line_words:
                    story_words.append(word)
    return story_words


def print_items(items):
        """Iterate over an iterable.
    
        Args:
                items: any iterable object.

        Returns:
                prints all items on the iterable. 
            
        """   
        for item in items:
                print(item)
            


def main(url):
    """call fetch_words and print_items functions.
    
    Args:
        url: the url of UTF-8 text document.

    Returns:
        prints all items from the iterable.        
    """        
    words =  fetch_words(url)
    print_items(words) 

if __name__ == "__main__":
    main(sys.argv[1])
