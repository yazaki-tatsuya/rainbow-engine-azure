#---- 掲載時不要START ----#
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import env
#---- 掲載時不要END ----#

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes
import time

# キーとエンドポイントの設定
subscription_key = env.get_env_variable("COMPUTER_VISION_KEY")
endpoint = env.get_env_variable("COMPUTER_VISION_ENDPOINT")

# クライアントの作成
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# # 画像のURL
# remote_image_url = "https://example.com/image.jpg"

# # OCRの実行
# print("===== Read File - remote =====")
# # Call API with URL and raw response (allows you to get the operation location)
# recognize_results = computervision_client.read(local_image_path,  raw=True)


# 画像ファイルのパス
local_image_path = "./20240114_IT#0811_Azure_OCR_使い方/OCRTest001.jpg"

# ファイルをバイトデータとして読み込む
with open(local_image_path, "rb") as image_stream:
    recognize_results = computervision_client.read_in_stream(image_stream, raw=True)

# 結果の取得
operation_location_remote = recognize_results.headers["Operation-Location"]
operation_id = operation_location_remote.split("/")[-1]

while True:
    get_printed_text_results = computervision_client.get_read_result(operation_id)
    if get_printed_text_results.status not in ['notStarted', 'running']:
        break
    time.sleep(1)

# 結果の表示
if get_printed_text_results.status == OperationStatusCodes.succeeded:
    for text_result in get_printed_text_results.analyze_result.read_results:
        for line in text_result.lines:
            print(line.text)
            print()