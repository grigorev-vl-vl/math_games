# Hello, there!
## Roadmap
- [x] Make sandbox v0.1.0
- [x] Prepare to deploy
- [x] Deploy
- [ ] Make a simple game
- [ ] Make a teacher's interface
- [ ] New features coming soon...   


## How to deploy
1) Install 
   1) python3-dev, python3-venv, python3 pip
   2) gunicorn, supervisor, nginx
   3) vim
   4) libpq-dev
2) Create a new environment
3) Make sure you installed all the required apps (requirements/prod.txt)
4) Create .env file to connect to your databese (default is postgreSQL)
5) Run with production settings (--settings==gamesite.settings.prod)
