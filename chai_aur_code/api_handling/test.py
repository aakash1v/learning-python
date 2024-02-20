import requests




def random_book():
    url = "https://api.freeapi.app/api/v1/public/books/39"
    response = requests.get(url)
    data = response.json()
    book_data= data["data"]

    if data["success"]==True and "data" in data:
        title = book_data["volumeInfo"]["title"]
        author = book_data["volumeInfo"]["authors"]
        desc = book_data["volumeInfo"]["description"]
        pagecount = book_data["volumeInfo"]["pageCount"]
        return (title,author,desc,pagecount)
    else:
        raise Exception("Failed to fetch book  information or data  ....")

def main():
    try:
        title,author,desc,pagecount = random_book()
        print(f"Title : {title}\nAuthor : {author}\nDescription : {desc}\nPageCount : {pagecount}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()