import heapq
from str_const import UsersColumns
import const


def get_raw_top(players): # возращает список таплов из id и winscounter лучших игроков
    raw_top = heapq.nlargest(const.top_range, players, key=lambda e:e[UsersColumns.winscounter.value.number])
    top = []
    for player in raw_top:
        top.append((player[UsersColumns.id.value.number], player[UsersColumns.winscounter.value.number]))
    return top

#def get_top(raw_top, messenger):
#    ids = str(raw_top[0][0])
#    for i in range(1, len(raw_top)):
#        ids += "," + str(raw_top[i][0])
#    links = link_name(ids, messenger)


#def link_name(user_id, messenger, name_case = "nom"):
#    users = messenger.vk.users.get(user_ids = user_id, name_case = name_case)
#    links = []
#    for i in users:
#        links.append("[id" + str(i['id']) + "|" + i["first_name"] + " " + i["last_name"] + "]")
#    return links


class Top():
    def __init__(self, players, messenger):
        self.raw_top = get_raw_top(players)
    #    self.top = get_top(self.raw_top, messenger)

    #def change_top(self):
    #    pass





