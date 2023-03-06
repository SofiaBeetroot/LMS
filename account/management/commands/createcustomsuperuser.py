from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

_DEFAULT_EMAIL_DOMAIN = 'example.com'


class Command(BaseCommand):
    help = 'Used to create a _custom_ superuser.'

    def add_arguments(self, parser):
        credentials = parser.add_argument_group('credentials')
        credentials.add_argument('--user', metavar='USER', dest='username',
                                 default='admin',                     # default='admin',
                                 help='user name (default: "%(default)s")')
        credentials.add_argument('--password', metavar='PASSWORD',
                                 default='qwerty',
                                 help='password (default: "%(default)s")')
        credentials.add_argument('--email', metavar='EMAIL',
                                 default='admin@example.com',
                                 help='e-mail address (default: "%(default)s")')  # help='e-mail address (default: "{}@{}")'.format('<user>', _DEFAULT_EMAIL_DOMAIN)

    def _report_success(self, message):
        self.stdout.write(self.style.SUCCESS(message))

    def _require_identical_configuration(self, user, password, email):
        if not user.check_password(password):
            raise CommandError('User "{}" exists but password differs.'
                               .format(user.username))

        if user.email != email:
            raise CommandError('User "{}" exists but e-mail address differs.'
                               .format(user.username))

        if not user.is_superuser:
            raise CommandError('User "{}" exists but is not a superuser.'
                               .format(user.username))

    def _create_new_superuser(self, username, password, email):
        return User.objects.create_superuser(username=username,
                                             password=password,
                                             email=email)

    def handle(self, *args, **options):
        username = options['username']
        password = options['password']
        email = options['email']

        if email is None:
            email = '{}@{}'.format(username, _DEFAULT_EMAIL_DOMAIN)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            try:
                user = self._create_new_superuser(username, password, email)
                user.save()
            except Exception as e:
                raise CommandError('Could not create user: {}'.format(e))

            self._report_success('Superuser "{}" with e-mail address "{}"'
                                 ' created.'.format(username, email))
        else:
            self._require_identical_configuration(user, password, email)
            self._report_success('User "{}" with identical configuration '
                                 'exists, nothing more to do.'
                                 .format(username))
