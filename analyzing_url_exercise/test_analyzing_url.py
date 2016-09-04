from unittest import TestCase
from analyzing_url_exercise.analyzing_url import analyze
from analyzing_url_exercise.models import Entity


class Test(TestCase):

    def entity_factory(self, protocol = '', host = '', domain = '', path = '', parameters = '',user = '', password = ''):
        entity = Entity()
        entity.url['protocol'] = protocol
        entity.url['host'] = host
        entity.url['domain'] = domain
        entity.url['path'] = path
        entity.url['parameters'] = parameters
        entity.url['user'] = user
        entity.url['password'] = password

        return entity.url

    def test_gmail(self):
        url = self.entity_factory(protocol='http', host='www', domain='google.com', path='mail', parameters='user=foo')
        self.assertDictEqual(analyze('http://www.google.com/mail/user=foo'), url)

    def test_ssh_git(self):
        url = self.entity_factory(protocol='ssh', user='foo', password='pwd.123', domain='git.com')
        self.assertDictEqual(analyze('ssh://foo%senha@git.com/'), url)

    def invalid_url(self):
        self.assertRaises(Exception(),"invalid url")

