# openai-write-faster-blogs

This is a small flask app that pulls information from GPT-3. Prompts are structured to help write blog posts faster

Adjust GPT-3 fields in blog.py to alter results,

- Example config.py file that is needed

## API 
OPENAI_API_KEY = 'your-open-ai-api-key'

## Flask
class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "i-like-turtles"


config = {
    'development': DevelopmentConfig,
    'testing' : DevelopmentConfig,
    'production' : DevelopmentConfig
}
