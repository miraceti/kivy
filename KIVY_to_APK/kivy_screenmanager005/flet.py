import flet
from flet import (
    UserControl, Page, Column, Row, icons,
    Container, Text, padding, alignment,
    LinearGradient,IconButton,GridView,
    transform, animation,colors,Stack,
    PieChart,PieChartSection,
        )
import flet as ft
from urllib.request import urlopen
import json

import datetime

version= " (v014g)"

#######################
urlexo1 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+count(pl_name)+as+nbe+from+ps+where+default_flag=1&format=json"
print(urlexo1)
data = json.loads(urlopen(urlexo1).read().decode("utf-8"))
# print(data)
data0=data[0]
# print(data0)
nb_exoplanets= data0['nbe']
print(nb_exoplanets)
######################
now = datetime.date.today()
y0 = now.year
print(y0)

############################################################
#data de champs multiples
# urlexo7 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
# pl_name,pl_bmasse,pl_bmassj,pl_rade,pl_radj,pl_dens,pl_orbper,pl_eqt,\
# hostname,st_spectype,st_mass,st_rad,st_teff,\
# releasedate,sy_dist,disc_year,disc_telescope,discoverymethod\
# +from+ps&format=json"

# list7 = json.loads(urlopen(urlexo7).read().decode("utf-8"))
# print("\nkeys : ",(list7[0]).keys())
# print("\nvalues : ",(list7[0]).values())
# print("\nitems : ",(list7[0]).items())
# dict_7_0 = list7[0]
#print("\nlist7 : ",list7)

#############################################################
#nombre de planetes par années
#nombre de planete par année
urlexoYD = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
pl_name,disc_year\
+from+ps&format=json"

listYD = json.loads(urlopen(urlexoYD).read().decode("utf-8"))
y0=y1=y2=y3=y4=y5=y6=y7=y8=y9=y10=0
now = datetime.date.today()
y0 = now.year
for planete in listYD:
    #print(planete['pl_name'])
    if planete['disc_year'] is None: 
        pass
    else:
        if planete['disc_year'] == y0 :
            #print(planete['pl_name'])
            y1+=1
        elif planete['disc_year'] == y0  -1 :
            #print(planete['pl_name'])
            y2+=1
        elif planete['disc_year'] == y0 - 2 :
            #print(planete['pl_name'])
            y3+=1
        elif planete['disc_year'] == y0 - 3 :
            #print(planete['pl_name'])
            y4+=1
        elif planete['disc_year'] == y0 - 4 :
            #print(planete['pl_name'])
            y5+=1
        elif planete['disc_year'] == y0 - 5 :
            #print(planete['pl_name'])
            y6+=1
        elif planete['disc_year'] == y0 - 6 :
            #print(planete['pl_name'])
            y7+=1
        elif planete['disc_year'] == y0 - 7 :
            #print(planete['pl_name'])
            y8+=1
        elif planete['disc_year'] == y0 - 8 :
            #print(planete['pl_name'])
            y9+=1
        else:
            y10+=1

print("nombre de planetes par année de découverte")            
print(str(y0 ),' : ',y1)
print(str(y0 - 1 ),' : ',y2)
print(str(y0 - 2 ),' : ',y3)
print(str(y0 - 3),' : ',y4)
print(str(y0 - 4),' : ',y5)
print(str(y0 - 5),' : ',y6)
print(str(y0 - 6),' : ',y7)
print(str(y0 - 7),' : ',y8)
print(str(y0 - 8),' : ',y9)
print(str(y0 - 9),' : ',y10)

#############################################################
#############################################################
#nombre de planetes par distances
urlexo0 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
pl_name,sy_dist\
+from+ps&format=json"

list0 = json.loads(urlopen(urlexo0).read().decode("utf-8"))

d10=d20=d30=d40=d50=d60=d70=d80=d90=d100=0
for planete in list0:
    #print(planete['pl_name'])
    if planete['sy_dist'] is None: 
        pass
    else:
        if planete['sy_dist'] < 10.00:
            #print(planete['pl_name'])
            d10+=1
        elif planete['sy_dist'] >= 10.00 and planete['sy_dist'] < 20.00:
            #print(planete['pl_name'])
            d20+=1
        elif (planete['sy_dist'] >= 20.00) and (planete['sy_dist']) < 30.00:
            #print(planete['pl_name'])
            d30+=1
        elif (planete['sy_dist'] >= 30.00) and (planete['sy_dist']) < 40.00:
            #print(planete['pl_name'])
            d40+=1
        elif (planete['sy_dist'] >= 40.00) and (planete['sy_dist']) < 50.00:
            #print(planete['pl_name'])
            d50+=1
        elif (planete['sy_dist'] >= 50.00) and (planete['sy_dist']) < 60.00:
            #print(planete['pl_name'])
            d60+=1
        elif (planete['sy_dist'] >= 60.00) and (planete['sy_dist']) < 70.00:
            #print(planete['pl_name'])
            d70+=1
        elif (planete['sy_dist'] >= 70.00) and (planete['sy_dist']) < 80.00:
            #print(planete['pl_name'])
            d80+=1
        elif (planete['sy_dist'] >= 80.00) and (planete['sy_dist']) < 90.00:
            #print(planete['pl_name'])
            d90+=1
        else:
            d100+=1

print("Nombre de planètes par bloc de distances 10 parsec")            
print(d10)
print(d20)
print(d30)
print(d40)
print(d50)
print(d60)
print(d70)
print(d80)
print(d90)
print(d100)

#liste des planetes les plus proches : 3
distmax = 100000
p1="vide"
p=0
planete_dist=[]
for planete in list0:
    if planete['sy_dist'] is None:
        pass
    else:
        p+=1
        planete_dist.append((planete['pl_name'], 
                             planete['sy_dist'], 
                             ))
        if planete['sy_dist'] < distmax:
            pl = planete['pl_name']#planete la plus proche 
            distmax = planete['sy_dist']

planete_la_plus_proche = pl
print("\nplanete la plus proche : ", pl)

#tri par ordre de distance
proche_list = sorted(planete_dist, key= lambda x: x[1])
print(proche_list[:3])

#entete tableau depart
col1=str("col01")
col2=str("col02")
col3=str("col03")

#entete tableau new
ncol1 = str("ncoll1")
ncol2 = str("ncoll2")
ncol3 = str("ncoll3")

################################################tableau 0
n0col01 = str("pl_name")
n0col02 = str("sy_dist")
n0col03 = ""

n0cel01 = proche_list[0][0]
n0cel02 = proche_list[0][1]
#n0cel03 = proche_list[0][2]

n0cel11 = proche_list[1][0]
n0cel12 = proche_list[1][1]
#n0cel13 = proche_list[1][2]

n0cel21 = proche_list[2][0]
n0cel22 = proche_list[2][1]
#n0cel23 = proche_list[2][2]
##########################################################


##################################################tableau 1
# n1col01 = str("pl_name")
# n1col02 = ""
# n1col03 = ""

# n1cel01 = proche_list[0][0]
# n1cel02 = proche_list[0][3]
# n1cel03 = proche_list[0][4]

# n1cel11 = proche_list[1][0]
# n1cel12 = proche_list[1][3]
# n1cel13 = proche_list[1][4]

# n1cel21 = proche_list[2][0]
# n1cel22 = proche_list[2][3]
# n1cel23 = proche_list[2][4]
#########################################################
planete_name_list = sorted(list0, key= lambda x: x['pl_name'])#créer une liste ordonné par nom
planete_name_list[0]

from operator import is_not
from functools import partial

planete_dist_list0 = list(filter(partial(is_not, None),planete_name_list))
keyValList = [None]
exampleSet = planete_dist_list0

#on retire les  sy_dist qui sont None
planete_dist_list1 = list(filter(lambda d: d['sy_dist'] not in keyValList, exampleSet))

#on tris la liste propre obtenue par sy_dist croissant
planete_dist_list2 = sorted(planete_dist_list1, key=lambda x: x['sy_dist'])

listpdl1=[]
cles=('pl_name','sy_dist')
for i in range(0,100):
    bigdict1=planete_dist_list2[i]
    subdict1={x: bigdict1[x] for x in cles if x in bigdict1}
    listpdl1.append(subdict1)
    i+=1

#suppression doublons
listpdl2=[dict(t) for t in {tuple(d.items()) for d in listpdl1}]

#tri par distance
listpdl3 = sorted(listpdl2, key=lambda d: d['sy_dist'])
planete_dist_list = listpdl3
print("\nles 5 planetes les plus proches : ",planete_dist_list[:5])

#################################################bouton 0
#planete les plus proches distance
plpp0_name=planete_dist_list[:10][0]['pl_name']
plpp0_dist=planete_dist_list[:10][0]['sy_dist']
plpp1_name=planete_dist_list[:10][1]['pl_name']
plpp1_dist=planete_dist_list[:10][1]['sy_dist']
plpp2_name=planete_dist_list[:10][2]['pl_name']
plpp2_dist=planete_dist_list[:10][2]['sy_dist']
plpp3_name=planete_dist_list[:10][3]['pl_name']
plpp3_dist=planete_dist_list[:10][3]['sy_dist']
plpp4_name=planete_dist_list[:10][4]['pl_name']
plpp4_dist=planete_dist_list[:10][4]['sy_dist']
plpp5_name=planete_dist_list[:10][5]['pl_name']
plpp5_dist=planete_dist_list[:10][5]['sy_dist']
plpp6_name=planete_dist_list[:10][6]['pl_name']
plpp6_dist=planete_dist_list[:10][6]['sy_dist']
plpp7_name=planete_dist_list[:10][7]['pl_name']
plpp7_dist=planete_dist_list[:10][7]['sy_dist']
plpp8_name=planete_dist_list[:10][8]['pl_name']
plpp8_dist=planete_dist_list[:10][8]['sy_dist']
plpp9_name=planete_dist_list[:10][9]['pl_name']
plpp9_dist=planete_dist_list[:10][9]['sy_dist']

#########################################################
################################################bouton 1
#planete methode decouverte nombre
urlexoMD = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
pl_name,discoverymethod\
+from+ps+order+by+pl_name+&format=json"

listMD = json.loads(urlopen(urlexoMD).read().decode("utf-8"))
print("listMD : ",listMD[:10])

discoverymethod_counts = {}
for track in listMD:
    method = track.get('discoverymethod')
    try:
        discoverymethod_counts[method]+=1
    except KeyError:
        discoverymethod_counts[method] = 1

print('COUNTS : ',discoverymethod_counts)

ordered_discoverymethod_counts_key = dict(sorted(discoverymethod_counts.items()))
print('KEYS : ',ordered_discoverymethod_counts_key)

ordered_discoverymethod_counts_value = sorted(discoverymethod_counts.items(), key=lambda x: x[1], reverse=True)
print('VALUES : ',ordered_discoverymethod_counts_value)
v = ordered_discoverymethod_counts_value
pmdn_0_name = v[0][0]
pmdn_0_count = v[0][1]
pmdn_1_name = v[1][0]
pmdn_1_count = v[1][1]
pmdn_2_name = v[2][0]
pmdn_2_count = v[2][1]
pmdn_3_name = v[3][0]
pmdn_3_count = v[3][1]
pmdn_4_name = v[4][0]
pmdn_4_count = v[4][1]
pmdn_5_name = v[5][0]
pmdn_5_count = v[5][1]
pmdn_6_name = v[6][0]
pmdn_6_count = v[6][1]
pmdn_7_name = v[7][0]
pmdn_7_count = v[7][1]
pmdn_8_name = v[8][0]
pmdn_8_count = v[8][1]
pmdn_9_name = v[9][0]
pmdn_9_count = v[9][1]

########################################################
###############################################bouton 2 
#graphique  calcule pourcentage
print("méthodes : ",v)
total_methode = sum(ordered_discoverymethod_counts_key.values())
print("total_methode : ",total_methode)
m0p = float("{:.2f}".format((v[0][1] / total_methode)*100))
m0n = v[0][0]
print("m0p :", m0p, '% pour la méthode ', str(m0n))
m1p = float("{:.2f}".format((v[1][1] / total_methode)*100))
m1n = v[1][0]
print("m1p :", m1p, '% pour la méthode ', str(m1n))
m2p = float("{:.2f}".format((v[2][1] / total_methode)*100))
m2n = v[2][0]
print("m2p :", m2p, '% pour la méthode ', str(m2n))
m3p = float("{:.2f}".format((v[3][1] / total_methode)*100))
m3n = v[3][0]
print("m3p :", m3p, '% pour la méthode ', str(m3n))
m4p = float("{:.2f}".format((v[4][1] / total_methode)*100))
m4n = v[4][0]
print("m4p :", m4p, '% pour la méthode ', str(m4n))
m5p = float("{:.2f}".format((v[5][1] / total_methode)*100))
m5n = v[5][0]
print("m5p :", m5p, '% pour la méthode ', str(m5n))
m6p = float("{:.2f}".format((v[6][1] / total_methode)*100))
m6n = v[6][0]
print("m6p :", m6p, '% pour la méthode ', str(m6n))
m7p = float("{:.2f}".format((v[7][1] / total_methode)*100))
m7n = v[7][0]
print("m7p :", m7p, '% pour la méthode ', str(m7n))
m8p = float("{:.2f}".format((v[8][1] / total_methode)*100))
m8n = v[8][0]
print("m8p :", m8p, '% pour la méthode ', str(m8n))
m9p = float("{:.2f}".format((v[9][1] / total_methode)*100))
m9n = v[9][0]
print("m9p :", m9p, '% pour la méthode ', str(m9n))
#autres
mautrep = float("{:.2f}".format(m4p+m5p+m6p+m7p+m8p+m9p))
mautren = "autres"
########################################################
###############################################bouton 3 
# planete_list =[]
# #suggestions=[         ft.AutoCompleteSuggestion(key="one 1", value="One"),]
# planete_list=[
#                     ft.AutoCompleteSuggestion(key="one 1", value="One"),
#                     ft.AutoCompleteSuggestion(key="two 2", value="Two"),
#                     ft.AutoCompleteSuggestion(key="three 3", value="Three"),
#                 ]
# data_p = [
#     {"name": f"Language {i}", "description": f"Description for language Description for language Description for language {i}"} 
#     for i in range(1, 5001)
# ]
# print(planete_name_list[0])

urlexo3 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
pl_name,pl_bmasse,pl_bmassj,pl_rade,pl_radj,pl_dens,pl_orbper,pl_eqt,\
hostname,st_spectype,st_mass,st_rad,st_teff,\
sy_dist,disc_year,disc_telescope,discoverymethod\
+from+ps+&format=json"

list3 = json.loads(urlopen(urlexo3).read().decode("utf-8"))
data_pSearch = list3

#######################################################
###############################################bouton 4 
urlexo4 = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
pl_name,disc_pubdate\
+from+ps+order+by+disc_pubdate+desc+&format=json"

list4 = json.loads(urlopen(urlexo4).read().decode("utf-8"))
planete_name_list1 = sorted(list4, key= lambda x: x['pl_name'])#créer une liste ordonné par nom
planete_name_list1[0]
data_p = planete_name_list1
print(data_p[1])
#on tris la liste propre obtenue par releasedate croissant
planete_dt_decouv_list = sorted(data_p, key=lambda x: x['disc_pubdate'],reverse=True)

print("les 5 planetes les plus recentes : ",planete_dt_decouv_list[:5])

listp1 = []
interesting_keys = ('pl_name','disc_pubdate')
for i in range(0,20):
    bigdict = planete_dt_decouv_list[i]
    subdict = {x: bigdict[x] for x in interesting_keys if x in bigdict}
    listp1.append(subdict)
    i+=1

print('\nsubdict:',subdict)
print('\nlistp1:',listp1)
#remode doubles
listp11 = [dict(t) for t in {tuple(d.items()) for d in listp1}]
#on tri par date
listp2= sorted(listp11, key=lambda d: d['disc_pubdate'], reverse=True)

planete_dt_decouv_list = listp2

#planete les plus recemment decouvertes
plpr0_name=planete_dt_decouv_list[:10][0]['pl_name']
plpr0_decouv=planete_dt_decouv_list[:10][0]['disc_pubdate']
plpr1_name=planete_dt_decouv_list[:10][1]['pl_name']
plpr1_decouv=planete_dt_decouv_list[:10][1]['disc_pubdate']
plpr2_name=planete_dt_decouv_list[:10][2]['pl_name']
plpr2_decouv=planete_dt_decouv_list[:10][2]['disc_pubdate']
plpr3_name=planete_dt_decouv_list[:10][3]['pl_name']
plpr3_decouv=planete_dt_decouv_list[:10][3]['disc_pubdate']
plpr4_name=planete_dt_decouv_list[:10][4]['pl_name']
plpr4_decouv=planete_dt_decouv_list[:10][4]['disc_pubdate']
plpr5_name=planete_dt_decouv_list[:10][5]['pl_name']
plpr5_decouv=planete_dt_decouv_list[:10][5]['disc_pubdate']
plpr6_name=planete_dt_decouv_list[:10][6]['pl_name']
plpr6_decouv=planete_dt_decouv_list[:10][6]['disc_pubdate']
plpr7_name=planete_dt_decouv_list[:10][7]['pl_name']
plpr7_decouv=planete_dt_decouv_list[:10][7]['disc_pubdate']
plpr8_name=planete_dt_decouv_list[:10][8]['pl_name']
plpr8_decouv=planete_dt_decouv_list[:10][8]['disc_pubdate']
plpr9_name=planete_dt_decouv_list[:10][9]['pl_name']
plpr9_decouv=planete_dt_decouv_list[:10][9]['disc_pubdate']
#######################################################
###############################################bouton 5 


#######################################################
#############################################################

class Exoplanet(Stack):
    

    def hover_animation(self, e):
        if e.data == 'true':
            e.control.content.controls[2].offset = transform.Offset(0, 0)
            e.control.content.controls[2].opacity = 1.0
            e.control.update()
        else:
            e.control.content.controls[2].offset = transform.Offset(0, 1)
            e.control.content.controls[2].opacity = 0.0
            e.control.update()

    def change_icon(self, e):
        if e.control.selected != True:
            e.control.selected = True
            e.control.icon_color = 'white'
            e.control.update()
        else:
            e.control.selected = False
            e.control.icon_color = 'white54'
            e.control.update()

    def icon(self, name, color, selected):
        return IconButton(
            icon=name,
            icon_size=18,
            icon_color=color,
            selected=selected,
            on_click=lambda e:self.change_icon(e),
        )

    def highlight_link(self,e):
        e.control.style.color = ft.colors.BLUE
        e.control.update()

    def unhighlight_link(self,e):
        e.control.style.color = None
        e.control.update()

    def MainContainer(self):
        self.main =Container(
            width=350, height=700, bgcolor='black', 
            border_radius=35, padding=4,
        )

        self.main_col = Column()

        self.green_container = Container(
            width=self.main.width,
            height=self.main.height * 0.70,
            border_radius=30,
            gradient=LinearGradient(
                begin=alignment.top_left,
                end=alignment.bottom_right,
                colors=["#01171c","#7de3fa"],
            ),

        )

        # self.notification = self.icon(icons.NOTIFICATIONS, 'white54', True)
        # self.hide = self.icon(icons.HIDE_SOURCE, 'white54', False)
        # self.chat = self.icon(icons.CHAT_ROUNDED, 'white54', False)


        # self.icon_column=Column(
        #     alignment='center',
        #     spacing=5,
        #     controls=[
        #         self.notification,
        #         self.hide,
        #         self.chat,
        #     ],
        # )
        def table_0(e):
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[3].controls[0].content)
            #text {'value': '0', 'weight': 'bold', 'color': 'black', 'n': 'content'}

            self.table_container.content.controls[0].controls[0].content.visible=False
            self.table_container.content.controls[0].controls[0].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[1].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[2].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[3].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[4].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[5].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[6].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[7].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[8].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)
            self.table_container.content.controls[0].controls[9].content = Text("", size=14, weight='bold',color=colors.BLACK,theme_style=ft.TextThemeStyle.HEADLINE_SMALL)

            print(self.table_container.bgcolor)
            self.table_container.bgcolor = ft.colors.AMBER
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4]=Text("")
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4])
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].value="les 10 planetes les plus proches"
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].bgcolor=colors.BLACK
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].color=colors.AMBER

            self.table_container.content.controls[0].controls[0].content.value = ""

            #maj des valeurs
            print(self.table_container.content.controls[0].controls[0].content)
            print(self.table_container.content.controls[0].controls[1].content)

            #valeurs
            self.table_container.content.controls[0].controls[0].content.value = str(plpp0_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp0_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[1].content.value = str(plpp1_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp1_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[2].content.value = str(plpp2_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp2_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[3].content.value = str(plpp3_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp3_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[4].content.value = str(plpp4_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp4_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[5].content.value = str(plpp5_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp5_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[6].content.value = str(plpp6_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp6_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[7].content.value = str(plpp7_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp7_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[8].content.value = str(plpp8_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp8_dist)+str(' pcs')
            self.table_container.content.controls[0].controls[9].content.value = str(plpp9_name)+str('\t\t\t\t\t')+'Dist : '+str(plpp9_dist)+str(' pcs')
           
            print(self.table_container.content)

            Exoplanet.update(self)

        def table_1(e):
            #nom des colonnes
            # self.datatable.columns[0].label.value=str(ncol2)
            # print(self.datatable.bgcolor)
            # self.datatable.bgcolor = ft.colors.GREEN_200
            # self.datatable.columns[0].label.value=str(n1col01)
            # self.datatable.columns[1].label.value=str(n1col02)
            # self.datatable.columns[2].label.value=str(n1col03)

            #valeur des cellules par ligne
            # self.datatable.rows[0].cells[0].content.value = str(n1cel01)
            # self.datatable.rows[0].cells[1].content.value = str(n1cel02)
            # self.datatable.rows[0].cells[2].content.value = str(n1cel03)

            # self.datatable.rows[1].cells[0].content.value = str(n1cel11)
            # self.datatable.rows[1].cells[1].content.value = str(n1cel12)
            # self.datatable.rows[1].cells[2].content.value = str(n1cel13)

            # self.datatable.rows[2].cells[0].content.value = str(n1cel21)
            # self.datatable.rows[2].cells[1].content.value = str(n1cel22)
            # self.datatable.rows[2].cells[2].content.value = str(n1cel23)
            # print(self.datatable.rows[0].cells[1].content.value)

            # self.table_container.content.controls[0].controls[0].PieChart.visible=False
            print("pichart")
            print(self.table_container.content.controls[0])
            print(self.table_container.content.controls[0].controls[0])
            print(self.table_container.content.controls[0].controls[0].content)
            self.table_container.content.controls[0].controls[0].content.visible=False
            self.table_container.content.controls[0].controls[0].content = Text("",
                                                                                size=12, weight='bold',color=colors.BLACK,)

            print(self.table_container.bgcolor)
            self.table_container.bgcolor = ft.colors.GREEN_200
            self.table_container.alignment = ft.alignment.center
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4]=Text("")
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4])
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].value="Les 10 méthodes de détections"
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].bgcolor=colors.BLACK
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].color=colors.GREEN_200

            #valeurs
            self.table_container.content.controls[0].controls[0].content.value = str(pmdn_0_name)+str('\t\t\t\t\t')+' : '+str(pmdn_0_count)
            self.table_container.content.controls[0].controls[1].content.value = str(pmdn_1_name)+str('\t\t\t\t\t')+' : '+str(pmdn_1_count)
            self.table_container.content.controls[0].controls[2].content.value = str(pmdn_2_name)+str('\t\t\t\t\t')+' : '+str(pmdn_2_count)
            self.table_container.content.controls[0].controls[3].content.value = str(pmdn_3_name)+str('\t\t\t\t\t')+' : '+str(pmdn_3_count)
            self.table_container.content.controls[0].controls[4].content.value = str(pmdn_4_name)+str('\t\t\t\t\t')+' : '+str(pmdn_4_count)
            self.table_container.content.controls[0].controls[5].content.value = str(pmdn_5_name)+str('\t\t\t\t\t')+' : '+str(pmdn_5_count)
            self.table_container.content.controls[0].controls[6].content.value = str(pmdn_6_name)+str('\t\t\t\t\t')+' : '+str(pmdn_6_count)
            self.table_container.content.controls[0].controls[7].content.value = str(pmdn_7_name)+str('\t\t\t\t\t')+' : '+str(pmdn_7_count)
            self.table_container.content.controls[0].controls[8].content.value = str(pmdn_8_name)+str('\t\t\t\t\t')+' : '+str(pmdn_8_count)
            self.table_container.content.controls[0].controls[9].content.value = str(pmdn_9_name)+str('\t\t\t\t\t')+' : '+str(pmdn_9_count)
            
            print(self.table_container.content)

            Exoplanet.update(self)

        def table_2(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = '#18ACEF'

            #valeur des cellules par ligne
            self.datatable.rows[0].cells[1].content.value = "cel112"

            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4]=Text("")
            self.table_container.content.controls[0].controls[0].content= Text("")

            print(self.table_container.content)
            print(self.table_container.bgcolor)
            self.table_container.bgcolor = '#18ACEF'
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4])
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].value="Répartition des méthodes de détection"
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].bgcolor=colors.BLACK
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].color=colors.CYAN_200

            #valeurs
            self.table_container.content.controls[0].controls[0].content.value = ""
            self.table_container.content.controls[0].controls[1].content.value = ""
            self.table_container.content.controls[0].controls[2].content.value = ""
            self.table_container.content.controls[0].controls[3].content.value = ""
            self.table_container.content.controls[0].controls[4].content.value = ""
            self.table_container.content.controls[0].controls[5].content.value = ""
            self.table_container.content.controls[0].controls[6].content.value = ""
            self.table_container.content.controls[0].controls[7].content.value = ""
            self.table_container.content.controls[0].controls[8].content.value = ""
            self.table_container.content.controls[0].controls[9].content.value = ""
            
            #insertion chart
            labels = ["Oxygen", "Hydrogen", "Carbon_Dioxide", "Nitrogen"]
            values = [4500, 2500, 1053, 500]
            normal_title_style2 = ft.TextStyle(
                size=12, color=colors.BLACK, weight=ft.FontWeight.BOLD
            )

            chart=PieChart(
                sections=[
                    PieChartSection(
                        m0p,
                        title=str(m0n)+'\n'+str(m0p)+"%",
                        title_style=normal_title_style2,
                        color="#c27ce6",
                        radius=120,
                    ),
                    PieChartSection(
                        m1p,
                        title=str(m1n)+'\n'+str(m1p)+"%",
                        title_style=normal_title_style2,
                        color=colors.YELLOW,
                        radius=120,
                        title_position=0.7,
                    ),
                    PieChartSection(
                        m2p,
                        title=str(m2n)+' ' +str(m2p)+"%",
                        title_style=normal_title_style2,
                        color="#afbeed",
                        radius=120,
                        title_position=0.8,
                    ),
                    PieChartSection(
                        m3p,
                        title=str(m3n)+' ' +str(m3p)+"%",
                        title_style=normal_title_style2,
                        color=colors.GREEN,
                        radius=120,
                        title_position=0.8,
                    ),
                    PieChartSection(
                        mautrep,
                        title=str(mautren)+' ' +str(mautrep)+"%",
                        title_style=normal_title_style2,
                        color=colors.RED,
                        radius=120,
                        title_position=0.2,
                    ),
                    # PieChartSection(
                    #     m5p,
                    #     title=str(m5n)+'\n'+str(m5p)+"%",
                    #     title_style=normal_title_style,
                    #     color=colors.PINK,
                    #     radius=120,
                    # ),
                    # PieChartSection(
                    #     m6p,
                    #     title=str(m6n)+'\n'+str(m6p)+"%",
                    #     title_style=normal_title_style,
                    #     color=colors.CYAN,
                    #     radius=120,
                    # ),
                    # PieChartSection(
                    #     m7p,
                    #     title=str(m7n)+'\n'+str(m7p)+"%",
                    #     title_style=normal_title_style,
                    #     color=colors.ORANGE,
                    #     radius=120,
                    # ),
                    # PieChartSection(
                    #     m8p,
                    #     title=str(m8n)+'\n'+str(m8p)+"%",
                    #     title_style=normal_title_style,
                    #     color=colors.BROWN,
                    #     radius=120,
                    # ),
                    # PieChartSection(
                    #     m9p,
                    #     title=str(m9n)+'\n'+str(m9p)+"%",
                    #     title_style=normal_title_style,
                    #     color=colors.GREY,
                    #     radius=120,
                    # ),
                    
                    
                ],
                sections_space=0,
                center_space_radius=0,
                expand=True,
            )


            self.table_container.content.controls[0].controls[0].content = chart
            

            Exoplanet.update(self)

        

        def table_3(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.RED_200

            #valeur des cellules par ligne
            self.datatable.rows[0].cells[1].content.value = "cel112"

            self.table_container.content.controls[0].controls[0].content.visible=False
            self.table_container.content.controls[0].controls[0].content =Text(
                             "",size=12, weight='bold',color=colors.BLACK,bgcolor=colors.RED_200,
                             )
            print(self.table_container.bgcolor)
            self.table_container.bgcolor = ft.colors.RED_200
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4])
            normal_title_style = ft.TextStyle(
                size=20, color=colors.BLACK, weight=ft.FontWeight.BOLD
            )
            button_style = ft.ButtonStyle(
                color=colors.BLACK, bgcolor=colors.WHITE
            )
            # ct_input = ft.AutoComplete(
            #     suggestions=planete_list,
            #     on_select=lambda e: print(e.control.selected_index, e.selection),
            #     text_style = ft.TextStyle(size=10),
            # )
            suggestion_list = ft.ListView(height=30)

            def on_text_change(e):
                # Filtrer les données en fonction de la saisie
                query = e.control.value.lower()
                filtered_data = [item for item in data_pSearch if query in item["pl_name"].lower()]
                
                # Limiter les résultats à 10 éléments
                suggestion_list.controls.clear()
                for item in filtered_data[:50]:
                    suggestion_list.controls.append(
                        ft.TextButton(
                            item["pl_name"],
                            style=button_style,
                            on_click=lambda e, item=item: select_item(e, item)
                        )
                    )
                Exoplanet.update(self)

            def select_item(e, item):
                text_field.value = item["pl_name"]
                suggestion_list.controls.clear()
                print(item["sy_dist"])

                self.table_container.content.controls[0].controls[1].content = ft.Text(
                  'Planète: '+  str(item["pl_name"]) + " ; Distance: " +  str(item["sy_dist"])+
                  "\nEtoile: " +  str(item["hostname"])+ " ; Année: " +  str(item["disc_year"])+
                  "\nMasse(T): " +  str(item["pl_bmasse"])+" ; Rayon(T): " +  str(item["pl_rade"])+
                  "\nMasse(J): " +  str(item["pl_bmassj"])+" ; Rayon(J): " +  str(item["pl_radj"])+
                  "\nDensitéPL: " +  str(item["pl_dens"])+" ; PériodePL: " +  str(item["pl_orbper"])+
                  "\nTempératurePL: " +  str(item["pl_eqt"])+
                  "\nInstrument: " +  str(item["disc_telescope"])+
                  "\nMethode: " +  str(item["discoverymethod"])+
                  "\nSpectraltypeST: " +  str(item["st_spectype"])+" ; TempératureST: " +  str(item["st_teff"])+
                  "\nRayonST: " +  str(item["st_rad"])+" ; MasseST: " +  str(item["st_mass"]),
                                   
                  color=colors.BLACK,size=13,weight=ft.FontWeight.BOLD
                    )

                Exoplanet.update(self)

            text_field = ft.TextField(
                label="recherche par nom d'exoplanetes",
                on_change=on_text_change,
                text_style=normal_title_style,
            )

            # print("cti : ",ct_input)
            print(self.table_container.content.controls[0].controls[0].content)
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].value="trois"
            # self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4] = ct_input
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4] = text_field
            # self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[5] = suggestion_list

            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].bgcolor=colors.WHITE
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].color=colors.BLACK

            #valeurs
            print("1: ",self.table_container.content.controls[0].controls[0].content)
            self.table_container.content.controls[0].controls[0].content=suggestion_list
            print("2: ",self.table_container.content.controls[0].controls[0].content)
            self.table_container.content.controls[0].controls[0].content.value = ""
            self.table_container.content.controls[0].controls[1].content.value = ""
            self.table_container.content.controls[0].controls[2].content.value = ""
            self.table_container.content.controls[0].controls[3].content.value = ""
            self.table_container.content.controls[0].controls[4].content.value = ""
            self.table_container.content.controls[0].controls[5].content.value = ""
            self.table_container.content.controls[0].controls[6].content.value = ""
            self.table_container.content.controls[0].controls[7].content.value = ""
            self.table_container.content.controls[0].controls[8].content.value = ""
            self.table_container.content.controls[0].controls[9].content.value = ""
            

            Exoplanet.update(self)

        def table_4(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.PURPLE_200

            #valeur des cellules par ligne
            self.datatable.rows[0].cells[1].content.value = "cel112"

            self.table_container.content.controls[0].controls[0].content.visible=False
            self.table_container.content.controls[0].controls[0].content = Text("",
                                                                                size=12, weight='bold',color=colors.BLACK,)

            print(self.table_container.bgcolor)
            self.table_container.bgcolor = ft.colors.PURPLE_200
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4])
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].value="Les 10 dernières planetes découvertes"
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].bgcolor=colors.BLACK
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].color=colors.PURPLE_200

            #valeurs
            self.table_container.content.controls[0].controls[0].content.value = str(plpr0_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr0_decouv)
            self.table_container.content.controls[0].controls[1].content.value = str(plpr1_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr1_decouv)
            self.table_container.content.controls[0].controls[2].content.value = str(plpr2_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr2_decouv)
            self.table_container.content.controls[0].controls[3].content.value = str(plpr3_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr3_decouv)
            self.table_container.content.controls[0].controls[4].content.value = str(plpr4_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr4_decouv)
            self.table_container.content.controls[0].controls[5].content.value = str(plpr5_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr5_decouv)
            self.table_container.content.controls[0].controls[6].content.value = str(plpr6_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr6_decouv)
            self.table_container.content.controls[0].controls[7].content.value = str(plpr7_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr7_decouv)
            self.table_container.content.controls[0].controls[8].content.value = str(plpr8_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr8_decouv)
            self.table_container.content.controls[0].controls[9].content.value = str(plpr9_name)+str('\t\t\t\t\t')+'Decouv : '+str(plpr9_decouv)
            

            Exoplanet.update(self)

        def table_5(e):
            #nom des colonnes
            self.datatable.columns[0].label.value=str(ncol2)
            print(self.datatable.bgcolor)
            self.datatable.bgcolor = ft.colors.DEEP_ORANGE

            #valeur des cellules par ligne

            self.datatable.rows[0].cells[1].content.value = "cel112"
            print(self.datatable.rows[0].cells[1].content.value)

            self.table_container.content.controls[0].controls[0].content.visible=False
            self.table_container.content.controls[0].controls[0].content = Text("",
                                                                                size=12, weight='bold',color=colors.BLACK,)

            print(self.table_container.bgcolor)
            self.table_container.bgcolor = ft.colors.DEEP_ORANGE
            print(self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4])
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].value="cinq"
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].bgcolor=colors.BLACK
            self.inner_green_container.content.controls[0].controls[0].content.controls[0].controls[4].color=colors.DEEP_ORANGE

            #valeurs
            self.table_container.content.controls[0].controls[0].content.value = ""
            self.table_container.content.controls[0].controls[1].content.value = ""
            self.table_container.content.controls[0].controls[2].content.value = ""
            self.table_container.content.controls[0].controls[3].content.value = ""
            self.table_container.content.controls[0].controls[4].content.value = ""
            self.table_container.content.controls[0].controls[5].content.value = ""
            self.table_container.content.controls[0].controls[6].content.value = ""
            self.table_container.content.controls[0].controls[7].content.value = ""
            self.table_container.content.controls[0].controls[8].content.value = ""
            self.table_container.content.controls[0].controls[9].content.value = ""
            


            Exoplanet.update(self)

        self.datatable=ft.DataTable(
                    width=250,
                    bgcolor="yellow",
                    column_spacing=1,
                    heading_row_height=20,
                    heading_row_color="#5e0b66",
                    data_row_min_height=25,
                    data_row_max_height=25,
                    data_row_color =({"hovered":"0x30FF0000"}),
                    border_radius=30,
                    columns=[
                        ft.DataColumn(ft.Text(str(col1),
                                                color="yellow",
                                                weight="bold")),
                        ft.DataColumn(ft.Text(str(col2),
                                                color="yellow",
                                                weight="bold",
                                                )),
                        ft.DataColumn(ft.Text(str(col3),
                                                color="yellow",
                                                weight="bold"
                                                )),
                                                
                    ],
                    rows=[
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("cel11", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel12", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel13", size=10, weight="bold")), 
                                # ft.DataCell(ft.Text("cel14")),                                                             
                            ],   
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("cel21", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel22", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel23", size=10, weight="bold")), 
                                # ft.DataCell(ft.Text("cel24")),                                                             
                            ],
                        ),
                        ft.DataRow(
                            cells=[
                                ft.DataCell(ft.Text("cel31", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel32", size=10, weight="bold")),
                                ft.DataCell(ft.Text("cel33", size=10, weight="bold")), 
                            #    ft.DataCell(ft.Text("cel43")),                                                             
                            ],
                        ),    
                    ],

                )
        
        self.table_container = Container(
            width=self.main.width,
            height=self.main.height * 0.40,
            border_radius=30,
            border=ft.border.all(2,colors.BLACK),
            # gradient=LinearGradient(
            #     begin=alignment.top_right,
            #     end=alignment.bottom_left,
            #     #colors=["#01171c","#7de3fa"],#cyan 2
            #     colors=["#333300","#ffffcc"]
            # ),
            padding=padding.only(bottom=10),
            bgcolor=colors.AMBER,
            content =Row(
                controls=[
                    Column(
                        expand = True,
                        horizontal_alignment='center',
                        alignment=alignment.center,
                        controls=[
                            Container(
                                content = Text(str(plpp0_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp0_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp1_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp1_dist)+str(' parsecs'), 
                                               size=12, weight='bold', color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp2_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp2_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp3_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp3_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp4_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp4_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp5_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp5_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp6_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp6_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp7_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp7_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp8_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp8_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                            Container(
                                content = Text(str(plpp9_name)+str('\t\t\t\t\t')+'Distance : '+str(plpp9_dist)+str(' parsecs'), 
                                               size=12, weight='bold',color=colors.BLACK,),
                            ),
                        ]
                    )
                ]
            )



            # content=Text("3 premières planetes les plus proches",
            #             size=10, 
            #             weight='bold',
            #             color=colors.WHITE70,
            #             text_align='center'
            #         ),




            )

        self.inner_green_container = Container(
            width=self.green_container.width,
            height=self.green_container.height,
            #bgcolor='blue',
            content=Row(
                spacing=0,
                controls=[
                    Column(
                        expand=8,
                        controls=[
                            Container(
                                padding=20, 
                                expand=True,
                                content=Row(
                                    controls=[
                                        Column(
                                            expand=True,
                                            horizontal_alignment='center',
                                            controls=[
                                                Text(
                                                    'EXOPLANETES CONFIRMEES'+str(version),
                                                    color=colors.LIGHT_BLUE,
                                                    size=16,
                                                    weight='bold',

                                                ),
                                                Text(
                                                    str(nb_exoplanets),
                                                    color='white',
                                                    size=20,
                                                    weight='bold',
                                                    #text_align=ft.TextAlign.CENTER,
                                                ),
                                                Text(
                                                    disabled=False,
                                                    color=colors.YELLOW,
                                                    text_align=ft.TextAlign.CENTER,
                                                    spans=[
                                                        ft.TextSpan(
                                                            "Go to NASA Exoplanet Archive",
                                                            ft.TextStyle(decoration=ft.TextDecoration.UNDERLINE),
                                                            url="https://exoplanetarchive.ipac.caltech.edu",
                                                            # on_enter=self.highlight_link,
                                                            # on_exit=self.unhighlight_link,
                                                            )
                                                    ],
                                                ),
                                                Row(
                                                    [
                                                ft.Container(
                                                    content=ft.Text("0",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.AMBER,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    on_click= table_0,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("1",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.GREEN_200,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    on_click=table_1,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("2",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor='#18ACEF',
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    # ink=True,
                                                    on_click=table_2,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("3",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.RED_200,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    # ink=True,
                                                    on_click=table_3,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("4",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.PURPLE_200,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    # ink=True,
                                                    on_click=table_4,
                                                ),
                                                ft.Container(
                                                    content=ft.Text("5",color=colors.BLACK,weight='bold'),
                                                    margin=5,
                                                    padding=5,
                                                    alignment=ft.alignment.center,
                                                    bgcolor=ft.colors.DEEP_ORANGE,
                                                    width=20,
                                                    height=30,
                                                    border_radius=10,
                                                    # ink=True,
                                                    on_click=table_5,
                                                ),
                                            ],
                                            alignment=ft.MainAxisAlignment.CENTER,
                                                ),
                                                Text(
                                                    "Les 10 planetes les plus proches",
                                                    color=colors.AMBER,
                                                    bgcolor=colors.BLACK,
                                                    size=15,
                                                    weight='bold',
                                                    #text_align=ft.TextAlign.CENTER,
                                                ),
                                                # self.datatable,
                                                self.table_container
                                            ],
                                        ),
                                    ]
                                ),
                            ),
                        ],
                    ),
                ],
            ),
        )

        self.grid_distances = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
            horizontal=True,
        )

        self.grid_decouverte = GridView(
            expand=True,
            max_extent=150,
            runs_count=0,
            spacing=12,
            run_spacing=5,
            horizontal=True,
        )

        self.main_content_area = Container(
            width=self.main.width,
            height=self.main.height * 0.40,
            #bgcolor='blue',
            padding=padding.only(top=2, left=10, right=10),
            content=Column(
                spacing=10,
                controls=[
                    Row(
                        alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            Container(
                                content=Text(
                                    'Nombres planètes par distances (parsec)',
                                    size=14,
                                    color='white',
                                    weight='bold',
                                )
                            ),
                        ]
                    ),
                    Container(
                        height=50,
                        content=self.grid_distances,
                    ),
                    Row(
                        # alignment='spaceBetween',
                        vertical_alignment='end',
                        controls=[
                            Container(
                                content=Text(
                                    'Nombres planetes par années',
                                    size=14,
                                    color='white',
                                    weight='bold',
                                )
                            ),
                        ],
                    ),
                    Container(
                        height=50,
                        content=self.grid_decouverte,
                    ),
                    
                ],
            ),
        )

        distance_list = [["10", str(d10)],
                     ["20", str(d20)],
                     ["30", str(d30)],
                     ["40", str(d40)],
                     ["50", str(d50)],
                     ["60", str(d60)],
                     ["70", str(d70)],
                     ["80", str(d80)],
                     ["90", str(d90)],
                     ["100", str(d100)],
                     ]
        for i in distance_list:
            __ = Container(
                width=100,
                height=100,
                bgcolor='white10',
                border_radius=15,
                alignment=alignment.center,
                content = Text( f'{i}',color='white', weight='bold' ),
            )
            self.grid_distances.controls.append(__)

            for x in i:
                __.content = Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                        Text(f'{i[0]}', size=11, color='yellow54'),
                        Text(f'{i[1]}', size=12,color='white', weight='bold'),
                    ]
                )

        decouverte_list = [
            [str(y0), str(y1)],
            [str(y0 - 1), str(y2)],
            [str(y0 - 2), str(y3)],
            [str(y0 - 3), str(y4)],
            [str(y0 - 4), str(y5)],
            [str(y0 - 5), str(y6)],
            [str(y0 - 6), str(y7)],
            [str(y0 - 7), str(y8)],
            [str(y0 - 8), str(y9)],
            [str(y0 - 9), str(y10)],       
        ]
        for i in decouverte_list:
            __ = Container(
                width=100,
                height=100,
                bgcolor='#0A0D1E',
                border_radius=15,
                alignment=alignment.center,
                content = Text( f'{i}',color='white', weight='bold' ),
                # on_hover=lambda e: self.hover_animation(e),
            )
            self.grid_decouverte.controls.append(__)

            for x in i:
                __.content = Column(
                    alignment='center',
                    horizontal_alignment='center',
                    controls=[
                        Text(f'{i[0]}', size=11, color='yellow54'),
                        Text(f'{i[1]}', size=12,color='white', weight='bold'),

                        # Text(
                        #     'Pay Now?',
                        #     color='white',
                        #     size=12, 
                        #     text_align='start',
                        #     weight='w600',
                        #     offset= transform.Offset(0, 1),
                        #     animate_offset = animation.Animation(duration=900, curve='decelerate'),
                        #     animate_opacity=300,
                        #     opacity=0,
                        # )
                    ]
                )


        self.green_container.content = self.inner_green_container

        self.main_col.controls.append(self.green_container)
        self.main_col.controls.append(self.main_content_area)

        self.main.content = self.main_col

            
        # for icon in self.icon_column.controls[:]:
        #     if icon.selected== True:
        #         icon.icon_color = 'white'
        
        return self.main
    

    def build(self):
        return Column(controls=[self.MainContainer(),])


def start(page: Page):
    page.title='Flet Expense Concept'
    page.horizontal_alignment='center'
    page.vertical_alignment='center'
    #page.theme_mode = flet.ThemeMode.DARK
    
    app = Exoplanet()
    page.add(app)
    page.update()
    
    
if __name__ == '__main__':
    flet.app(target=start)

