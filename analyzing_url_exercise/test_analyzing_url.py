from unittest import TestCase
from analyzing_url_exercise.analyzing_url import analyze
from analyzing_url_exercise.models import Entity


class Test(TestCase):

    def entity_factory(self, protocol = '', host = '', domain = '', path = '', parameters = '',user = '', password = ''):
        mock = Entity()
        mock.url['protocol'] = protocol
        mock.url['host'] = host
        mock.url['domain'] = domain
        mock.url['path'] = path
        mock.url['parameters'] = parameters
        mock.url['user'] = user
        mock.url['password'] = password

        return mock.url

    def test_gmail(self):
        url = self.entity_factory(protocol='http', host='www', domain='google.com', path='mail', parameters='user=foo')
        self.assertDictEqual(analyze('http://www.google.com/mail/user=foo'), url)

    def test_ssh_git(self):
        url = self.entity_factory(protocol='ssh', user='foo', password='pwd.123', domain='git.com')
        self.assertDictEqual(analyze('ssh://foo%senha@git.com/'), url)

    def test_invalid_url(self):
        self.assertRaises(Exception(),"invalid url")

