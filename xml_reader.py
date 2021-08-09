
"""A module for Slate article selections. 

Attributes:
    None.
"""

import requests
import feedparser


article = feedparser.parse("https://slate.com/feeds/all.rss")


def article_selection():
    """Showcase Slate's article listing and prompt the chosen article link.

    Args:
        None.

    Returns:
        the URL link of the article number selected by the user.
    """
    for i in range(len(article.entries)):
        print(f"{i}. {article.entries[i].title}: {article.entries[i].description}")
    
    usernum = input("Enter a article number: ")
    usernum_m = int(usernum)
    return f"You can see that article at {article.entries[usernum_m].link}"


def main():
    """the main functionality of the Slate article selections module.

    Args:
        None.

    Returns:
        None.
    """
    print(article_selection())
    user_enter = input("Enter yes to continue (no to end program): ")
    if user_enter == "yes":
        print(article_selection())
    elif user_enter == "no":
        exit()


if __name__ == "__main__":
    main()
    
    
    

