import pyautogui
import time
import random
py = pyautogui

def autoclick(x, y):
    for count in range(1):
        py.leftClick(x, y)

def lock_in():
    for count in range(2):
        py.leftClick(1290, 1089)

def select(x, y):
    autoclick(x, y)
    time.sleep(1)
    lock_in()

agents = ["Brimstone", "Viper", "Omen", "Killjoy", "Cypher", "Sova", "Sage", "Phoenix", "Jett",
 "Reyna", "Raze", "Breach", "Skye", "Yoru", "Astra", "Kayo", "Chamber", "Neon"]

random_agent = random.choice(agents)
print("Your Agent is", random_agent)


if random_agent == "Skye":
    select(1400, 1344)
elif random_agent == "Jett":
    select(1400, 1233)
elif random_agent == "Omen":
    select(840, 1339)
elif random_agent == "Astra":
    select(835, 1232)
elif random_agent == "Breach":
    select(947, 1226)
elif random_agent == "Phoenix":
    select(948, 1339)
elif random_agent == "Brimstone":
    select(1055, 1218)
elif random_agent == "Raze":
    select(1062, 1344)
elif random_agent == "Chamber":
    select(1172, 1230)
elif random_agent == "Reyna":
    select(1174, 1338)
elif random_agent == "Cypher":
    select(1281, 1231)
elif random_agent == "Sage":
    select(1287, 1339)
elif random_agent == "Kayo":
    select(1503, 1233)
elif random_agent == "Sova":
    select(1503, 1341)
elif random_agent == "Killjoy":
    select(1616, 1236)
elif random_agent == "Viper":
    select(1620, 1343)
elif random_agent == "Neon":
    select(1729, 1233)
elif random_agent == "Yoru":
    select(1730, 1343)

