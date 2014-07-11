#!/bin/bash

echo "redeploying readlingual"
echo

echo "updating project ..."
echo

git pull origin
echo

echo "... done"
echo

echo "touching the wsgi file for recompilation ..."
echo

touch readlingual/wsgi.py

echo "...done"
echo
