@echo off
cd /d "%~dp0"

echo Обновление Фонда Рублевые сбережения...

python parser.py

git add fund214.csv
git commit -m "update fund214"
git push

pause

