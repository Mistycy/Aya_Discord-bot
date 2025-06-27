import openai
import os
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

class OpenAIChat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="perguntar")
    async def perguntar(self, ctx, *, pergunta):
        await ctx.send("💬 Pensando...")
        resposta = self.gerar_resposta_openrouter(pergunta)
        await ctx.send(resposta)

    def gerar_resposta_openrouter(self, prompt):
        url = "https://openrouter.ai/api/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "HTTP-Referer": "https://seusite.com",
            "X-Title": "discord-bot"
        }

        data = {
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "Você é um assistente útil e gentil."},
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(url, headers=headers, json=data)
            result = response.json()
            if 'choices' in result:
                return result['choices'][0]['message']['content'].strip()
            else:
                return "❌ Erro: resposta inesperada da API."
        except Exception as e:
            return f"❌ Erro ao gerar resposta: {e}"

# Função obrigatória para carregar a cog
async def setup(bot):
    await bot.add_cog(OpenAIChat(bot))