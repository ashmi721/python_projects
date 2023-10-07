'''Given a list of dictionaries containing information about books (title, author, year),
 write a function to find the most recent book's title.
'''
book_list = [
    {'title':'Book1','author':'Author1','year':'2000'},
    {'title':'Book2','author':'Author2','year':'2010'},
    {'title':'Book3','author':'Author3','year':'2020'},

]

def find_most_recent_book(books):
    max_year = -10000
    recent_title = ''
    
    for book in books:
        year_str = book.get('year','0')
        # print(year_str)
        try:
            year = int(year_str)
        except ValueError:
            year = 0
            
        if year > max_year: 
           max_year = year
           recent_title = book.get('title','')

    return recent_title       


most_recent_title = find_most_recent_book(book_list)
print(f"The most recent book's title is:",most_recent_title)
