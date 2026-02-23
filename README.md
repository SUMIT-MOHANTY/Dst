# Portfolio Deployment

Deployed to Heroku/PythonAnywhere

## Setup

git init
git add .
git commit -m "Initial commit"

## Heroku Deploy

heroku create
heroku addons:create heroku-postgresql
heroku config:set FLASK_ENV=production
git push heroku main
