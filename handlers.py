from aiogram import Router
from aiogram.types import Message, InlineQueryResultCachedVideo, InlineQuery
from aiogram.filters import CommandStart, CommandObject

VIDEO_FILE_ID = "BAACAgIAAxkBAAMGaPvfM7Xc9ENsf28qnhSBu6nCHOwAAqOSAAIl3eFL2xbZ_IDydF02BA"


router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message, command: CommandObject):
    await message.answer_video(
        video=VIDEO_FILE_ID,
    )

@router.inline_query()
async def inline_query_handler(query: InlineQuery):
    results = [
        InlineQueryResultCachedVideo(
            id="GOOSE_WALK_AND_FLEX",
            video_file_id=VIDEO_FILE_ID,
            title="Гусь танцует",
            description="Гусь идёт и танцует",
            caption=""
        )
    ]
    
    await query.answer(
        results,
        cache_time=3600,
        is_personal=False
    )
