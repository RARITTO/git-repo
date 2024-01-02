
import asyncio
import requests 

async def fun1( ):
    url = 'https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg'
    file = requests.get(url , allow_redirects=True)
    open('wiki.jpg', 'wb').write(file.content)
    
    print('fun1')
async def fun2 ( ):
    
    url = 'https://www.mozilla.org/en-US/firefox/new/'
    file = requests.get(url , allow_redirects=True)
    open('wiki2.jpg', 'wb').write(file.content)
    print('fun2')
async def fun3 ( ):
    
    url = 'https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg'
    file = requests.get(url , allow_redirects=True)
    open('wiki3.jpg', 'wb').write(file.content)
    print('fun3')
async def fun4 ( ):
    
    url = 'https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg'
    file = requests.get(url , allow_redirects=True)
    open('wiki4.jpg', 'wb').write(file.content)
    print('fun4')
async def fun5 ( ):
    
    url = 'https://c4.wallpaperflare.com/wallpaper/622/676/943/3d-hd-wikipedia-3d-wallpaper-preview.jpg'
    file = requests.get(url , allow_redirects=True)
    open('wiki4.jpg', 'wb').write(file.content)
    print('fun4')

async def main():
    l = await asyncio.gather(
         fun1(),
         fun2(),
         fun3(),
         fun4(),
         fun5()
    )
asyncio.run(main())