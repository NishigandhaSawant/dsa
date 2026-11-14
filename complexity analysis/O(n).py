def find_paper(papers, name):
    for paper in papers:
        if paper == name:
            return True
    return False

papers = [ "anita", "bob", "charlie", "david", "eve"]

search_name = "charlie"
result = find_paper(papers, search_name)

if result:
    print('paper found')
else:
    print('paper not found')