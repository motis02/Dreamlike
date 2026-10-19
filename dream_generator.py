import random
import time
from typing import List, Dict

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

if __name__ == "__main__":
    generator = RandomDreamGenerator()
    print("正在为你生成专属梦境...💫\n")
    time.sleep(1.5)
    new_dream = generator.generate_dream()
    print(generator.format_dream_text(new_dream))