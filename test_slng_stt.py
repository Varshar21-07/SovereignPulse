import asyncio
from pipecat_slng import SlngSTTService

async def test():
    api_key = "slng_cu_QfdsNgIBQ6Ar3KEAzHeGNxz7JIrR6Fj96mOoFJxc"
    print("Testing SLNG STT connection...")
    stt = SlngSTTService(
        api_key=api_key,
        model="deepgram/nova:3",
        world_part="in"
    )
    print("Initialized SlngSTTService successfully:", stt)

if __name__ == "__main__":
    asyncio.run(test())
