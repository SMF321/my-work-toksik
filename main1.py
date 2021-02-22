from telethon import TelegramClient
from datetime import datetime ,timedelta
import common

api_id = common.api_id
api_hash = common.api_hash
client = TelegramClient('smf', api_id, api_hash)

async def main():

    promezjutokilinet = int(input('Хочешь вборку новостей за один день или за промежуток?\n1)Один день\n2)Промежуток\nВвод:'))
    dialogs = await client.get_dialogs()
    viborkanala = int(input('Скакого канала хотите просмотреть новости?\n1)Интернет-Розыск\n2)Информация опасносте\n3)Со всех источников!\nВвод:'))
    if viborkanala == 1:
    # Интернет-Розыск
        dialogid = -1001200803575
        for dlg in dialogs:
            if dlg.id == dialogid:
                imya = dlg
        msgs = await client.get_messages(imya, limit=300)
        main2(promezjutokilinet,msgs)
    elif viborkanala == 2:
        dialogid = -1001018448328
        for dlg in dialogs:
            if dlg.id == dialogid:
                imya = dlg
        msgs = await client.get_messages(imya, limit=300)
        main2(promezjutokilinet,msgs)
    elif viborkanala == 3:
        dialogi = [-1001200803575,-1001018448328]
        for dialogid in dialogi:
            for dlg in dialogs:
                if dlg.id == dialogid:
                    imya = dlg
            msgs = await client.get_messages(imya, limit=300)
            if promezjutokilinet == 1:
                daymes = int(input('Если один день, введите, интересующий Вас, день(какое числа)\nВвод:'))
                monthmes = int(input('Введите, интересующий Вас, месяц(какой месяца)\nВвод:'))
                yearmes = int(input('Введите, интересующий Вас, год(какой год)\nВвод:'))
                createmessage(msgs, daymes, monthmes, yearmes)
            elif promezjutokilinet == 2:
                daymes1 = int(input('Если промежуток, введите, интересующий Вас, день(с какого числа)\nВвод:'))
                monthmes1 = int(input('Введите, интересующий Вас, месяц(с какого месяца)\nВвод:'))
                yearmes1 = int(input('Введите, интересующий Вас, год(с какого года)\nВвод:'))
                daymes2 = int(input('Введите, интересующий Вас, день(по какое число)\nВвод:'))
                monthmes2 = int(input('Введите, интересующий Вас, месяц(по какой месяц)\nВвод:'))
                yearmes2 = int(input('Введите, интересующий Вас, год(по какой год)\nВвод:'))
                date1 = datetime(yearmes1, monthmes1, daymes1)
                date2 = datetime(yearmes2, monthmes2, daymes2 + 1)
                while date1 < date2:
                    daymes = date1.day
                    monthmes = date1.month
                    yearmes = date1.year
                    date1 = date1 + timedelta(days=1)
                    createmessage(msgs, daymes, monthmes, yearmes)
            else:
                print('Программа не будет работать, обещаю!!!')
    else:
        print('Программа не будет работать, обещаю!!!')

def main2(promezjutokilinet,msgs):
    if promezjutokilinet == 1:
        daymes = int(input('Если один день, введите, интересующий Вас, день(какое числа)\nВвод:'))
        monthmes = int(input('Введите, интересующий Вас, месяц(какой месяца)\nВвод:'))
        yearmes = int(input('Введите, интересующий Вас, год(какой год)\nВвод:'))
        createmessage(msgs, daymes, monthmes, yearmes)
    elif promezjutokilinet == 2:
        daymes1 = int(input('Если промежуток, введите, интересующий Вас, день(с какого числа)\nВвод:'))
        monthmes1 = int(input('Введите, интересующий Вас, месяц(с какого месяца)\nВвод:'))
        yearmes1 = int(input('Введите, интересующий Вас, год(с какого года)\nВвод:'))
        daymes2 = int(input('Введите, интересующий Вас, день(по какое число)\nВвод:'))
        monthmes2 = int(input('Введите, интересующий Вас, месяц(по какой месяц)\nВвод:'))
        yearmes2 = int(input('Введите, интересующий Вас, год(по какой год)\nВвод:'))
        date1 = datetime(yearmes1, monthmes1, daymes1)
        date2 = datetime(yearmes2, monthmes2, daymes2+1)
        while date1 < date2:
            daymes = date1.day
            monthmes = date1.month
            yearmes = date1.year
            date1 = date1 + timedelta(days=1)
            createmessage(msgs,daymes,monthmes,yearmes)
    else:
        print('Программа не будет работать, обещаю!!!')

def createmessage(msgs,daymes,monthmes,yearmes):
    for i in range(300):
        if msgs[i].date.day == daymes:
            if msgs[i].date.month == monthmes:
                if msgs[i].date.year == yearmes:
                    print(msgs[i].message)
                    print('----------------------------------------------------')

with client:
    client.loop.run_until_complete(main())

