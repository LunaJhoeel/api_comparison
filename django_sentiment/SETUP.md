## Launch
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d '{"text":"I love using Hugging Face transformers!"}'


