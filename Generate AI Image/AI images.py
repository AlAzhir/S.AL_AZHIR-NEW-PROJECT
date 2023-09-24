import openai

openai.api_key=open("API_KEY","r").read()

response=openai.Image.create_edit(
    image=open("image.png","rb"),
    mask=open("mask.png","rb"),
    prompt="Blue sports car on the street",
    n=1,
    size="1024x1024"
)
image_url=response['data'][0]['url']

print(response['data'])

print(image_url)