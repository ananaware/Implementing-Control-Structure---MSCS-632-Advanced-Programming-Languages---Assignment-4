#!/usr/bin/env bash
set -e
mkdir -p out
javac -d out src/ScheduleApp.java
java -cp out ScheduleApp
