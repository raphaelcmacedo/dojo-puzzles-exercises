# Exercisie extracted from
# http://dojopuzzles.com/problemas/exibe/analisando-urls/

# Given a URL, develop a program to indicate whether the URL is valid or not and, if valid, return its constituent parts.
#
# Examples:
#
#     Entry: http://www.google.com/mail/user=foo
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

from analyzing_url_exercise.models import Entity

def analyze(url):
    entity = Entity()
    return entity.url