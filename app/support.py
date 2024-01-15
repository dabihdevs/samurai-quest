from csv import reader
from os import walk
import pygame

def import_csv_layout(path):
    
    terrain_map = []
    with open(path) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    

def import_folder(path, scale=(128, 128)):
    """
    Returns list of surfaces, one for each image inside the input path. The scale factor
    can be used to scale the surface, default is (128, 128) pixels.
    """
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            image_surf = pygame.transform.scale(image_surf, scale)
            surface_list.append(image_surf)
    
    return surface_list

""" def import_folder(path):
    surface_list = []

    for _,__,img_files in walk(path):
        for image in img_files:
            fullpath = path + '/' + image
            image_surf = pygame.image.load(fullpath).convert_alpha()
            surface_list.append(image_surf)

    return surface_list """