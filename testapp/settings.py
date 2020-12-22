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
    'aggregation_regress.tests.AggregationTests.test_annotated_conditional_aggregate',
    'aggregation_regress.tests.AggregationTests.test_annotation_with_value',
    'aggregation_regress.tests.AggregationTests.test_values_list_annotation_args_ordering',
    'annotations.tests.NonAggregateAnnotationTestCase.test_annotate_exists',
    'annotations.tests.NonAggregateAnnotationTestCase.test_combined_expression_annotation_with_aggregation',
    'backends.tests.BackendTestCase.test_queries',
    'backends.tests.BackendTestCase.test_unicode_password',
    'backends.tests.FkConstraintsTests.test_disable_constraint_checks_context_manager',
    'backends.tests.FkConstraintsTests.test_disable_constraint_checks_manually',
    'backends.tests.LastExecutedQueryTest.test_last_executed_query',
    'bulk_create.tests.BulkCreateTests.test_bulk_insert_nullable_fields',
    'expressions_case.tests.CaseExpressionTests.test_annotate_with_in_clause',
    'introspection.tests.IntrospectionTests.test_get_constraints',
    'introspection.tests.IntrospectionTests.test_get_table_description_types',
    'introspection.tests.IntrospectionTests.test_smallautofield',
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
