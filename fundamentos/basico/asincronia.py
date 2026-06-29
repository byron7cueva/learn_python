import asyncio
import time

def pedir_cafe():
    print("Pidiendo un cafe")
    time.sleep(3)
    print("Cafe listo")
    return "Cafe"

async def pedir_cafe_async():
    print("Pidiendo un cafe")
    await asyncio.sleep(3) # No bloque, si no mas bien cede el control
    print("Cafe listo")
    return "Cafe"

# Llamar a la funcion dentro de un contexto asincrono
async def main():
    inicio = time.time()

    # Ejecuttar dos tareas a la vez
    await asyncio.gather(
        pedir_cafe_async(),
        pedir_cafe_async(),
        pedir_cafe_async()
    )
    fin = time.time()
    print(f"Tiempo total {fin - inicio:.2f}")

asyncio.run(main())