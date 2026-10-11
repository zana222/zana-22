# کد ساخت فایل صوتی از توییت
from gtts import gTTS

tweet_text = """
AI can be wrong and still sound completely sure.
I once got a wrong answer from AI that sounded so convincing I almost believed it.
A person might stop and say I don't know.
But AI can give a wrong answer with the same confidence as a right one.
That is the real problem.
Maybe the next big step is not making AI smarter,
but teaching it when to say I might be wrong.
Would you trust an AI that knows when it does not know?
"""

tts = gTTS(text=tweet_text, lang='en')
tts.save("tweet_audio.mp3")
print("فایل صوتی با موفقیت ساخته شد!")
