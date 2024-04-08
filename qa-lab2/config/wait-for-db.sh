#!/bin/sh
# wait until MySQL is really available
set -e

host="$1"
shift
cmd="$@"

until mysql -h"$host" -u"root" -p1234 -e "show databases;" > /dev/null 2>&1; do
    >&2 echo "DB is unavailable - sleeping"
    sleep 1
done
>&2 echo "DB is up - executing command"
exec $cmd