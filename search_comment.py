from TikTokApi import TikTokApi
import asyncio
import os
import sys

if len(sys.argv) < 2:
    print("Veuillez fournir un mot ou une expression à rechercher.")
    sys.exit(1)

search_term = sys.argv[1]

video_ids = [
    "7280187119081884961",
    "7279831870110518561",
    "7279098586686819616",
    "7276734394738511137",
    "7276495084001004833",
    "7273903879832505632",
    "7271712060709342497",
    "7270581817978129696",
    "7266079986841292064",
    "7264664697742413088"
]

async def get_comments(video_id, search_term):
    async with TikTokApi() as api:
        await api.create_sessions(num_sessions=1, sleep_after=3)
        video = api.video(id=video_id)
        async for comment in video.comments(count=100):
            if search_term.lower() in comment.text.lower():
                print(f"{comment.text}")
                print(f"https://www.tiktok.com/@scrowhacking/video/{video_id}")
                sys.exit(0)

if __name__ == "__main__":
    for video_id in video_ids:
        asyncio.run(get_comments(video_id, search_term))

