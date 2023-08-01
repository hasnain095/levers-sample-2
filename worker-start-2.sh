#! /usr/bin/env bash
set -e

celery -A app.worker worker -B -l info -Q main-queue-app-2,queue-app-2-sync -c 1
