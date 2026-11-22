# Mi Bot de Discord 🤖

Mi primer bot, hecho para aprender cómo funciona un bot por dentro: escuchar mensajes, decidir qué hacer y responder.

## Qué sabe hacer
- Si le escribes `hola`, responde `¡Hola! ¿Cómo estás?`
- Si le escribes `!dado`, tira un dado y responde un número del 1 al 6
- Si le escribes `kael`, responde con un mensaje personalizado

## Cómo lo armé
1. Creé una aplicación en el [Portal de Desarrolladores de Discord](https://discord.com/developers/applications).
2. Dentro de **Bot**, generé un token y activé el permiso **Message Content Intent** (sin esto, el bot no puede leer lo que escriben).
3. Con **OAuth2 → URL Generator**, generé un link con el scope `bot` y los permisos de enviar mensajes, y lo usé para invitar al bot a mi servidor.

## Cómo correrlo
```bash
pip install -r requirements.txt
python bot.py
```

Crea un archivo `.env` en la carpeta del proyecto con tu token:

```env
DISCORD_TOKEN=tu_token_de_discord
```

Mantén este archivo privado: está excluido de Git y no debes compartir tu token.

## Cómo funciona (la idea general)
Todo bot repite siempre el mismo ciclo:
1. **Escuchar**: `on_message` se activa cada vez que llega un mensaje.
2. **Decidir**: con `if` / `elif` se compara el texto del mensaje (`message.content`).
3. **Responder**: `await message.channel.send(...)` manda la respuesta al canal.

## Próximos pasos
- Agregar más comandos.
