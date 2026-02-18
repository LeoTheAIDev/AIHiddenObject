from openai import OpenAI
import base64

# 🔑 Put your API key here (keep it secret, do NOT share it)
client = OpenAI(api_key="RzQrJRvxP3PHdaWofALW4-2zEFZqe8_jjChMQXvekO-Ymo9D0eTsT3BlbkFJMtG1IRuA559cl9e_XyO-WWYTVm6NF4HWemvLziKKZoojrxYAsRyXX7KPMZdDYhdOzQcziwhjwA")

original_path = "OriginalImage_with_circle.png"
mask_path = "mask.png"
output_path = "Edited.png"

try:
    response = client.images.edit(
        model="dall-e-2",   # or "gpt-image-1" if you prefer
        image=open(original_path, "rb"),
        mask=open(mask_path, "rb"),
        prompt="Add something interesting inside the transparent circle.",
        size="1024x1024",
        response_format="b64_json",
    )

    image_data = base64.b64decode(response.data[0].b64_json)
    with open(output_path, "wb") as f:
        f.write(image_data)

    print("✅ DALL·E edited image saved as", output_path)

except Exception as e:
    print(f"❌ Error: {e}")
