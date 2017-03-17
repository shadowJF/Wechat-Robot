from pydub import AudioSegment

sound = AudioSegment.from_mp3("170307-110806.mp3")
sound.export("output", format="wav")
