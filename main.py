def find_path(data, element):
    path = [element]
    while data and element:
        for x, y in data:
            if x == path[-1]:
                path.append(y)
                continue
        return " > ".join(path)


List = [
    ['html', 'java'],
    ['java', 'mahdi'],
    ['mahdi', 'taha'],
    ['taha', 'radin'],
    ['css', 'JavaScript'],
    ['requests', 'python']
]
Element = "html"
print(find_path(List, Element))
