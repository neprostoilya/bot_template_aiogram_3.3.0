from config.instance import bot, dp
from handlers.commands import router_commands
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Register handlers
def register_handlers():
    dp.include_router(router_commands)

# Run bot
if __name__ == "__main__":
    logger.info("Bot started")
    register_handlers()
    dp.run_polling(bot)
