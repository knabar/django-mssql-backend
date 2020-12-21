# TODO:
#
# * m2m_through_regress
# * many_to_one_null

set -e

DJANGO_VERSION="$(python -m django --version)"

cd django
git fetch --depth=1 origin +refs/tags/*:refs/tags/*
git checkout $DJANGO_VERSION
pip install -r tests/requirements/py3.txt

python tests/runtests.py --settings=testapp.settings --noinput --keepdb \
    custom_columns \
    custom_managers \
    custom_methods \
    custom_migration_operations \
    custom_pk \
    dates \
    db_typecasts \
    db_utils \
    defer \
    distinct_on_fields \
    empty \
    expressions_window \
    extra_regress \
    field_deconstruction \
    field_defaults \
    field_subclassing \
    filtered_relation \
    fixtures_model_package \
    force_insert_update \
    foreign_object \
    from_db_value \
    generic_relations \
    generic_relations_regress \
    get_earliest_or_latest \
    get_object_or_404 \
    known_related_objects \
    m2m_and_m2o \
    m2m_intermediary \
    m2m_multiple \
    m2m_recursive \
    m2m_regress \
    m2m_signals \
    m2m_through \
    m2o_recursive \
    managers_regress \
    many_to_many \
    many_to_one \
    max_lengths \
    mutually_referential \
    nested_foreign_keys \
    null_fk \
    null_fk_ordering \
    null_queries \
    one_to_one \
    or_lookups \
    order_with_respect_to \
    pagination \
    prefetch_related \
    queryset_pickle \
    raw_query \
    reverse_lookup \
    save_delete_hooks \
    select_related \
    select_related_onetoone \
    select_related_regress \
    update \
    update_only_fields
