import requests
import Suppe
import Downloader

login_url = "https://elearning.uni-oldenburg.de/plugins.php/uollayoutplugin/login?cancel_login=1"
course_url = "https://elearning.uni-oldenburg.de/dispatch.php/my_courses"


def start(login_data):
    with requests.Session() as session:
        session.post(login_url, login_data)

        ids = Suppe.getCourseID(session)

        Downloader.dowload(ids, session)
