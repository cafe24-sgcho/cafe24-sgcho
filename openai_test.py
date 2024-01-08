import os
from dotenv import load_dotenv
from openai import OpenAI

# .env 파일 로드
load_dotenv()

# 환경 변수 설정
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

client = OpenAI(
  organization='org-PH8w9Tb9YAupFb1SbJ2399d8',
)


curl https://api.openai.com/v1/chat/completions 
  -H "Content-Type: application/json" 
  -H "Authorization: Bearer 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 
  -d '{
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "Say this is a test!"}],
     "temperature": 0.7
   }'