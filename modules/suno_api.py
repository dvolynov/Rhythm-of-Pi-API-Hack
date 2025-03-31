import httpx
import aiofiles
import os


class SunoAPI:

    SUNO_API_URL = "https://apibox.erweima.ai/api/v1/generate"

    def __init__(self, auth_token, save_directory):
        self.headers = {
            "Authorization": f"Bearer {auth_token}",
            "Accept":        "application/json",
            "Content-Type":  "application/json"
        }
        self.save_directory = save_directory

    async def create_task(self, prompt, custom_mode, instrumental, model, callback_url):
        payload = {
            "prompt":       prompt,
            "customMode":   custom_mode,
            "instrumental": instrumental,
            "model":        model,
            "callBackUrl":  callback_url
        }
        async with httpx.AsyncClient() as client :
            response = await client.post(self.SUNO_API_URL, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()


    async def download_audio(self, audio_url):
        async with httpx.AsyncClient() as client:
            audio_response = await client.get(audio_url)
            audio_response.raise_for_status()

            file_name = os.path.basename(audio_url)
            file_path = os.path.join(self.save_directory, file_name)

            os.makedirs(self.save_directory, exist_ok=True)

            async with aiofiles.open(file_path, 'wb') as audio_file:
                await audio_file.write(audio_response.content)

            return file_name