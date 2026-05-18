import requests

def search_book(title: str) -> dict:
    """
    Returns basic information about a book

    Args: 
        Title of the book

    Return:
        A dictionary with the title, author and publication year of the book.
    """
    try:
        resp = requests.get(
            "https://openlibrary.org/search.json",
            params={
                "title": title,
                "limit": 1,
                "fields": "title,author_name,first_publish_year,isbn,number_of_pages_median,subject,cover_i,key"
            },
            timeout=8
        )
        resp.raise_for_status()
        docs = resp.json().get("docs", [])

        if not docs:
            return {"status": "not_found", "title": title}

        doc = docs[0]
        return {
            "status": "found",
            "title": doc.get("title"),
            "authors": doc.get("author_name", [])[0],
            "first_published": doc.get("first_publish_year"),
            "isbns": doc.get("isbn", [])[:3],
            "pages": doc.get("number_of_pages_median"),
            "subjects": doc.get("subject", [])[:5],
            "cover_url": (
                f"https://covers.openlibrary.org/b/id/{doc['cover_i']}-M.jpg"
                if doc.get("cover_i") else None
            ),
            "ol_url": f"https://openlibrary.org{doc['key']}" if doc.get("key") else None,
        }

    except requests.RequestException as e:
        return {"status": "error", "message": str(e)}
    
def search_author_id(author_name: str) -> str: 
    """
    Returns the id of a certain author 

    Args: 
        Name of the author 

    Return:
        A str with the id of the author 
    """
    try: 
        resp = requests.get(
            "https://openlibrary.org/search.json",
            params={
                "author": author_name,
                "sort": "new",
                "fields": "author_name, author_key"
            },
            timeout=8
        )
        resp.raise_for_status()
        docs = resp.json().get("docs", [])

        if not docs:
            return {"status": "not_found", "author": author_name}

        doc = docs[0]
        author_id = doc.get("author_key")[0]

        return author_id
    
    except requests.RequestException as e:
        return {"status": "error", "message": str(e)}
    

def search_author_works(author_id: str) -> dict: 
    """
    Returns the books of a certain author 

    Args: 
        an str of the author id 

    Return:
        A dictionary with the works of the author 
    """

    author_id = author_id.strip()
    url = f"https://openlibrary.org/authors/{author_id}/works.json"

    try:
        resp = requests.get(
            url,
            timeout=8,
        )
        resp.raise_for_status()

        return resp
    
    except requests.RequestException as e:
        return {"status": "error", "message": str(e)}
    
