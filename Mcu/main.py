from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


app=Ursina()

yapılandırma=1
blocksecimi= 1
hız=1

def update():
    
    global yapılandırma
    global blocksecimi
    
    if held_keys["n"or"N"]:
        yapılandırma=1
    if held_keys["b"or"B"]:
        yapılandırma=2
    if held_keys["m"or"M"]:
        yapılandırma=3
    
    if yapılandırma==1:
        

        if held_keys["1"]:
            blocksecimi=1
        elif held_keys["2"]:
            blocksecimi=2
        elif held_keys["3"]:
            blocksecimi=3
        elif held_keys["4"]:
            blocksecimi=4
        elif held_keys["5"]:
            blocksecimi=5
        elif held_keys["6"]:
           blocksecimi=6
        elif held_keys["7"]:
           blocksecimi=7
        elif held_keys["8"]:
           blocksecimi=8
        elif held_keys["9"]:
           blocksecimi=9
        elif held_keys["0"]:
           blocksecimi=10

    elif yapılandırma==2:

        if held_keys["1"]:
            blocksecimi=11
        elif held_keys["2"]:
            blocksecimi=12
        elif held_keys["3"]:
            blocksecimi=13
        elif held_keys["4"]:
            blocksecimi=14
        elif held_keys["5"]:
            blocksecimi=15
        elif held_keys["6"]:
           blocksecimi=16
        elif held_keys["7"]:
           blocksecimi=17
        elif held_keys["8"]:
           blocksecimi=18
        elif held_keys["9"]:
           blocksecimi=19
        elif held_keys["0"]:
           blocksecimi=20
    
    elif yapılandırma==3:

        if held_keys["1"]:
            blocksecimi=21

    global hız

    if held_keys["q"or"Q"]:
        hız=2
    if held_keys["e"or"E"]:
        hız=1
    if held_keys["r"or"R"]:
        hız=3

class Block(Button):
    def __init__(self,position=(0,0,0),texture="grass_block_top",model="cube",color=color.white,higlight_color=color.lime,origin_y=0.5):
        super().__init__(
            parent=scene,
            position=position,
            model=model,
            color=color,
            texture=texture,
            origin_y=origin_y,

        )
    def input(self, key):
        if self.hovered:
            if key=="right mouse down":
                if blocksecimi==1:
                    block=Block(position=self.position + mouse.normal, texture="bedrock")
                elif blocksecimi==2:
                    block=Block(position=self.position + mouse.normal, color=color.green,texture="grass_block_top")
                elif blocksecimi==3:
                    block=Block(position=self.position + mouse.normal, texture="oak_log")
                elif blocksecimi==4:
                    block=Block(position=self.position + mouse.normal, texture="bedrock", model="sphere")
                elif blocksecimi==5:
                    block=Block(position=self.position + mouse.normal, texture="cobblestone")
                elif blocksecimi==6:
                    block=Block(position=self.position + mouse.normal, texture="dirt")
                elif blocksecimi==7:
                    block=Block(position=self.position + mouse.normal, texture="crying_obsidian")
                elif blocksecimi==8:
                    block=Block(position=self.position + mouse.normal, texture="netherrack")
                elif blocksecimi==9:
                    block=Block(position=self.position + mouse.normal, texture="azalea_leaves")
                elif blocksecimi==10:
                    block=Block(position=self.position + mouse.normal, texture="dark_oak_log")
                elif blocksecimi==11:
                    block=Block(position=self.position + mouse.normal, texture="stone_bricks")
                elif blocksecimi==12:
                    block=Block(position=self.position + mouse.normal, texture="bricks")
                elif blocksecimi==13:
                    block=Block(position=self.position + mouse.normal, texture="bookshelf")
                elif blocksecimi==14:
                    block=Block(position=self.position + mouse.normal, texture="oak_planks")
                elif blocksecimi==15:
                    block=Block(position=self.position + mouse.normal, texture="dark_oak_planks")
                elif blocksecimi==16:
                    block=Block(position=self.position + mouse.normal, texture="glass")
                elif blocksecimi==17:
                    block=Block(position=self.position + mouse.normal, texture="chiseled_deepslate")
                elif blocksecimi==18:
                    block=Block(position=self.position + mouse.normal, texture="deepslate_bricks")
                elif blocksecimi==19:
                    block=Block(position=self.position + mouse.normal, texture="nether_bricks")
                elif blocksecimi==20:
                    block=Block(position=self.position + mouse.normal, texture="netherite_block")
                elif blocksecimi==21:
                    block=Block(position=self.position + mouse.normal, texture="ice")
            
            elif key=="left mouse down":
                destroy(self)
            elif key=="escape":
                exit()
            elif key=="w"or"W":
                if hız==1:
                    oyuncu.speed=6
                elif hız==2:
                    oyuncu.speed=10
                elif hız==3:
                    oyuncu.speed=1

            if blocksecimi==1:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10),texture="bedrock")
            elif blocksecimi==2:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,position=(0.7,-0.35),rotation=(-5,-10,-10), color=color.green, texture="grass_block_top")
            elif blocksecimi==3:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="oak_log")
            elif blocksecimi==4:
                belirteç=Entity(model="sphere",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="bedrock")
            elif blocksecimi==5:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="cobblestone")
            elif blocksecimi==6:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="dirt")
            elif blocksecimi==7:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="crying_obsidian")
            elif blocksecimi==8:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="aile1")
            elif blocksecimi==9:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="merve")
            elif blocksecimi==10:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="dark_oak_log")
            elif blocksecimi==11:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="stone_bricks")
            elif blocksecimi==12:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="bricks")
            elif blocksecimi==13:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="bookshelf")
            elif blocksecimi==14:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="oak_planks")
            elif blocksecimi==15:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="dark_oak_planks")
            elif blocksecimi==16:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="glass")
            elif blocksecimi==17:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="chiseled_deepslate")
            elif blocksecimi==18:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="deepslate_bricks")
            elif blocksecimi==19:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="nether_bricks")
            elif blocksecimi==20:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="netherite_block")
            elif blocksecimi==20:
                belirteç=Entity(model="cube",parent=camera.ui,scale=0.4 ,color=color.white,position=(0.7,-0.35),rotation=(-5,-10,-10), texture="burhan1")

            






oyuncu=FirstPersonController()
Sky()
for x in range(30):

    for y in range(30):
        block=Block(color=color.green,position=(x,0,y))

app.run()
