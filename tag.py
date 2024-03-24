HighTag = ["高级资深干员", "资深干员"]
RareTag = ["特种干员", "位移", "快速复活", "削弱", "爆发", "控场", "召唤", "支援"]
TeZhong = ["削弱", "控场"]
TeZhong_1 = ["生存", "减速"]
WeiYi = ["重装干员", "防护", "输出", "减速"]
KuaiHuo = ["削弱", "控场"]
XueRuo = ["群攻", "辅助干员", "近战位"]
BaoFa = ["术师干员", "群攻"]
KongChang = ["减速", "先锋干员", "费用回复"]
ZhiYuan = ["辅助干员", "生存", "先锋干员", "费用回复"]
ZhiYuan_1 = ["近战位", "近卫干员", "输出", "远程位", "医疗干员", "治疗"]
OrdinaryTag = ["治疗", "减速", "输出", "防护", "生存"]
ZhiLiao = ["先锋干员", "费用回复", "辅助干员"]
ShuChu = ["辅助干员", "群攻", "重装干员"]
FangHu = ["近卫干员", "术师干员", "群攻", "远程位"]
ShengCun = ["防护", "重装干员", "辅助干员"]


# BottomTag = ["近战位", "远程位", "近卫干员", "狙击干员", "重装干员", "医疗干员", "辅助干员", "术师干员", "先锋干员",
#             "费用回复"]


def Search(i, sum, tag, tagArr, click):
    for n in range(6):
        for m in range(sum):
            if tag[n] == tagArr[m]:
                con(click, i, n)
                return


def con(click, i, n):
    click[0] = 1
    click[i + 1] = 1
    click[n + 1] = 1


# 出现“资深干员”和“高级资深干员时”自选
def Six_Five_Stars(tag, click):
    for i in range(2):
        for j in range(2):
            if tag[j] == HighTag[i]:
                click[0] = -1


# 选择2个稀有tag(必出5星)
def Five_Stars(tag, click):
    for i in range(6):
        for j in range(8):
            if tag[i] == RareTag[j]:
                if j == 0:
                    Search(i, 2, tag, TeZhong, click)
                    return
                if j == 1:
                    Search(i, 4, tag, WeiYi, click)
                    return
                if j == 2:
                    Search(i, 2, tag, KuaiHuo, click)
                    return
                if j == 3:
                    Search(i, 3, tag, XueRuo, click)
                    return
                if j == 4:
                    Search(i, 2, tag, BaoFa, click)
                    if click[0] == 1:
                        return
                    for n in range(6):
                        if tag[n] == "狙击" or tag[n] == "远程位":
                            for m in range(6):
                                if tag[m] == "输出":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1
                    return
                if j == 5:
                    Search(i, 3, tag, KongChang, click)
                    return
                if j == 6:
                    click[0] = 1
                    click[i + 1] = 1
                    return
                if j == 7:
                    Search(i, 4, tag, ZhiYuan, click)


# 选择1个稀有tag+1个普通tag(可能出5星或4星)
def Five_Four_Stars(tag, click):
    for i in range(6):
        for j in range(8):
            if tag[i] == RareTag[j]:
                if j == 0:
                    for n in range(6):
                        if tag[n] == "输出":
                            con(click, i, n)
                            return
                if j == 3:
                    for n in range(6):
                        if tag[n] == "狙击":
                            con(click, i, n)
                            return
                if j == 4:
                    for n in range(6):
                        if tag[n] == "输出":
                            con(click, i, n)
                            return
                if j == 5:
                    for n in range(6):
                        if tag[n] == "远程位":
                            con(click, i, n)
                            return
                if j == 7:
                    Search(i, 6, tag, ZhiYuan_1, click)


# 选择1个稀有tag(可能出4星或5星)
def Four_Five_Stars(tag, click):
    for i in range(6):
        for j in range(8):
            if tag[i] == RareTag[j]:
                click[0] = 1
                click[i + 1] = 1


# 选择1个稀有tag+1个普通tag(必出4星)
def Four_Stars(tag, click):
    for i in range(6):
        for j in range(8):
            if tag[i] == RareTag[j]:
                if j == 0:
                    for n in range(6):
                        if tag[n] == "防护":
                            con(click, i, n)
                            return
                if j == 2:
                    for n in range(6):
                        if tag[n] == "防护" or tag[n] == "输出":
                            con(click, i, n)
                            return
                if j == 3:
                    for n in range(6):
                        if tag[n] == "术师干员":
                            con(click, i, n)
                            return
                    for n in range(6):
                        if tag[n] == "狙击干员":
                            for m in range(6):
                                if tag[m] == "输出":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1
                                    return
                if j == 4:
                    for n in range(6):
                        if tag[n] == "近战位":
                            for m in range(6):
                                if tag[m] == "近卫干员" or tag[m] == "输出":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1
                                    return
                if j == 5:
                    for n in range(6):
                        if tag[n] == "术师干员" or tag[n] == "输出":
                            con(click, i, n)


# 选择2个普通tag(可能出4星或5星)
def Four_Five_Stars_1(tag, click):
    for i in range(6):
        for j in range(5):
            if tag[i] == OrdinaryTag[j]:
                if j == 0:
                    for n in range(6):
                        if tag[n] == "减速":
                            con(click, i, n)
                            return
                if j == 1:
                    for n in range(6):
                        if tag[n] == "近战位" or tag[n] == "术师干员":
                            con(click, i, n)
                            return
                    for n in range(6):
                        if tag[n] == "狙击干员":
                            for m in range(6):
                                if tag[m] == "输出":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1
                                    return
                if j == 4:
                    for n in range(6):
                        if tag[n] == "远程位":
                            con(click, i, n)


# 选择2个普通tag(可能出4星)
def Four_Stars_1(tag, click):
    for i in range(6):
        for j in range(5):
            if tag[i] == OrdinaryTag[j]:
                if j == 0:
                    Search(i, 3, tag, ZhiLiao, click)
                    return
                if j == 1:
                    for n in range(6):
                        if tag[n] == "输出":
                            for m in range(6):
                                if tag[m] == "近卫干员" or tag[m] == "近战位":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1
                                    return
                        if tag[n] == "群攻":
                            for m in range(6):
                                if tag[m] == "狙击干员" or tag[m] == "术师干员":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1
                                    return
                if j == 4:
                    for n in range(6):
                        if tag[n] == "输出":
                            for m in range(6):
                                if tag[m] == "狙击" or tag[m] == "远程位":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1


# 选择2个普通tag(小几率出5星)
def Five_Stars_1(tag, click):
    for i in range(6):
        for j in range(5):
            if tag[i] == OrdinaryTag[j]:
                if j == 0:
                    for n in range(6):
                        if tag[n] == "术师干员" or tag[n] == "输出":
                            con(click, i, n)
                            return
                if j == 1:
                    for n in range(6):
                        if tag[n] == "术师干员":
                            for m in range(6):
                                if tag[m] == "输出":
                                    click[0] = 1
                                    click[i + 1] = 1
                                    click[n + 1] = 1
                                    click[m + 1] = 1
                                    return
                if j == 2:
                    Search(i, 3, tag, ShuChu, click)
                    return
                if j == 3:
                    Search(i, 4, tag, FangHu, click)
                    return
                if j == 4:
                    Search(i, 3, tag, ShengCun, click)

