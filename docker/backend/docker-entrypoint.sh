#!/usr/bin/env sh
set -e

CMD=$1


run_migrations() {
    echo "Checking database status"
    until pg_isready -h $POSTGRES_SERVER -p $POSTGRES_PORT -U $POSTGRES_USER; do
        echo "Database is not running"
        sleep 1
    done

    echo "Running migrations"
    python manage.py migrate --no-input
}

case "$CMD" in
    "runserver" )
        run_migrations

        echo "Starting server"
        exec gunicorn -c $GUNICORN_CONF planta_electrica.wsgi
        ;;
    "collectstatic" )
        collect_static
        ;;
    * )
        exec "$@"
        ;;
esac
