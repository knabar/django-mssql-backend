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
    'aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_exists',
    'aggregation.tests.AggregateTestCase.test_aggregation_subquery_annotation_values_collision',
    'aggregation.tests.AggregateTestCase.test_count_star',
    'aggregation.tests.AggregateTestCase.test_distinct_on_aggregate',
    'aggregation.tests.AggregateTestCase.test_expression_on_aggregation',
    'bulk_create.tests.BulkCreateTests.test_bulk_insert_nullable_fields',
    'ordering.tests.OrderingTests.test_deprecated_values_annotate',
    'ordering.tests.OrderingTests.test_order_by_fk_attname',
    'ordering.tests.OrderingTests.test_order_by_pk',
    'ordering.tests.OrderingTests.test_orders_nulls_first_on_filtered_subquery',
    'prefetch_related.tests.GenericRelationTests.test_prefetch_GFK_nonint_pk',
)

SECRET_KEY = "django_tests_secret_key"

# Use a fast hasher to speed up tests.
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.MD5PasswordHasher',
]
