from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards import main_kb
from utils.get_time import get_current_time
# Commands router
router_commands = Router()

# Start command
@router_commands.message(Command("start"))
async def command_start_handler(message: Message):
    await message.answer(f"Hi {message.from_user.first_name}! Current time is {get_current_time()}", reply_markup=main_kb.get_main_kb())

# Help command
@router_commands.message(Command("help"))
async def command_help_handler(message: Message):
    await message.answer("Help!")

# Info command
@router_commands.message(Command("info"))
async def command_info_handler(message: Message):
    await message.answer("Info!")
