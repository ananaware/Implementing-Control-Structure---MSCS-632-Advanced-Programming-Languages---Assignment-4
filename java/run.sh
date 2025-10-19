#!/usr/bin/env bash
set -e
cd "$(dirname "$0")"
javac -encoding UTF-8 -d out src/ScheduleApp.java
java -cp out ScheduleApp
