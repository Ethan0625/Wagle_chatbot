import json
import requests
from transformers import PreTrainedTokenizerFast, GPT2LMHeadModel
#from transformers.models.auto.tokenization_auto import AutoTokenizer


from model_generate import User, Wagle, KoGPT2Chat 

# autoTokenizer = AutoTokenizer.from_pretrained("gpt2-large")
# url = 'https://train-wrrhqlm5konh50zk93l1-gpt2-train-teachable-ainize.endpoint.ainize.ai/predictions/gpt-2-en-medium-finetune'


def wagle(input : User)->Wagle : 
    """와글와글 신나게 이야기를 나눠봐요."""
    model = KoGPT2Chat.load_from_checkpoint('model_chp/model_-last.ckpt')
    text = input.user
    return Wagle(wagle = model.chat(u_text=text.strip(),m=model))
    
# def wagle2(input : User)->Wagle : 
#     """와글와글 신나게 이야기를 나눠봐요."""
#     model = KoGPT2Chat.load_from_checkpoint('model_chp/model_-last.ckpt')
#     text = input.user
#     encoded = autoTokenizer.encode(text)
#     data = {
#         'text' : encoded,
#         'length' : input.length
#         }
#     response = requests.post(model, data = json.dumps(data), headers ={"Content-Type":'application/json; charset=utf-8'})
    
#     if response.status_code == 200:
#         text = dict()
#         res = response.json()
#         for idx, output in enumerate(res):
#             text[idx] = autoTokenizer.decode(res[idx], skip_special_tokens = True)
#         return Wagle(wagle = model.chat())
#     else:
#         return Wagle(wagle = response.status_code)