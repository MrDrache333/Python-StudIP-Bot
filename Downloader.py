import Suppe

def dowload(ids, session):
    for id in ids:

        fileLink = Suppe.getFileLink(session, id)

        file = session.get(fileLink)

        zipFile = open("Dateien//" + id + ".zip", "wb")
        zipFile.write(file.content)
        zipFile.close
