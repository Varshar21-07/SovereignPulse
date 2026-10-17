import asyncio
import time
import os
from pipecat_slng import SlngTTSService, SlngTTSSettings, WorldPart

async def test():
    api_key = "slng_cu_QfdsNgIBQ6Ar3KEAzHeGNxz7JIrR6Fj96mOoFJxc"
    print("Testing SLNG TTS connection with api_key...")
    
    tts = SlngTTSService(
        api_key=api_key,
        voice="aura-2-thalia-en",
        model="deepgram/aura:2",
        world_part="in" # using India sovereign hub or eu-north
    )
    print("Initialized SlngTTSService successfully:", tts)

if __name__ == "__main__":
    asyncio.run(test())
