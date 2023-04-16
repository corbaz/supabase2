#!/bin/bash
git add .
git commit -m "Primer commit"
git push github main
git push gitlab main
git push heroku main
heroku open