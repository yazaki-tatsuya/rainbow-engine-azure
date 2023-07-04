import os
import azure.cognitiveservices.speech as speechsdk

# 環境変数"SPEECH_KEY"と"SPEECH_REGION"を取得
# 値自体は外だし(.env)している
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)

# 声の言語や種類を設定。
# ラインナップはこちらのページで紹介されています。
# https://learn.microsoft.com/en-us/azure/cognitive-services/speech-service/language-support?tabs=tts

# speech_config.speech_synthesis_voice_name='en-US-JennyNeural'
# speech_config.speech_synthesis_voice_name='ja-JP'
#speech_config.speech_synthesis_voice_name='ja-JP-AoiNeural1' # あおい ♀
# speech_config.speech_synthesis_voice_name='ja-JP-DaichiNeural1' # だいち ♂
# speech_config.speech_synthesis_voice_name='ja-JP-KeitaNeural' # けいた ♂
# speech_config.speech_synthesis_voice_name='ja-JP-MayuNeural1' # まゆ ♀
# speech_config.speech_synthesis_voice_name='ja-JP-NanamiNeural' # ななみ ♀
# speech_config.speech_synthesis_voice_name='ja-JP-NaokiNeural1' # なおき ♂
# speech_config.speech_synthesis_voice_name='ja-JP-AoiNeural1' # しおり ♀

# シンセサイザーは一般的に音楽を合成する機械
# 発話設定(speech config)と音響設定(audio config)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# コンソールからテキストを取得し、デフォルトスピーカーに合成
print("Enter some text that you want to speak >")
text = input()

####################################################################
# 追加箇所：Speech Synthesis Markup Language (SSML)の定義
# style：怒った、叫ぶ、ささやく、友好的などの声のスタイル
# styledegree：0.01～2の間で指定。0.01に近いほど標準的、2に近いほどstyleが強調される。
# role：男、女、老女、老男、若女、若男、成人男性、成人女性など
ssml_text = "<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts' xml:lang='ja-JP'>" \
        "<voice name='en-US-AriaNeural'>" \
        "<mstts:express-as style='shouting' styledegree='2'>"+"That'd be just amazing!"+"</mstts:express-as>" \
        "</voice></speak>"

# 修正箇所：SSML経由の場合は「speak_ssml_async」メソッドを使用
speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml_text).get()
# speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()
####################################################################

# 音響合成完了
if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized for text [{}]".format(ssml_text))
# 音響合成キャンセル
# タイムアウト、API呼び出しの最中のキャンセル、APIで受信した音声が処理できずエラーになった場合
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))
            print("Did you set the speech resource key and region values?")
