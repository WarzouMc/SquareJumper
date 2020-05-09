"""
This module is used to manage all game levels
"""
from core.generator.materials import materials
from core.generator.background.background import Backgrounds


# Obtain different level
def get_levels():
    # First level build
    # Line -> x
    # Column -> y
    level_0 = [
        "##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "############################################################################################################################################################################################################################################################################################################################################*#############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "############################################################################################################################################################################################################################################################################################################################################ù######################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################****###################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "##############################################################################################################################################################################################################################################################################################################**######################*###****##################*******############******####****##################################***##*#*#*#########################################################################################################################################################################################################################################################################################################################################################################################################################################################################**####*****#######################**##***#**#***###########################################################################*****#############################################################$$$$##***######################################***#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "#####################################################################################################################################################################################################################################################################################################*#####***$$#*################**##$###$$$$####****##########$$$$$$$############$$$$$$####$$$$###*****##########################$$$##$#ù#$#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################**##$$####$$$$$##**###################$$##$$$#$$#$$$#*####################################***##############################***#$$$$$##***#*#**###***************###########################****########$$$######################################$$$###***###############################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "##########################################################################################################################################################################################################################################################################################**#########$*####$$$###$##############*#$$##############$$$$#*#######*********############################$$$$$######*********##################$#######################################################################################################################################################################################################################################################################################################################################################################################################################################################################$$###############$$##**##############################$#*###############################***$$$###########################**#$$$########$$$#ù#$$###$$$$$$$$ùùùùùùù###########################$$$$#######################################################$$$##***##########################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "##########################################################################################################################################################################################################################################################################################$$##########$############*############$######################$#*#####$$$$$$$$$##**#*****#########################**##$$$$$$$$$###*******##############********#############******#####################################################################***********####################################################################################################################################################################################################################################################################################################################################################**######################$$###########***##################$#*#############################$$$#####***######################$$################$####****######$$$$$$$#############****###******###################################******************############$$$##***#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "######################################################################################################################################################################################################################################################################################**#######***##******#########$#####*##***##########################$#*##############$$#$$$$$#######*********#########$$##############$$$$$$$##############$$$$$$$$#############$$$$$$##*#*################################################################$$$$$$$$$$$#*##################**#################################################################################################################################################****#########################################################**#*############################################################################################################$$#########################**#*##**##$$$####################$#****############**##**##***#########$$$##**##***##**####****########################$$$$#*****##############***###$$$$###$$$$$$###################################$$$ù$$$ù$$ùù$$$$$$#################$$$#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################",
        "######################################################################################################################################################****###############################################################################################################**###########$$#######$$$##$$$$$$###########*###$#*$$$############################$##*##########################$$$ùùùùùù########################################################********###########$#$####################################################***######*##############$#*################$$#################################################################################################################################################$$$$######################################################**#$$#$#*#################################################################################################*******#############################$$#$##$$###########################$$$$####********$$##$$##$$$##############$$##$$$##$$####$$$$#############################$$$$$#****######***$$$####################################****####****######$###$##$$############################***###***#################################################################################################*******##################################################################################################################################################################################################################################################################################################################################################################################",
        "######################################################################################################################################################$$$$######################################################****########################################*****########$$####*###*#################################$#####ù##################################ù#############################$$$$$$########################################################$$$$$$$$###############***#########################***####################$$$######$################$#*#######################################################################################################***###***#######################################################***###############################################*#$$######$#*########################################################################################****###$$$$$$$########################################################################$$$$$ùùù###############################################################################$$$$#****#$$$#######################################$$$$####$$$$###########################################$$$###$$$###****########################****##############################################################$$$$$$$###############################################################################################################******#############################################################################################################################################################################################################################################################",
        "#################################################################################################################################################***############################################################$$$$########################################$$$$$###***########$###$###########**##########################$##################################$##################################################################################################################$$$###****##################$$$######**************#####***####################$###***********#################****#################################################################***$$$###$$$#####***###################################*****#######$$$***###***###################################**#$###########$##*#####################################################################################$$$$#######################################################################################$$$####################################################################################$$$$##############################################################################################################$$$$****####################$$$$########################################################################################**##***########****#########################################################################$$$$$$#############################################################################################################################################################################################################################################################",
        "#########################*********###################***###########*******##############***##***###**#######*******##############*###*********###$$$#####################****#####*********#####**####*#####################################*##***********##########$$$#######################*ùù*####################*################################################################################################################################################################$$$$####*#########**###########$$$$$$$$$$$$$$#####$$$########################$$$$$$$$$$$######******#####$$$$##################*****##########*###**###*#######*##########****$$$##############$$$#######*############******#########$$$$$##########$$$***$$$####################****#######**##$$################$########***####***###############*****##############******###########******##################################################################################################################################################################################################################################################################################################################$$$$##############***##################*****######**####**###################*****####***#######################**##$$##$$$###***##$$$$#########################*****##*##****####****####################****##############################################################################################################################################################################################****###################################################################",
        "*************************$$$$$$$$$*******************$$$***********$$$$$$$**************$$$**$$$***$$*******$$$$$$$**************$***$$$$$$$$$***************************$$$$*****$$$$$$$$$*****$$****$*************************************$**ù$$$$$$$$$$************************************$$$$********************$************************************************************************************************************************************************************************$*********$$**************************************************************************$$$$$$***************************$$$$$**********$***$$***$*******$**********$$$$***************************$************$$$$$$***************************ùùù***********************$$$$*******$$*****************************$$$****$$$***************$$$$$**************$$$$$$***********$$$$$$************************************************************************************************************************************************************************************************************************************************************************************************************************************$$$******************$$$$$******$$****$$*******************$$$$$****$$$***********************$$************$$$*******************************$$$$$**$**$$$$****$$$$********************$$$$**********************************************************************************************************************************************************************************************$$$$*******************************************************************",
        "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùùùùùùùùùùùùùùù$$$$$$$$$$$$$ùù$$$$$$$$$$$$$ù$ù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùùùù$$$$$$$$$ùùùùù$$$$$$$$$$$$$$$$$$$$$$$$$$ù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùùùùùùùùùùùùùùùùù$$$$$ùùùùùùùùù$$$$$$$$$$$$ùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùù$$$$$$$ùùùùùùùù$$$$$$$$$ùùù$$$$$$$ùùùùùùùùùù$$$$$ù$ùù$$$$$$$$$$$$$$$$$$$$$$ùùùùùùùùùùùùù$$$$$$$$$$$$$$$$$$ùùùùùù$$$$$$$$$ùùù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùù$$$ùùùùùù$$ùùù$$$$$$$$ùù$$$$$$$$$$ùùù$$$$$ùùù$$$$$$$ùù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùùùùùùùùùùùùùùù$$$$$$$$$$$$ùùùù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùùù$$$$$$$$ùù$$$$$$$$$$$$$ùùùùù$$$$$$$$$$$$$$$$$$$ùù$$$ùùùù$$$$$$$$$$$$$$$$$$$$$$$$$$ùùùù$$$$$$$$$$$$$$$$$$$$$$$$ùù$$$$$$$$$$$ùùù$$$$$$ùùù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùùù$$$ùùùùù$$$$$$$$$$$$$$$$$$$$$$$$$$$$ùùùùùùùù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ù$$ù$$$ù$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$&&&&&&&&&&&$$$$$$$$$$$$$$"
    ]

    # That give raw id of a material by a character
    value = {'#': 0, '$': 1, '*': 3, 'ù': 2, '&': 6}

    level_list = [
        LevelDesigner(level=to_level_path(value=value, string=level_0, change=[348, 450, 520, 900, 1000, 1100, 1200, 6000]), background=Backgrounds()
                      .background_list[0])
    ]
    return level_list


# That function transform char list level builder into a raw level
def to_level_path(value, string, change):
    terrain_type = [1, 4, 5, 1, 4, 5, 4, 1]
    x_len = len(string[0])
    y_len = len(string)
    level = [[0]*x_len]*y_len
    y = 0
    for line in string:
        x = 0
        x_path = [0] * x_len
        current_terrain = 0
        for material in line:
            x_path[x] = int(value.get(material))
            if change[current_terrain] < x:
                current_terrain += 1
            if x_path[x] == 1:
                x_path[x] = terrain_type[current_terrain]
            x += 1
        level[y] = x_path
        y += 1
    return level


# This class is used to manage the current level
class LevelDesigner:

    def __init__(self, level, background):
        self.level_path = level
        self.background = background

    # Modify level path
    def set_path(self, path):
        self.level_path = path

    # Obtain the numbers of this level
    def get_blocks(self):
        return self.get_length() * len(self.level_path[0])

    # Obtain x path size
    def get_length(self):
        return len(self.level_path)

    # Get the level path
    def get_level_path(self):
        return self.level_path

    # Get level background
    def get_background(self):
        return self.background

    # Obtain block id on a location
    def get_block_id_at(self, x=0, y=0):
        if len(self.level_path[(self.get_length() - y) - 1]) <= x:
            return 0
        return self.level_path[(self.get_length() - y) - 1][x]

    # Obtain block on a location
    def get_block_at(self, x=0, y=0):
        _id = self.get_block_id_at(x, y)
        material = materials.Materials().get_material_by_id(_id=_id)
        return material

    # Obtain first void block for x location
    def get_first_void_block_at(self, x=0):
        for i in range(len(self.get_level_path())):
            if self.get_block_id_at(x=x, y=i) == 0 or self.get_block_id_at(x=x, y=i) == 3:
                return x, i - 1
        return None
