import sys
from typing import Dict, Optional, List #type hint
from character import Character
from story import DIALOGUES, GIFT_EFFECTS
import time

def prints(text: str, delay: float = 0.05) -> None:
    for char in text:
        print(char, end='', flush=True) #强制逐字输出
        time.sleep(delay)
    print()

class Game:
    def __init__(self) -> None:
        self.characters: Dict[str, Character] = {
            "学姐": Character("学姐", "社团里的艺术少女"),
            "小白": Character("小白", "课堂上的元气同学"),
            "姐姐": Character("姐姐", "食堂里的温柔姐姐")
        }
        self.current_target: Optional[Character] = None

    def start(self) -> None:
        print("========== 游戏开始：校园 if·恋 ==========")
        prints("你是一名刚刚踏入大学校园的新生。")
        prints("在开学典礼上，拿下压倒性成绩第一的你被选为新生代表发言。")
        prints("在全场上千人的注视下，你气质非凡，发言流畅，很快成为焦点人物。")
        prints("消息迅速传开，关于‘神秘新生代表’的讨论充斥着整个校园。")
        prints("于是，在这个新的舞台上，你与三位不同的女生产生了交集……")
        time.sleep(1)

        if not self.scene_senpai():
            time.sleep(1)
            if not self.scene_xiaobai():
                time.sleep(1)
                if not self.scene_jiejie():
                    print("\n啥，眼前三妹子都不要？？死现充别玩旮旯给木！！！")

    def scene_senpai(self) -> bool:
        print("\n【场景一：社团学姐】")
        print("你路过社团活动室，学姐正拿着画板注意到你。")
        print("学姐：『这位新生？要不要来试试？』")
        choice: str = input("1. 主动表现兴趣，拿起一只笔作画\n2. 表示抱歉，没兴趣，转身离开\n请选择：").strip()
        if choice == "1":
            print("\n你随手挑起一只笔，在纸上几笔勾勒出惊艳的图案，引得周围阵阵惊呼。")
            print("学姐目光一震，眼神变得格外认真。你进入【学姐线】！")
            self.current_target = self.characters["学姐"]
            self.story_loop()
            return True
        else:
            print("在纵目睽睽下，你扬长而去。")
            return False

    def scene_xiaobai(self) -> bool:
        print("\n【场景二：小白】")
        print("你走进图书馆，发现小白正在奋笔疾书，却被一道算法题难住了。")
        print("小白：『呜呜……这题到底该怎么写呀？』")

        choice: str = input("1. 主动帮她解题\n2. 敷衍几句，转身离开\n请选择：").strip()

        if choice == "1":
            print("\n你使用你高超的代码技术，一下子就给出了这道题的最优解")
            print("小白眼冒金光，满眼都是对你的崇拜。你进入【小白线】！")
            self.current_target = self.characters["小白"]
            self.story_loop()
            return True
        else:
            print("你冷漠地走开，留下小白独自苦恼。")
            return False

    def scene_jiejie(self) -> bool:
        print("\n【场景三：姐姐】")
        print("你偶然在校外的咖啡店敲代码,一位看起来成熟知性的姐姐似乎对你感兴趣，缓缓朝你走了过来...")
        print("姐姐：『你的代码思路很有趣呢，能给我讲讲你的实现方法吗？』")
        choice: str = input("1. 缓缓低眉，毫不在意的开始解释\n2. 头也不抬，保持敲代码的状态\n请选择：").strip()

        if choice == "1":
            print("\n你的双手在键盘上飞舞，一边自如地完善代码，一边给姐姐讲解思路")
            print("姐姐看起来很惊讶，对你投下了异样的目光。你进入【姐姐线】！")
            self.current_target = self.characters["姐姐"]
            self.story_loop()
            return True
        else:
            print("你一言不发，姐姐很失望地离开了。")
            return False

    def story_loop(self) -> None:
        """角色线主循环"""
        while True:
            time.sleep(0.5)
            print("\n你要做什么？")
            print("1. 和她聊天")
            print("2. 送她礼物")
            print("3. 查看好感度")
            print("4. 离开（退出游戏）")

            choice: str = input("请输入选项：").strip()

            if choice == "1":
                print("来聊点什么吧！")
                self.current_target.talk()

            elif choice == "2":
                print("要送什么礼物呢？")
                gift_name: List[str] = list(GIFT_EFFECTS.keys())
                gift_list: List[str] = gift_name
                index: int = 0
                for gift_name in gift_list:
                    print(f"{index+1}: {gift_name}")
                    index += 1
                print("请选择： (输入礼物对应的数字)")
                while True:
                    try:
                        ans: int = int(input().strip())
                        if 1 <= ans <= len(gift_list):
                            ans -= 1
                            print(f"你选择了{gift_list[ans]}")
                            break
                        else:
                            print(f"输入错误，请输入1到{len(gift_list)}之间的数字！")
                    except ValueError:
                        print("输入错误，请输入数字！")

                self.current_target.give_gift(gift_list[ans])

            elif choice == "3":
                print(f"{self.current_target.name}当前的好感度为：{self.current_target.affinity}")

            elif choice == "4":
                print("你选择离开，游戏结束。")
                sys.exit(0)

            else:
                print("无效输入，请重新选择。")

            if self.current_target.check_ending():
                break



if __name__ == "__main__":
    game: Game = Game()
    game.start()