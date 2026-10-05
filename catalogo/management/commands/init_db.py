from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Initialize database with migrations and data'

    def handle(self, *args, **options):
        self.stdout.write('Running migrations...')
        try:
            call_command('migrate', verbosity=2)
            self.stdout.write(self.style.SUCCESS('✓ Migrations applied'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Migration error: {e}'))
            return

        self.stdout.write('Loading initial data...')
        try:
            call_command('load_initial_data')
            self.stdout.write(self.style.SUCCESS('✓ Data loaded'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Data load error: {e}'))

        self.stdout.write('Collecting static files...')
        try:
            call_command('collectstatic', '--noinput', verbosity=0)
            self.stdout.write(self.style.SUCCESS('✓ Static files collected'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'✗ Static error: {e}'))

        self.stdout.write(self.style.SUCCESS('\n✓ Database initialization complete'))
