# Exercisie extracted from
# http://dojopuzzles.com/problemas/exibe/analisando-urls/

# Given a URL, develop a program to indicate whether the URL is valid or not and, if valid, return its constituent parts.
#
# Examples:
#
#     Entry: http://www.google.com/mail?user=foo
#     Output:
#     Protocol: http
#     Host: www
#     domain: google.com
#     path: mail
#     parameters: user = foo
#
#     Entry: ssh://foo%senha@git.com/
#     Output:
#     Protocol: ssh
#     User: foo
#     Password: password
#     domain: git.com

from analyzing_url_exercise.models import Url
from urllib.parse import urlparse


def analyze(url_string):
    o = urlparse(url_string)
    url = Url(protocol=o.scheme, parameters=o.query, path=o.path)

    if o.hostname is None:
        raise ValueError('Invalid url')
    if o.hostname.count('.') >= 2:
        index = o.hostname.index('.')
        url.host = o.hostname[:index]
        url.domain = o.hostname[index + 1:]
    else:
        url.domain = o.hostname

    url.path = url.path.replace('/','')

    if o.username is not None:
        url.user = o.username

    if o.password is not None:
        url.password = o.password
    elif o.username is not None and '%' in url.user:
        url.password = url.user.split('%')[-1]
        url.user = url.user.split('%')[0]

    return url
