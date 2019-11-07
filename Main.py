import User
import Login

if (__name__ == "__main__"):
    login_data = dict(loginname=User.loginname, password=User.password)
    Login.start(login_data)


