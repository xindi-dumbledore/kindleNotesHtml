from bs4 import BeautifulSoup
html_file = "notes.html"
with open(html_file, 'r') as fp:
    htmls = fp.read()

soup = BeautifulSoup(htmls, 'html.parser')
all_divs = soup.find_all('div')


lines = []
for info in soup.find_all(["h2", "div"]):
    if info.name == "h2":  # chapter
        lines.append("### " + info.text.strip())
    elif info.name == "div":
        c = info['class'][0]
        if c == 'bookTitle':
            lines.append("# " + info.text.strip())
        elif c == "authors":
            lines.append(info.text.strip())
        elif c == "noteText":
            lines.append("- "+info.text.strip().split("\n")[0])

f = open("converted.md", "w")
f.writelines("\n\n".join(lines))
f.close()
