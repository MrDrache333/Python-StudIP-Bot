from bs4 import BeautifulSoup


def getCourseID(session):
    response = session.get("https://elearning.uni-oldenburg.de/dispatch.php/my_courses")
    soup = BeautifulSoup(response.text, "html.parser")
    idLines = soup.findAll("img", {"src": "https://elearning.uni-oldenburg.de/pictures/course/nobody_small.png?d=1566215753"})
    ids = []
    for idLine in idLines:
        id = idLine.get("class")
        ids.append(str(id).split("['course-avatar-small', 'course-")[1].rsplit("']")[0])  # ID rausfiltern
    return ids


def getFileLink(session, id):
    response = session.get("https://elearning.uni-oldenburg.de/dispatch.php/course/files/flat?cid=" + id)
    soupFiles = BeautifulSoup(response.text, "html.parser")
    link = soupFiles.find("a", {"cid": id}).get("href")
    return link