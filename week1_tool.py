name = input("请输入你的名字：")
power_level = int(input("请输入你的力量值: "))

if power_level >888:
    print(f"{name},能量充足，准备战斗！")
else:
    print(f"{name},力量值不足，需要继续修炼！")