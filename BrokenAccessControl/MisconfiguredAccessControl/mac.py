# This script specifically checks miscofigured access controls in a very simple webapp.
import requests
import argparse

def access_control_test(login_url, admin_url, username, password):
    try:
        session = requests.session()
        post_response = session.post(login_url, data={'username': username, 'password': password})

        print("""
                !!!! Server Response After Logging In !!!
              
              """, post_response.text)

        """
        Check if we can access the admin page. 
        To get all the directories in a webapp,we can use tools like gobuster,
        Here I'm assuming the directory before hand.
        """

        req_data = {
            'role': 'admin'
        }
        get_response = session.get(admin_url, params=req_data)

        print("""
                !!!! Server Response After Accessing Admin Page !!!
              
              """, get_response.text)
        return get_response
    except Exception as e:
        print('Error is ', e)
        raise e

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Take username, password, admin url and login url as input')

    parser.add_argument('-u', '--username', help='Username', required=True)
    parser.add_argument('-p', '--password', help='Password', required=True)
    parser.add_argument('-a', '--admin', help='Admin url', required=True)
    parser.add_argument('-l', '--login', help='Login url', required=True)

    args = parser.parse_args()

    admin_url = args.admin
    login_url = args.login
    username = args.username
    password = args.password
    print(admin_url, login_url, username, password)

    response = access_control_test(login_url, admin_url, username, password)
    if response.status_code == 200:
        print("Vulnerable to Broken Access Control")
    else:
        print("Not Vulnerable to Broken Access Control")


