from openai import OpenAI
import base64

# 🔑 Put your API key here (keep it secret, do NOT share it)
client = OpenAI(api_key="-2zEFZqe8_jjChMQXvekO-Ymo9D0eTsT3BlbkFJMtG1IRuA559cl9e_XyO-WWYTVm6NF4HWemvLziKKZoojrxYAsRyXX7KPMZdDYhdOzQcziwhjwA")

prompt = (
    "Create a american cartoonish image of anything that looks like its from a story, not like fantasy more like an interesting story where many thing are happening something important shold be happening around the center, its for a spotter game and not to much happening"
)

response = client.images.generate(
    model="dall-e-3",   # or "gpt-image-1" if that's what you usem 
    prompt=prompt,
    size="1024x1024",
    response_format="b64_json",
)

image_base64 = response.data[0].b64_json

if not image_base64:
    raise RuntimeError("No base64 image data returned from API")

filename = "OriginalImage.png"
with open(filename, "wb") as f:
    f.write(base64.b64decode(image_base64))

print(f"✅ Image saved as {filename}")
