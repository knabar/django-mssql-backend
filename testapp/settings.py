import dj_database_url

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite'),
    'other': dj_database_url.config(env='DATABASE_URL_OTHER', default='sqlite:///db.sqlite'),
}

INSTALLED_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'sql_server.pyodbc',
    'testapp',
)


TEST_RUNNER = 'testapp.runner.ExcludeTestSuiteRunner'
EXCLUDED_TESTS = (
    'ordering.tests.OrderingTests.test_deprecated_values_annotate',
    'ordering.tests.OrderingTests.test_orders_nulls_first_on_filtered_subquery',
)

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
