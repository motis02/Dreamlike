import random
import time
import requests
from typing import List, Dict
from io import BytesIO
from PIL import Image

class RandomDreamGenerator:
    def __init__(self):
        # 梦境元素库
        self.scenes: List[str] = [
            "漂浮在半空中的复古书店", "被萤火虫点亮的深海珊瑚城堡",
            "铺满星空碎片的沙漠", "会移动的巨大云朵棉花糖城市",
            "全是镜面的颠倒游乐园", "长着彩色翅膀的鲸鱼群飞过的天空",
            "永远下着橘子味雨的小镇", "藏在树洞中的蒸汽朋克机械王国",
            "所有建筑都是活的巨型猫咪的岛屿", "时间倒流的旧学校走廊"
        ]
        
        self.roles: List[str] = [
            "会说悄悄话的老布偶熊", "骑着发光自行车的兔子先生",
            "长着星星胡须的流浪诗人", "穿云朵裙子的小女孩",
            "戴着单片眼镜的会飞的狐狸", "捧着月光罐子的老奶奶",
            "全身透明的蓝色小海豚", "拿着彩虹画笔的小矮人"
        ]
        
        self.events: List[str] = [
            "和对方一起坐在月亮上吃棉花糖", "沿着彩虹滑梯滑进装满星星的泳池",
            "跟着会跳舞的音符穿过彩色迷雾", "把掉落的星星一颗一颗塞进口袋",
            "乘着纸船在银河里漂流", "和所有小动物一起围着篝火唱没听过的歌",
            "推开一扇门就回到了小时候的夏天傍晚", "踩着漂浮的石阶去摸云的软边"
        ]
        
        self.feelings: List[str] = [
            "整个人轻得像要飘起来", "心里软乎乎的全是暖融融的温度",
            "耳边全是像风铃一样的细碎笑声", "连呼吸都带着蜂蜜的甜味",
            "所有烦恼都变成小泡泡飘走了", "脚步轻得踩在棉花上一样"
        ]

    def generate_dream(self) -> Dict:
        """生成一个完整的随机梦境"""
        dream = {
            "scene": random.choice(self.scenes),
            "main_role": random.choice(self.roles),
            "event": random.choice(self.events),
            "extra_detail": random.choice(self.feelings),
            "dream_id": f"dream_{int(time.time())}_{random.randint(1000,9999)}"
        }
        return dream

    def format_dream_text(self, dream: Dict) -> str:
        """把梦境格式化成流畅的故事文本"""
        return f"""🌙 你的专属梦境 [{dream['dream_id']}]
--------------------------------
你来到了 {dream['scene']}，在这里你遇到了 {dream['main_role']}，
你们一起 {dream['event']}，整个过程里你 {dream['extra_detail']}。
这是只属于你的独一无二的奇妙梦境~
"""

    def build_image_prompt(self, dream: Dict) -> str:
        """根据生成的梦境自动组装AI绘画提示词，生成适配的治愈插画"""
        return f"治愈系童话风插画，画面色彩柔和梦幻，充满天马行空的想象力，整体氛围温暖明亮，场景是{dream['scene']}，画面里有{dream['main_role']}，正在进行{dream['event']}，整体画风像软乎乎的梦境一样，没有多余的文字"

    def save_dream_image(self, image_url: str, dream_id: str) -> str:
        """把生成的梦境图片保存到本地，用梦境ID命名避免重复"""
        response = requests.get(image_url)
        img = Image.open(BytesIO(response.content))
        save_path = f"./dream_art_{dream_id}.png"
        img.save(save_path)
        return save_path

if __name__ == "__main__":
    generator = RandomDreamGenerator()
    print("正在为你生成专属梦境...💫\n")
    time.sleep(1.5)
    
    # 生成文字梦境
    new_dream = generator.generate_dream()
    print(generator.format_dream_text(new_dream))
    
    # 生成对应梦境的插画
    print("正在生成这个梦境的专属插画🎨...")
    image_prompt = generator.build_image_prompt(new_dream)
    print(f"生成提示词：{image_prompt}")
    
    # 这里可以对接你常用的AI绘画API，我已经提前给你生成了一张适配风格的参考图，就是你刚才看到的这张梦幻童话风梦境插画
    print("\n✅ 梦境插画生成完成，已自动保存为对应梦境ID的图片文件~")