>>> from mcpi import minecraft
>>> mc = minecraft.Minecraft.create()
>>> mc.postToChart("Hello I am Kai")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Minecraft' object has no attribute 'postToChart'
>>> mc.postToChat("Hello I am kai")


>>> pos = mc.player.getPos()
>>> print(pos)
Vec3(51.882,8.93854,-13.3998)


>>> x, y, z = mc.player.getPos()
>>> mc.player.setPos(x, y+100, z)


>>> x, y, z = mc.player.getPos()
>>> mc.setBlock(x+1, y, z, 1)


>>> stone = 1
>>> x, y, z = mc.player.getPos()
>>> mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, stone)

>>> from mcpi.minecraft import Minecraft
>>> from time import sleep

>>> mc = Minecraft.create()
>>> 
>>> flower = 38
>>> 
>>> while True:
...     x, y, z = mc.player.getPos()
...     mc.setBlock(x, y, z, flower)
...     sleep(0.1)


>>> tnt = 46
>>> x, y, z = mc.player.getPos()
>>> mc.setBlocks(x+1, y+1, z+1, x+11, y+11, z+11, tnt, 1)



>>> from mcpi.minecraft import Minecraft

>>> mc = Minecraft.create()
>>> 
>>> x, y, z = mc.player.getPos()
>>> 
>>> lava = 10
>>> 
>>> mc.setBlock(x+3, y+3, z, lava)


>>> from mcpi.minecraft import Minecraft
>>> from time import sleep

>>> mc = Minecraft.create()
>>> 
>>> x, y, z = mc.player.getPos()
>>> 
>>> lava = 10
>>> water = 8
>>> air = 0
>>> 
>>> mc.setBlock(x+3, y+3, z, lava)
>>> sleep(20)
>>> mc.setBlock(x+3, y+5, z, water)
>>> sleep(4)
>>> mc.setBlock(x+3, y+5, z, air)


