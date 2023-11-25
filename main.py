import asyncio
import aiohttp

async def obtener_respuesta_async(numero_guia):
    url = 'https://mobile.servientrega.com/Services/ShipmentTracking/api/ControlRastreovalidaciones'
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.9',
        'Content-Type': 'application/json',
        'Origin': 'https://mobile.servientrega.com',
        'Referer': f'https://mobile.servientrega.com/WebSitePortal/RastreoEnvioDetalle.html?Guia={numero_guia}',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"'
    }
    data = {
        'numeroGuia': numero_guia,
        'idValidacionUsuario': '1',
        'tipoDatoValidar': '1',
        'datoRespuestaUsuario': '1',
        'idpais': 1,
        'lenguaje': 'es'
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(url, headers=headers, json=data) as response:
            return await response.json()

async def main():
    numero_guia = '9136016383'  # Aquí coloca el número de guía que deseas consultar
    respuesta = await obtener_respuesta_async(numero_guia)
    print(respuesta)  # Esto imprimirá la respuesta JSON obtenida

# Ejecutar el bucle de eventos
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
