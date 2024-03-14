from bot.start_bot import starts_bot
from handlers import dp
from handlers.handler_otvet_bot import dp
from handlers.callbacks import dp

__all__ = ['starts_bot', 'dp']

if __name__ == "__main__":
    starts_bot()
