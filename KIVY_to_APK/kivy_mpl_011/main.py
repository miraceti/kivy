from kivy.utils import platform
from kivy.config import Config

#avoid conflict between mouse provider and touch (very important with touch device)
#no need for android platform
if platform != 'android':
    Config.set('input', 'mouse', 'mouse,disable_on_activity')
else:
    #for android, we remove mouse input to not get extra touch 
    Config.remove_option('input', 'mouse')

from kivy.lang import Builder
from kivy.app import App

import matplotlib.pyplot as plt

from kivy.metrics import dp
import numpy as np

from kivy_matplotlib_widget.uix.hover_widget import add_hover,BaseHoverFloatLayout
from matplotlib.ticker import FormatStrFormatter
from kivy.properties import ColorProperty,NumericProperty,StringProperty
from matplotlib import gridspec
from numpy.random import rand
from matplotlib.ticker import NullFormatter, MaxNLocator
from numpy import linspace

import requests
from kivy.uix.floatlayout import FloatLayout
from collections import Counter
import pandas as pd

version= " (v010)"
##########################################
#code de recuperation des données externes
urlexo_pllist = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+distinct+\
pl_name,disc_year,sy_dist,discoverymethod,pl_bmasse,pl_rade,pl_orbper,pl_eqt,pl_dens\
+from+ps+&format=json"
response = requests.get(urlexo_pllist)
data_pllist = response.json()
#######################
#### ECRAN1
#######################
data_nbpl = list({(item['pl_name']) for item in data_pllist})
nb_exoplanets= len(data_nbpl)

# Regrouper par 'pl_name' et garder les valeurs maximales pour les autres colonnes
aggregated_data = {}
for row in data_pllist:
    pl_name = row['pl_name']
    if pl_name not in aggregated_data:
        aggregated_data[pl_name] = row
    else:
        for key in row:
            if key != 'pl_name' and row[key] is not None:
                # Conserver la valeur maximale pour les autres colonnes
                aggregated_data[pl_name][key] = max(aggregated_data[pl_name][key], row[key]) if aggregated_data[pl_name][key] is not None else row[key]

# Convertir en une liste de tuples pour MDDataTable
data_table_tuple = [
    (row['pl_name'], row['disc_year'], row['sy_dist'], row['discoverymethod'], row['pl_bmasse'], row['pl_rade'], row['pl_orbper'], row['pl_eqt'], row['pl_dens'])
    for row in aggregated_data.values()
]
#######################

#######################
### ECRAN2
#######################
#cle associés
keys = ["pl_name","disc_year","sy_dist","discoverymethod","pl_bmasse","pl_rade","pl_orbper","pl_eqt","pl_dense"]

#conversion en liste de dict
data_table_dict = [dict(zip(keys, tpl)) for tpl in data_table_tuple]

#######################

#######################
### ECRAN3
#######################
#extraction des tuples (pl_name, disc_year) sans doublons
unique_data = list(set(map(lambda x: (x['pl_name'], x['disc_year']), data_table_dict)))

#creation du comptage par année
from collections import Counter
#comptage decouverte par annee
discovery_counts = Counter(item['disc_year'] for item in data_table_dict)
#tri par annee
sorted_discovery_counts = sorted(discovery_counts.items())

#separation resultat en 2 listes
liste_annee, liste_nb = zip(*sorted_discovery_counts)

liste_annee = list(liste_annee)
liste_nb = list(liste_nb)

#tracer graphique
plt.figure(3, figsize=(10,6))
plt.plot(liste_annee, liste_nb, marker='o', linestyle='-', color='b', label='Nombre par année')
plt.title("Nombre d'exoplanètes par année")
plt.xlabel("Année")
plt.ylabel("Nombre")
plt.grid(True)
plt.legend()
# plt.show()


#######################
### ECRAN4
#######################
# plt.figure(4)
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = data['a'] + 10 * np.random.randn(50)
# data['d'] = np.abs(data['d']) * 100

# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('entry a')
# plt.ylabel('entry b')
# # plt.show()

#extraire les données
x = [item['disc_year'] for item in data_table_dict] #année de decouverte : X
y = [item['pl_bmasse'] for item in data_table_dict] #masse de la planete : Y
methods = [item['discoverymethod'] for item in data_table_dict]#methode de decouverte

#taille des points
size = 100

#palette de couleurs
unique_methods = list(set(methods))
colors = {method: plt.cm.tab10(i) for i, method in enumerate(unique_methods)}

#tracer graph
plt.figure(4, figsize=(10,6))

for method in unique_methods:
    #filtrage data par methodes
    x_vals = [x[i] for i in range(len(x)) if methods[i]== method]
    y_vals = [y[i] for i in range(len(y)) if methods[i]== method]
    plt.scatter(x_vals, y_vals, s=size, color=colors[method], label=method, alpha=0.7, edgecolors='w')

#ajout detail graph
plt.title("Masse de la planete VS Année de découverte", fontsize=16)
plt.xlabel("Année de découverte (disc_year)", fontsize=14)
plt.ylabel("Masse de la planete (pl_bmasse)", fontsize=14)
plt.grid(True, linestyle='--', alpha=0.6)

#legende
plt.legend(title="Méthodes de découvertes", fontsize=12, loc='center left', bbox_to_anchor=(1, 0.5))

#ajuster l'epacement
plt.tight_layout()

#######################
### ECRAN5
#######################

#pie
# plt.style.use('dark_background')
# labels = 'Frogs', 'Hogs', 'Dogs', 'logs'
# sizes = [15, 30, 45, 10]
# fig, ax = plt.subplots()
# ax.pie(sizes, labels=labels)


#########
#comptage des ocurence
discovery_methods = [item['discoverymethod'] for item in data_table_dict]
method_counts = Counter(discovery_methods)

#preparation données
labels = list(method_counts.keys())
counts = list(method_counts.values())

#palette de couleurs pour les barres
colors = plt.cm.Paired.colors[:len(labels)]

#tracage
plt.figure(5, figsize=(8,6))
plt.bar(labels, counts, color=colors, edgecolor='black')
plt.title("Répartition  des méthodes de découverte", fontsize=14)
plt.xlabel("Méthodes de découverte", fontsize=12, fontweight='bold')
plt.ylabel("nombre d'éléments", fontsize=12)
plt.xticks(rotation=45 , fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()


fig_num=plt.gcf().number
print(fig_num)
############################################################
#########################################


KV = '''
BoxLayout:
        
    orientation:'vertical'
    BoxLayout:
        size_hint_y:0.1
        Button:
            text:"ACCUEIL" " - nb : '''+str(nb_exoplanets)+'''"
            on_release:app.home()

        ToggleButton:
            group:'touch_mode'
            state:'down'
            text:"PAN" 
            on_release:
                app.set_touch_mode('pan')
                self.state='down'    
        ToggleButton:
            group:'touch_mode'
            text: 'ZOOM_BOX'
            on_press: 
                app.set_touch_mode('zoombox')
                self.state='down'
                    
    BoxLayout: 
        ScreenManager:
            id:sm
            Screen1:
            Screen2:
            Screen3:
            Screen4:
            Screen5:
            Screen6:
            Screen7:
            Screen8:
            Screen9:
            Screen10:

    BoxLayout:
        size_hint_y:0.1
        Button:
            text:"ECRAN PRECEDENT"
            on_release:app.previous_screen()
        Button:
            text:"ECRAN SUIVANT"
            on_release:app.next_screen()
                
<Screen1@Screen>
    name:'screen1'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        fast_draw:True
        interactive_axis:True
        
<Screen2@Screen> 
    name:'screen2'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True
        
<Screen3@Screen> 
    name:'screen3'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True
        
<Screen4@Screen> 
    name:'screen4'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        max_hover_rate:5/60
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True

<Screen5@Screen> 
    name:'screen5'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        max_hover_rate:5/60
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True

<Screen6@Screen> 
    name:'screen6'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        max_hover_rate:5/60
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True


<Screen7@Screen> 
    name:'screen7'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        max_hover_rate:5/60
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True


<Screen8@Screen> 
    name:'screen8'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        max_hover_rate:5/60
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True


<Screen9@Screen> 
    name:'screen9'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        max_hover_rate:5/60
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True


<Screen10@Screen> 
    name:'screen10'  
    figure_wgt:figure_wgt                  
    MatplotFigureSubplot:
        id:figure_wgt
        max_hover_rate:5/60
        fast_draw:True
        interactive_axis:True
        draw_all_axes:True
    
                        
<PlotlyHover2>
    custom_color: [0,0,0,1]
    BoxLayout:
        id:main_box
        x:
            root.x_hover_pos + dp(4)
        y:
            root.y_hover_pos - root.hover_height/2
        size_hint: None, None
        height: label.texture_size[1]+ dp(4)
        width: 
            self.minimum_width + dp(12) if root.show_cursor \
            else dp(0.0001)            
        orientation:'vertical'
        padding: 0,-dp(1),0,0
        
        canvas:            
            Color:
                rgba: root.custom_color if root.custom_color else [0,0,0,1]
            Rectangle:
                pos: self.pos
                size: self.size
            Triangle:
                points:
                    [ \
                    root.x_hover_pos, root.y_hover_pos, \
                    main_box.x, root.y_hover_pos+ dp(4), \
                    main_box.x, root.y_hover_pos- dp(4)  \
                    ]
            SmoothLine:
                width:dp(1)
                points:
                    [ \
                    root.x_hover_pos, root.y_hover_pos, \
                    main_box.x, root.y_hover_pos \
                    ]                           
             
        BoxLayout:
            size_hint_x:None
            width:label.texture_size[0]
            padding: dp(12),0,0,0
            Label:
                id:label
                text: 
                    '(' + root.label_x_value  +','+ root.label_y_value +')'
                font_size:root.text_size
                color:
                    [0,0,0,1] if (root.custom_color[0]*0.299 + \
                    root.custom_color[1]*0.587 + root.custom_color[2]*0.114) > 186/255 \
                    else [1,1,1,1]
                font_name : root.text_font

                font_name : root.text_font
                
        FloatLayout:
            size_hint: None,None
            width: dp(0.01) 
            height: dp(0.01) 
            BoxLayout:
                size_hint:None,None
                x:main_box.x + main_box.width + dp(4)
                y:main_box.y + main_box.height/2 - label3.texture_size[1]/2
                width:label3.texture_size[0]
                height:label3.texture_size[1]
                Label:
                    id:label3
                    text: 
                        root.custom_label if root.custom_label and not '_child' in root.custom_label else ''  
                    font_size:root.text_size
                    color: root.text_color
                    font_name : root.text_font      

<InfoHover2>
    custom_color: [0,0,0,1]
    BoxLayout:
        id:main_box
        x:
            root.x_hover_pos + dp(4) if root.x_hover_pos + dp(4) < root.figwidth - label.texture_size[0] - self.padding[0] * 2 \
            else root.x_hover_pos - dp(4) - max(label.texture_size[0],label2.texture_size[0]) - self.padding[0] * 2
        y:
            root.y_hover_pos + dp(4)
        size_hint: None, None
        height: root.hover_height
        width: 
            max(label.texture_size[0],label2.texture_size[0]) + dp(12) if root.show_cursor \
            else dp(0.0001)            
        orientation:'vertical'
        padding: 0,dp(4),0,dp(4)
        
        canvas:            
            Color:
                rgba: root.custom_color if root.custom_color else [0,0,0,1]
            Rectangle:
                pos: self.pos
                size: self.size
            Color:
                rgba: 0,0,0,1
             
            Line:
                width: 1    
                rounded_rectangle:
                    (self.x, self.y, self.width, self.height,\
                    dp(4), dp(4), dp(4), dp(4),\
                    self.height)                 
                
                
        canvas.after:            
            Color:
                rgba: 0,0,0,1
            Rectangle:
                size: (dp(8),dp(8))
                pos: 
                    (root.x_hover_pos-dp(8/2), \
                     root.y_hover_pos-dp(8/2))
        
        BoxLayout:
            size_hint_x:None
            width:label.texture_size[0]
            padding: dp(12),0,0,0
            Label:
                id:label
                text: 
                    root.label_x + ': ' + root.label_x_value  
                font_size:root.text_size
                color:
                    [0,0,0,1] if (root.custom_color[0]*0.299 + \
                    root.custom_color[1]*0.587 + root.custom_color[2]*0.114) > 186/255 \
                    else [1,1,1,1]
                font_name : root.text_font

        BoxLayout:
            size_hint_x:None
            width:label2.texture_size[0]   
            padding: dp(12),0,0,0
            Label:
                id:label2
                text:
                    root.label_y + ': ' + root.label_y_value    
                font_size:root.text_size
                color:
                    [0,0,0,1] if (root.custom_color[0]*0.299 + \
                    root.custom_color[1]*0.587 + root.custom_color[2]*0.114) > 186/255 \
                    else [1,1,1,1]
                font_name : root.text_font
        FloatLayout:
            size_hint: None,None
            width: dp(0.01) 
            height: dp(0.01) 
            BoxLayout:
                size_hint:None,None
                x:main_box.x + main_box.width + dp(4)
                y:main_box.y + main_box.height - label3.texture_size[1]
                width:label3.texture_size[0]
                height:label3.texture_size[1]
                Label:
                    id:label3
                    text: 
                        root.custom_label if root.custom_label and not '_child' in root.custom_label else ''  
                    font_size:root.text_size
                    color: root.text_color
                    font_name : root.text_font  
                    
'''

class PlotlyHover2(BaseHoverFloatLayout):
    """ PlotlyHover adapt the background and the font color with the line or scatter color""" 
    text_color=ColorProperty([0,0,0,1])
    text_font=StringProperty("Roboto")
    text_size = NumericProperty(dp(14))
    hover_height = NumericProperty(dp(24))

    
    def __init__(self, **kwargs):
        """ init class """
        super().__init__(**kwargs)  

class InfoHover2(BaseHoverFloatLayout):
    """ InfoHover adapt the background and the font color with the line or scatter color""" 
    text_color=ColorProperty([0,0,0,1])
    text_font=StringProperty("Roboto")
    text_size = NumericProperty(dp(14))
    hover_height = NumericProperty(dp(48))
    
    def __init__(self, **kwargs):
        """ init class """
        super().__init__(**kwargs)     

class Test(App):
    lines = []

    def build(self):
        self.graph_app = Builder.load_string(KV)
        return self.graph_app


    def on_start(self, *args):

# =============================================================================
#         figure 1 - screen1
# =============================================================================
        # x = np.linspace(0, 2 * np.pi, 400)
        # y = np.sin(x ** 2)
        
        # fig, axs = plt.subplots(2, 2)
        # axs[0, 0].plot(x, y)
        # axs[0, 0].set_title('Axis [0, 0]')
        # axs[0, 1].plot(x, y, 'tab:orange')
        # axs[0, 1].set_title('Axis [0, 1]')
        # axs[1, 0].plot(x, -y, 'tab:green')
        # axs[1, 0].set_title('Axis [1, 0]')
        # axs[1, 1].plot(x, -y, 'tab:red')
        # axs[1, 1].set_title('Axis [1, 1]')
        
        # axs[1, 1].set_xlim(2,10)
        
        # for ax in axs.flat:
        #     ax.set(xlabel='x-label', ylabel='y-label')

        # # Hide x labels and tick labels for top plots and y ticks for right plots.
        # for ax in axs.flat:
        #     ax.label_outer()

        ###########
        # Liste des planètes
        planets = data_table_dict

        # Filtrer les planètes ayant une valeur 'none' ou 1 dans la colonne 'pl_bmasse'
        filtered_planets0 = [
            planet for planet in planets
            if planet['pl_bmasse'] not in [None,'none', '1', 1] 
        ]

        filtered_planets = [
            planet for planet in filtered_planets0
            if  1 < float(planet['pl_bmasse']) < 100
        ]

        # Filtrer les planètes ayant une valeur 'none' ou 1 dans la colonne 'pl_bmasse'
        filtered_planets_avec_10 = [
            planet for planet in planets
            if planet['pl_bmasse'] not in [None,'none'] 
        ]

        filtered_planets_avec_1 = [
            planet for planet in filtered_planets_avec_10
            if  0 < float(planet['pl_bmasse']) < 100
        ]

        # Extraire les masses
        masses = [float(planet['pl_bmasse']) for planet in filtered_planets]
        masses_avec_1 = [float(planet['pl_bmasse']) for planet in filtered_planets_avec_1]

        # Définir les tranches
        bins = [0, 2, 4, 6, 8, 10]
        labels = ['0-2', '2-4', '4-6', '6-8', '8-10']

        # Diviser les données en tranches
        mass_bins = []
        for mass in masses:
            for j in range(len(bins) - 1):
                if bins[j] <= mass < bins[j + 1]:
                    mass_bins.append(labels[j])
                    break

        mass_bins_avec_1 = []
        for mass in masses_avec_1:
            for j in range(len(bins) - 1):
                if bins[j] <= mass < bins[j + 1]:
                    mass_bins_avec_1.append(labels[j])
                    break

        # Compter les occurrences de chaque tranche
        bin_counts = Counter(mass_bins)
        bin_counts_avec_1 = Counter(mass_bins_avec_1)

        # Trier les tranches pour un graphique bien tracé
        sorted_bins = sorted(bin_counts.keys(), key=lambda x: int(x.split('-')[0]))
        sorted_counts = [bin_counts[bin] for bin in sorted_bins]

        # Trier les tranches pour un graphique bien tracé
        sorted_bins_avec_1 = sorted(bin_counts_avec_1.keys(), key=lambda x: int(x.split('-')[0]))
        sorted_counts_avec_1 = [bin_counts_avec_1[bin] for bin in sorted_bins_avec_1]

        # Créer une figure avec deux sous-graphiques
        fig1 = plt.figure()
        # set height ratios for subplots
        gs = gridspec.GridSpec(2, 1, height_ratios=[1, 1]) 
        
        # the first subplot
        ax0 = plt.subplot(gs[0])
        
        # Tracer le premier graphique
        ax0.plot(sorted_bins, sorted_counts, marker='o', linestyle='-', color='b', label='inclue masse = 1T')
        ax0.set_ylabel("Nombre de planètes")
        ax0.set_title("Distribution du nombre de planètes par tranches de masse (inclue masse = 1T)")
        ax0.legend()
        ax0.grid()

        # Tracer le second graphique (identique au premier)
        ax1 = plt.subplot(gs[1], sharex = ax0)
        ax1.plot(sorted_bins_avec_1, sorted_counts_avec_1, marker='o', linestyle='-', color='r', label='exclue masse = 1T')
        ax1.set_xlabel("Tranches de masse (en M_Terre)")
        ax1.set_ylabel("Nombre de planètes")
        ax1.set_title("Distribution du nombre de planètes par tranches de masse (exclue masse = 1T)")
        ax1.legend()
        ax1.grid()

         # put legend on first subplot
        # ax0.legend((line0, line1), ('red line', 'blue line'), loc='lower left')
        
        # remove vertical gap between subplots
        plt.subplots_adjust(hspace=.0)

        # Ajuster l'espacement entre les graphiques
        # plt.tight_layout()

        fig1=plt.gcf()
        # Afficher les graphiques
        #plt.show()

        ###########
                
        screen1=self.graph_app.ids.sm.get_screen('screen1')
        screen1.figure_wgt.figure = fig1
        screen1.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen1.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen1.figure_wgt.register_cursor()
        
        add_hover(screen1.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())

# =============================================================================
#         figure 2 - screen2
# =============================================================================
        x = np.linspace(0, 2 * np.pi, 400)
        y = np.sin(x ** 2)
        
        fig2 = plt.figure()
        # set height ratios for subplots
        gs = gridspec.GridSpec(2, 1, height_ratios=[2, 1]) 
        
        # the first subplot
        ax0 = plt.subplot(gs[0])
        # log scale for axis Y of the first subplot
        ax0.set_yscale("log")
        line0, = ax0.plot(x, y, color='r',label='red line')
        
        # the second subplot
        # shared axis X
        ax1 = plt.subplot(gs[1], sharex = ax0)
        line1, = ax1.plot(x, y, color='b', linestyle='--',label='red line')
        plt.setp(ax0.get_xticklabels(), visible=False)
        # remove last tick label for the second subplot
        yticks = ax1.yaxis.get_major_ticks()
        yticks[-1].label1.set_visible(False)
        
        # put legend on first subplot
        ax0.legend((line0, line1), ('red line', 'blue line'), loc='lower left')
        
        # remove vertical gap between subplots
        plt.subplots_adjust(hspace=.0)
                
        screen2=self.graph_app.ids.sm.get_screen('screen2')
        screen2.figure_wgt.figure = fig2
        screen2.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen2.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen2.figure_wgt.register_cursor()
        
        add_hover(screen2.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())

# =============================================================================
#         figure 3 - screen3
# =============================================================================

        # create all axes we need
        ax0 = plt.subplot(211)
        ax1 = ax0.twinx()
        ax2 = plt.subplot(212)
        ax3 = ax2.twinx()
        
        # share the secondary axes
        if hasattr(ax1,'sharey'):
            ax1.sharey(ax3)
        else:
            ax1.get_shared_y_axes().join(ax1, ax3)
            
        
        ax0.plot(rand(1) * rand(10),'r')
        ax1.plot(10*rand(1) * rand(10),'b')
        ax2.plot(3*rand(1) * rand(10),'g')
        ax3.plot(10*rand(1) * rand(10),'y')
        fig3=plt.gcf()
                
        screen3=self.graph_app.ids.sm.get_screen('screen3')
        screen3.figure_wgt.figure = fig3
        screen3.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen3.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen3.figure_wgt.register_cursor()
        
        add_hover(screen3.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())

# =============================================================================
#         figure 4 - screen4
# =============================================================================

        # Define a function to make the ellipses
        def ellipse(ra,rb,ang,x0,y0,Nb=100):
            xpos,ypos=x0,y0
            radm,radn=ra,rb
            an=ang
            co,si=np.cos(an),np.sin(an)
            the=linspace(0,2*np.pi,Nb)
            X=radm*np.cos(the)*co-si*radn*np.sin(the)+xpos
            Y=radm*np.cos(the)*si+co*radn*np.sin(the)+ypos
            return X,Y
         
        # Define the x and y data 
        # For example just using random numbers
        x = np.random.randn(10000)
        y = np.random.randn(10000)
         
        # Set up default x and y limits
        xlims = [min(x),max(x)]
        ylims = [min(y),max(y)]
         
        # Set up your x and y labels
        xlabel = '$\mathrm{Your\\ X\\ Label}$'
        ylabel = '$\mathrm{Your\\ Y\\ Label}$'
         
        # Define the locations for the axes
        left, width = 0.12, 0.55
        bottom, height = 0.12, 0.55
        bottom_h = left_h = left+width+0.02
         
        # Set up the geometry of the three plots
        rect_temperature = [left, bottom, width, height] # dimensions of temp plot
        rect_histx = [left, bottom_h, width, 0.25] # dimensions of x-histogram
        rect_histy = [left_h, bottom, 0.25, height] # dimensions of y-histogram
        
        # Set up the size of the figure
        fig4 = plt.figure(1, figsize=(9.5,9))
         
        # Make the three plots
        axTemperature = plt.axes(rect_temperature) # temperature plot
        axHistx = plt.axes(rect_histx, sharex = axTemperature) # x histogram
        axHisty = plt.axes(rect_histy, sharey = axTemperature) # y histogram
        
        
        # Remove the inner axes numbers of the histograms
        nullfmt = NullFormatter()
        axHistx.xaxis.set_major_formatter(nullfmt)
        axHisty.yaxis.set_major_formatter(nullfmt)
         
        # Find the min/max of the data
        xmin = min(xlims)
        xmax = max(xlims)
        ymin = min(ylims)
        ymax = max(y)
         
        # Make the 'main' temperature plot
        # Define the number of bins
        nxbins = 50
        nybins = 50
        nbins = 100
         
        xbins = linspace(start = xmin, stop = xmax, num = nxbins)
        ybins = linspace(start = ymin, stop = ymax, num = nybins)
        xcenter = (xbins[0:-1]+xbins[1:])/2.0
        ycenter = (ybins[0:-1]+ybins[1:])/2.0

        H, xedges,yedges = np.histogram2d(y,x,bins=(ybins,xbins))
        X = xcenter
        Y = ycenter
        Z = H
         
        # Plot the temperature data
        cax = (axTemperature.imshow(H, extent=[xmin,xmax,ymin,ymax],
               interpolation='nearest', origin='lower',aspect='auto'))
         
        # Plot the temperature plot contours
        contourcolor = 'w'
        xcenter = np.mean(x)
        ycenter = np.mean(y)
        ra = np.std(x)
        rb = np.std(y)
        ang = 0
         
        X,Y=ellipse(ra,rb,ang,xcenter,ycenter)
        axTemperature.plot(X,Y,":",color = contourcolor,ms=1,linewidth=2.0)
        axTemperature.annotate('$1\\sigma$', xy=(X[15], Y[15]), xycoords='data',xytext=(10, 10),
                               textcoords='offset points', horizontalalignment='right',
                               verticalalignment='bottom',fontsize=25)
         
        X,Y=ellipse(2*ra,2*rb,ang,xcenter,ycenter)
        axTemperature.plot(X,Y,":",color = contourcolor,ms=1,linewidth=2.0)
        axTemperature.annotate('$2\\sigma$', xy=(X[15], Y[15]), xycoords='data',xytext=(10, 10),
                               textcoords='offset points',horizontalalignment='right',
                               verticalalignment='bottom',fontsize=25, color = contourcolor)
         
        X,Y=ellipse(3*ra,3*rb,ang,xcenter,ycenter)
        axTemperature.plot(X,Y,":",color = contourcolor, ms=1,linewidth=2.0)
        axTemperature.annotate('$3\\sigma$', xy=(X[15], Y[15]), xycoords='data',xytext=(10, 10),
                               textcoords='offset points',horizontalalignment='right',
                               verticalalignment='bottom',fontsize=25, color = contourcolor)
         
        #Plot the axes labels
        axTemperature.set_xlabel(xlabel,fontsize=25)
        axTemperature.set_ylabel(ylabel,fontsize=25)      
         
        #Make the tickmarks pretty
        ticklabels = axTemperature.get_xticklabels()
        for label in ticklabels:
            label.set_fontsize(18)
            label.set_family('serif')
         
        ticklabels = axTemperature.get_yticklabels()
        for label in ticklabels:
            label.set_fontsize(18)
            label.set_family('serif')
         
        #Set up the plot limits
        axTemperature.set_xlim(xlims)
        axTemperature.set_ylim(ylims)
         
        #Set up the histogram bins
        xbins = np.arange(xmin, xmax, (xmax-xmin)/nbins)
        ybins = np.arange(ymin, ymax, (ymax-ymin)/nbins)
         
        #Plot the histograms
        axHistx.hist(x, bins=xbins, color = 'blue')
        axHisty.hist(y, bins=ybins, orientation='horizontal', color = 'red')
         
        #Set up the histogram limits
        axHistx.set_xlim( min(x), max(x) )
        axHisty.set_ylim( min(y), max(y) )
         
        #Make the tickmarks pretty
        ticklabels = axHistx.get_yticklabels()
        for label in ticklabels:
            label.set_fontsize(12)
            label.set_family('serif')
         
        #Make the tickmarks pretty
        ticklabels = axHisty.get_xticklabels()
        for label in ticklabels:
            label.set_fontsize(12)
            label.set_family('serif')
         
        #Cool trick that changes the number of tickmarks for the histogram axes
        axHisty.xaxis.set_major_locator(MaxNLocator(4))
        axHistx.yaxis.set_major_locator(MaxNLocator(4))
        fig4=plt.gcf()

        screen4=self.graph_app.ids.sm.get_screen('screen4')
        screen4.figure_wgt.figure = fig4
        screen4.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen4.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen4.figure_wgt.register_cursor()
        
        add_hover(screen4.figure_wgt,mode='desktop',hover_widget=InfoHover2())

# =============================================================================
#         figure 5 - screen5
# =============================================================================

        # create all axes we need
        # methods = [item['discoverymethod'] for item in data_table_dict]#methode de decouverte

        #taille des points
        size = 100

        #palette de couleurs
        # unique_methods = list(set(methods))
        # colors = {method: plt.cm.tab10(i) for i, method in enumerate(unique_methods)}

        #comptage des ocurence
        discovery_methods = [item['discoverymethod'] for item in data_table_dict]
        method_counts = Counter(discovery_methods)

        #preparation données
        labels = list(method_counts.keys())
        counts = list(method_counts.values())

        #palette de couleurs pour les barres
        colors = plt.cm.Paired.colors[:len(labels)]

        #tracage
        plt.figure(5, figsize=(8,6))
        plt.bar(labels, counts, color=colors, edgecolor='black')
        plt.title("Répartition  des méthodes de découverte", fontsize=18, fontweight='bold')
        plt.xlabel("Méthodes de découverte", fontsize=16, fontweight='bold')
        plt.ylabel("nombre d'éléments", fontsize=16, fontweight='bold')
        plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        plt.yticks( fontsize=14, fontweight='bold')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        fig_num=plt.gcf().number
        print(fig_num)
        fig5=plt.gcf()
                
        screen5=self.graph_app.ids.sm.get_screen('screen5')
        screen5.figure_wgt.figure = fig5
        screen5.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen5.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen5.figure_wgt.register_cursor()
        
        add_hover(screen5.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())

# =============================================================================
#         figure 6 - screen6
# =============================================================================

        # create all axes we need
        #tracage
        # plt.figure(6, figsize=(8,6))
        # plt.bar(labels, counts, color=colors, edgecolor='black')
        # plt.title("Répartition  des méthodes de découverte", fontsize=18, fontweight='bold')
        # plt.xlabel("Méthodes de découverte", fontsize=16, fontweight='bold')
        # plt.ylabel("nombre d'éléments", fontsize=16, fontweight='bold')
        # plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        # plt.grid(axis='y', linestyle='--', alpha=0.7)
        # plt.tight_layout()

        #tracer graphique
        plt.figure(6, figsize=(8,6))
        plt.plot(liste_annee, liste_nb, marker='o', linestyle='-', color='b', label='Nombre par année')
        plt.title("Nombre d'exoplanètes par année", fontsize=24, fontweight='bold')
        plt.xlabel("Année", fontsize=20, fontweight='bold')
        plt.xticks(rotation=45 , fontsize=18, fontweight='bold')
        plt.ylabel("Nombre", fontsize=20, fontweight='bold')
        plt.yticks( fontsize=18, fontweight='bold')
        plt.grid(True)
        # plt.legend("nb/annee", fontsize=14)
        # plt.show()


        fig_num=plt.gcf().number
        print(fig_num)
        fig6=plt.gcf()
                
        screen6=self.graph_app.ids.sm.get_screen('screen6')
        screen6.figure_wgt.figure = fig6
        screen6.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen6.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen6.figure_wgt.register_cursor()
        
        add_hover(screen6.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())

# =============================================================================
#         figure 7 - screen7
# =============================================================================

        # create all axes we need
        #tracage
        # plt.figure(7, figsize=(8,6))
        # plt.bar(labels, counts, color=colors, edgecolor='black')
        # plt.title("Répartition  des méthodes de découverte", fontsize=18, fontweight='bold')
        # plt.xlabel("Méthodes de découverte", fontsize=16, fontweight='bold')
        # plt.ylabel("nombre d'éléments", fontsize=16, fontweight='bold')
        # plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        # plt.grid(axis='y', linestyle='--', alpha=0.7)
        # plt.tight_layout()

        #extraire les données
        x = [item['disc_year'] for item in data_table_dict] #année de decouverte : X
        y = [item['pl_bmasse'] for item in data_table_dict] #masse de la planete : Y
        methods = [item['discoverymethod'] for item in data_table_dict]#methode de decouverte

        #taille des points
        size = 100

        #palette de couleurs
        unique_methods = list(set(methods))
        colors = {method: plt.cm.tab10(i) for i, method in enumerate(unique_methods)}

        #tracer graph
        plt.figure(7, figsize=(8,10))

        for method in unique_methods:
            #filtrage data par methodes
            x_vals = [x[i] for i in range(len(x)) if methods[i]== method]
            y_vals = [y[i] for i in range(len(y)) if methods[i]== method]
            plt.scatter(x_vals, y_vals, s=size, color=colors[method], label=method, alpha=0.7, edgecolors='w')

        #ajout detail graph
        plt.title("Masse de la planete VS Année de découverte", fontsize=18, fontweight='bold')
        plt.xlabel("Année de découverte (disc_year)", fontsize=16, fontweight='bold')
        plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        plt.ylabel("Masse de la planete (pl_bmasse)", fontsize=16, fontweight='bold')
        plt.yticks( fontsize=14, fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.6)

        #legende
        plt.legend(title="Méthodes de découvertes", fontsize=14, loc='upper left', bbox_to_anchor=(0, 1))

        #ajuster l'epacement
        plt.tight_layout()

        fig_num=plt.gcf().number
        print(fig_num)
        fig7=plt.gcf()
                
        screen7=self.graph_app.ids.sm.get_screen('screen7')
        screen7.figure_wgt.figure = fig7
        screen7.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen7.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen7.figure_wgt.register_cursor()
        
        add_hover(screen7.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())


# =============================================================================
#         figure 8 - screen8
# =============================================================================

        # create all axes we need
        #comptage des ocurence
        # discovery_methods = [item['discoverymethod'] for item in data_table_dict]
        # method_counts = Counter(discovery_methods)

        # #preparation données
        # labels = list(method_counts.keys())
        # counts = list(method_counts.values())

        # #palette de couleurs pour les barres
        # colors = plt.cm.Paired.colors[:len(labels)]
        #tracage
        # plt.figure(8, figsize=(8,6))
        # plt.bar(labels, counts, color=colors, edgecolor='black')
        # plt.title("Répartition  des méthodes de découverte", fontsize=18, fontweight='bold')
        # plt.xlabel("Méthodes de découverte", fontsize=16, fontweight='bold')
        # plt.ylabel("nombre d'éléments", fontsize=16, fontweight='bold')
        # plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        # plt.grid(axis='y', linestyle='--', alpha=0.7)
        # plt.tight_layout()


                # Extraire les données
        x = [item['pl_bmasse'] if item['pl_bmasse'] is not None else 0.00   for item in data_table_dict]
        y = [item['pl_rade'] if item['pl_rade'] is not None else 0.00    for item in data_table_dict]
        methods = [item['discoverymethod'] for item in data_table_dict]  # Méthode de découverte

        # Filtrer les valeurs dans la plage (0, 10) exclusivement
        filtered_data = [
            (x_val, y_val, method)
            for x_val, y_val, method in zip(x, y, methods)
            if 0 < x_val < 10 and 0 < y_val < 10
        ]

        # Extraire les données filtrées
        x_filtered = [data[0] for data in filtered_data]
        y_filtered = [data[1] for data in filtered_data]
        methods_filtered = [data[2] for data in filtered_data]

        # Taille fixe des points
        size = 100  # Taille fixe des points

        # Générer une palette de couleurs pour les méthodes
        unique_methods = list(set(methods_filtered))
        colors = {method: plt.cm.tab10(i) for i, method in enumerate(unique_methods)}

        # Tracer le graphique
        # plt.figure(figsize=(10, 6))
        plt.figure(8, figsize=(8,6))

        for method in unique_methods:
            # Filtrer les données par méthode
            x_vals = [x_filtered[i] for i in range(len(x_filtered)) if methods_filtered[i] == method]
            y_vals = [y_filtered[i] for i in range(len(y_filtered)) if methods_filtered[i] == method]
            plt.scatter(x_vals, y_vals, s=size, color=colors[method], label=method, alpha=0.7, edgecolors='w')

        # Ajouter des détails au graphique
        plt.title("Masse vs Rayon des planètes", fontsize=18, fontweight='bold')
        plt.xlabel("Masse de la planète (pl_bmasse)", fontsize=16, fontweight='bold')
        plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        plt.ylabel("Rayon de la planète (pl_rade)", fontsize=16, fontweight='bold')
        plt.yticks( fontsize=14, fontweight='bold')
        plt.grid(True, linestyle='--', alpha=0.6)

        # Placer la légende sur la droite
        plt.legend(title="Méthodes de découverte", fontsize=14, loc='upper left', bbox_to_anchor=(0, 1))

        # Ajuster l'espacement
        plt.tight_layout()

        # Afficher le graphique
        # plt.show()


        fig_num=plt.gcf().number
        print(fig_num)
        fig8=plt.gcf()
                
        screen8=self.graph_app.ids.sm.get_screen('screen8')
        screen8.figure_wgt.figure = fig8
        screen8.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen8.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen8.figure_wgt.register_cursor()
        
        add_hover(screen8.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())


# =============================================================================
#         figure 9 - screen9
# =============================================================================

        # create all axes we need
        #comptage des ocurence
        discovery_methods = [item['discoverymethod'] for item in data_table_dict]
        method_counts = Counter(discovery_methods)

        #preparation données
        labels = list(method_counts.keys())
        counts = list(method_counts.values())

        #palette de couleurs pour les barres
        colors = plt.cm.Paired.colors[:len(labels)]
        #tracage
        plt.figure(9, figsize=(8,6))
        plt.bar(labels, counts, color=colors, edgecolor='black')
        plt.title("Répartition  des méthodes de découverte", fontsize=18, fontweight='bold')
        plt.xlabel("Méthodes de découverte", fontsize=16, fontweight='bold')
        plt.ylabel("nombre d'éléments", fontsize=16, fontweight='bold')
        plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        plt.yticks( fontsize=14, fontweight='bold')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        fig_num=plt.gcf().number
        print(fig_num)
        fig9=plt.gcf()
                
        screen9=self.graph_app.ids.sm.get_screen('screen9')
        screen9.figure_wgt.figure = fig9
        screen9.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen9.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen9.figure_wgt.register_cursor()
        
        add_hover(screen9.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())


# =============================================================================
#         figure 10 - screen10
# =============================================================================

        # create all axes we need
        #comptage des ocurence
        discovery_methods = [item['discoverymethod'] for item in data_table_dict]
        method_counts = Counter(discovery_methods)

        #preparation données
        labels = list(method_counts.keys())
        counts = list(method_counts.values())

        #palette de couleurs pour les barres
        colors = plt.cm.Paired.colors[:len(labels)]
        #tracage
        plt.figure(10, figsize=(8,6))
        plt.bar(labels, counts, color=colors, edgecolor='black')
        plt.title("Répartition  des méthodes de découverte", fontsize=18, fontweight='bold')
        plt.xlabel("Méthodes de découverte", fontsize=16, fontweight='bold')
        plt.yticks( fontsize=14, fontweight='bold')
        plt.ylabel("nombre d'éléments", fontsize=16, fontweight='bold')
        plt.xticks(rotation=45 , fontsize=14, fontweight='bold')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()

        fig_num=plt.gcf().number
        print(fig_num)
        fig10=plt.gcf()
                
        screen10=self.graph_app.ids.sm.get_screen('screen10')
        screen10.figure_wgt.figure = fig10
        screen10.figure_wgt.cursor_xaxis_formatter = FormatStrFormatter('%.1f') 
        screen10.figure_wgt.cursor_yaxis_formatter = FormatStrFormatter('%.1f') 
        
        screen10.figure_wgt.register_cursor()
        
        add_hover(screen10.figure_wgt,mode='desktop',hover_widget=PlotlyHover2())


    def set_touch_mode(self,mode):
        for screen in self.graph_app.ids.sm.screens:
            if hasattr(screen,'figure_wgt'):
                screen.figure_wgt.touch_mode=mode

    def home(self):
        screen=self.graph_app.ids.sm.current_screen
        screen.figure_wgt.main_home()
        
    def previous_screen(self):
        screen_name=self.graph_app.ids.sm.current
        screen_number = int(screen_name[-1])
        if screen_number<=1:
            screen_number=10
        else:
            screen_number-=1
            
        self.graph_app.ids.sm.current = 'screen' + str(screen_number)        
        
    def next_screen(self):
        screen_name=self.graph_app.ids.sm.current
        screen_number = int(screen_name[-1])
        if screen_number>=10:
            screen_number=1
        else:
            screen_number+=1
            
        self.graph_app.ids.sm.current = 'screen' + str(screen_number)


Test().run()