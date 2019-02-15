import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api import VkUpload
import random
import requests

import time
fascist =('............/´¯/)...................(\¯`\\ \n'
'.........../...//....ЗДОХНИ...\\...\\\n'
'........../...//......ФАШИСТ...\\...\\\n'
'...../´¯/..../´¯\.ЕБАНЫй../¯` \....\¯`\\ \n'
'.././.../..../..../.|_......._|.\....\....\...\...\\ \n'
'(.(....(....(..../..)..)…...(..(.\....)....)....)...)\n'
'.\................\/.../......\...\/................/\n'
'..\.................. /.........\................../')

def randompic():
    import vk_api
    import random
    login, password = '79217662563', 'rendex1337'
    vk_session1 = vk_api.VkApi(login, password)
    try:
        vk_session1.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
    vk1 = vk_session1.get_api()
    stra = str(vk1.photos.get(owner_id='-84187544', album_id='wall', offset=1, count='1'))
    numsof = int(stra[10:15])
    str1 = str(
        vk1.photos.get(owner_id='-84187544', album_id='wall', offset=random.randint(0, numsof - 1),
                       count='1'))
    star_serch = str1.rfind("'id': ") + 6
    end_serch = str1.rfind(", 'album_id'")
    retrik = ('photo-84187544' + '_' + str1[star_serch:end_serch])
    return retrik


def miniature(id, peer):
    start_miniature=peer.rfind(id)
    miniature = peer.find("'photo_50': '", start_miniature)+int(len("'photo_50': '"))
    end_miniature = peer.find("'", miniature)
    return peer[miniature:end_miniature]




def whos(peer):
    i=1
    start_sername=0
    start_serfam=0
    list_of_people = []
    startserchnum = peer.find("'count': ")+9
    endserchnum = peer.find(", 'profiles'")
    counter = int(peer[startserchnum:endserchnum])
    if int(peer.find('groups')) != -1:
        counter = counter -1

    while i <= counter:
        start_sername=peer.find("'first_name': '",start_sername)+15
        end_sername = peer.find("', ", start_sername)
        start_serfam = peer.find("'last_name': '", start_serfam)+14
        end_sernfam = peer.find("', ", start_serfam)
        name = (peer[start_sername:end_sername] + ' ' + peer[start_serfam:end_sernfam])
        list_of_people.append(name)
        i += 1
    return random.choice(list_of_people)

def answers_who():
    answ = ['Я думаю, что ', 'С уверенностью могу сказать, что ', 'Мне кажется, ', 'С помощью фактов и логики я доказал, что ',
            'Я провел мысленный экперимент и выяснил, что ', 'Здравый смысл говорит мне о том, что ', 'Как показывает практика, ',
            'Используя диалектическую логику я пришел к выводу, что ', 'Как по мне, то ']
    return random.choice(answ)

def main():
    session = requests.Session()
    vk_session = vk_api.VkApi(token='48188f4a5e220530bddeb1bdbdec4bc89384e4a251b62275005f9784f98429f2e86b1c246fbd4acb794c9')
    longpoll = VkBotLongPoll(vk_session, '178122731')
    vk = vk_session.get_api()
    upload = VkUpload(vk_session)

    for event in longpoll.listen():

        if event.type == VkBotEventType.MESSAGE_NEW:

            if event.obj.text.lower().find('не одобря') == -1 and event.obj.text.lower().find('одобря')!=-1:
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message=('МЫ НЕ ОДОБРЯЕМ'))
            if event.obj.text == '!пикча':
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, attachment=randompic())
            if event.obj.text == '14':
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="88")
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="МЫ НЕ ОДОБРЯЕМ")
            if event.obj.text.lower().find('!кто') != (-1):
                per = str(event.obj.peer_id)
                peer = str(vk.messages.getConversationMembers(peer_id=per))
                strl = event.obj.text
                while strl.find('&quot;') > 0:
                    i = strl.find('&quot;')
                    strl = strl[:i] + '"' + strl[i + len('&quot;'):]
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message=(answers_who() + whos(peer) + strl[(strl).lower().find('!кто')+4:]))
            if event.obj.text.lower().find('фаши') != (-1):
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message=(fascist))
            if event.obj.text == '!монетка':
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="Орёл")
            if event.obj.text.lower().find('надеко') != (-1):
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, message="Надеко - мразь")
            if random.randint(1, 100) == 1:
                miniature_avatar = miniature(str(event.obj.from_id), str(vk.messages.getConversationMembers(peer_id=event.obj.peer_id)))
                image_url = miniature_avatar
                attachments = []
                image = session.get(image_url, stream=True)
                photo = upload.photo_messages(photos=image.raw)[0]

                attachments.append(
                    'photo{}_{}'.format(photo['owner_id'], photo['id'])
                )
                vk.messages.send(peer_id=event.obj.peer_id, random_id=0, attachment=','.join(attachments))



if __name__ == '__main__':

    main()
