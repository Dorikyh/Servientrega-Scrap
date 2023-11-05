import asyncio
import aiohttp

base = 9136016382

async def get_package(package, session):
    url = 'https://mobile.servientrega.com/GreenMobile/CO/mapas/DistribucionCliente/getGuiasDistribucionCliente'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/118.0',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'X-Requested-With': 'XMLHttpRequest',
        'Origin': 'https://mobile.servientrega.com',
        'Referer': 'https://mobile.servientrega.com/GreenMobile/CO/Mapas/DistribucionCliente/FrmDistribucionCliente?NumeroGuia='+str(package),
        'Cookie': '_gcl_au=1.1.1628043997.1697595921; _ga=GA1.2.1146112341.1697595921; _gid=GA1.2.2101526116.1697595921; _ga_ST8S2VTEC8=GS1.1.1697595921.1.1.1697598039.60.0.0; _fbp=fb.1.1697595922091.267531242; _gat=1',
    }

    data = {
        'strIdGuia': package
    }

    async with session.post(url, headers=headers, data=data) as response:
        if response.status == 200:
            data = await response.json()
            if data and data.get('strNoGuia') and data['strNoGuia'] != 'null':
                # print(data) if you want to see the full json response
                numero_guia = data.get('strNoGuia')
                fecha_paquete = data.get('strFechaEntrega')[:10]
                nombre_empleado = data.get('strNombreEmpleado')
                ciudad_destino = data.get('strNombreCiudad')
                return f"[{numero_guia}] ({fecha_paquete}): {nombre_empleado}, {ciudad_destino}"
            else:
                return "Package not found"
        else:
            return "Error: " + str(response.status)

async def main():
    async with aiohttp.ClientSession() as session:
        # if you want to get all packages from a specific number you can change the in range(1) to a bigger number to get a lot of packages, because ids are secuencial
        tasks = [get_package(base + i, session) for i in range(1)]
        results = await asyncio.gather(*tasks)

        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
