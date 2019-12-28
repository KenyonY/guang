#!bin/bash
# python workflow.py
git add .
git pull
git commit --allow-empty-message --amend
git push -u origin master