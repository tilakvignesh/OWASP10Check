# Script checks whether the webapp is vulnerable to IDOR or not.
"""
NOTE: this script won't work with sites that don't have an authentication mechanism 
or sites where the backend does not extract and use info from the query params 
(Or extracts but has some sort of security measure)


EXAMPLE FOR WHERE THIS WILL WORK:

Let's say u have a website https://a.com?user_id:abc123

Then if u make a request to https://a.com?user_id:bca213 and u get a 200 response,
it means that the site is vulnerable to IDOR

"""
import requests
import random
import argparse

def idor_test(url, key, query_param):
    try:
        
        mangled_query_param = ''.join(random.sample(query_param, len(query_param)))

        req_data = {
            key: mangled_query_param
        }

        response = requests.get(url, params=req_data)
        print(response.url)
        return response
    except Exception as e:
        raise e

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Take url, key and query param as input')

    parser.add_argument('-u', '--url', help='Url', required=True)
    parser.add_argument('-k', '--key', help='Key', required=True)
    parser.add_argument('-q', '--query_param', help='Query param', required=True)

    args = parser.parse_args()

    url = args.url
    key = args.key
    query_param = args.query_param
    print(url, key, query_param)

    response = idor_test(url, key, query_param)
    if response.status_code == 200:
        print("Vulnerable to IDOR")
    else:
        print("Not Vulnerable to IDOR")