#!/bin/bash

echo "Start"
sleep 3 && echo "Job1 is done" &
sleep 2 && echo "Job2 is done" &
sleep 1 && echo "Job3 is done" &

wait

echo "Done"
