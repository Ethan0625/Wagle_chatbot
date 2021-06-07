from model import User, Wagle, KoGPT2Chat 

def wagle(input : User)->Wagle : 
    """와글와글 신나게 이야기를 나눠봐요."""
    model = KoGPT2Chat.load_from_checkpoint('model_chp/model_-last.ckpt')
    text = input.user
    return Wagle(wagle = model.chat(text = text.strip()))