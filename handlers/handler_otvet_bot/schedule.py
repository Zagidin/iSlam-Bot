import asyncio
import aioschedule

from base.setting_write_base import delete_user_base_settings


async def schedule():
    # Schedule the function to run every 24 hours
    aioschedule.every(1).minutes.do(delete_user_base_settings)

    # Run the scheduler in an infinite loop
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

