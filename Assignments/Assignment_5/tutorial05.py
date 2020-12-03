#CS384 2020 Assignment 5 - Web Series Renamer
#Satyam kumar
#1801EE48
#Submission Date:16th November 2020
import os
import re


def renamed_FIR_series(padding_episode,padding_season=0):
    # rename Logic for FIR series
    path = r'./Subtitles/FIR'
    episode_no = ''
    for file_name in os.listdir(path):
        pattern = re.compile(r'\d+')
        list_1 = re.findall(pattern, file_name)
        episode_no = list_1[0]
        while(len(episode_no) < padding_episode):
            episode_no = '0'+episode_no
        if(len(episode_no) > padding_episode):
            episode_no = episode_no[-1*padding_episode:]
        if file_name.endswith(".mp4"):
            if not os.path.isfile(path+'/'+'FIR'+' - Episode '+episode_no+'.mp4'):
                os.rename(path+'/'+file_name, path+'/'+'FIR' +
                          ' - Episode '+episode_no+'.mp4')
            else:
                os.remove(path+'/'+file_name)
        if(file_name.endswith('.srt')):
            if not os.path.isfile(path+'/'+'FIR'+' - Episode '+episode_no+'.srt'):
                os.rename(path+'/'+file_name, path+'/'+'FIR' +
                          ' - Episode '+episode_no+'.srt')
            else:
                os.remove(path+'/'+file_name)
    pass


def renamed_Game_of_Thrones_series(padding_season, padding_episode):
    # rename Logic for game of thrones series
    path = r'./Subtitles/Game of Thrones'
    season_no = ''
    episode_no = ''
    episode_name = ''
    for file_name in os.listdir(path):
        list_2 = file_name.split(' - ')
        season_no = list_2[1][0:list_2[1].index('x')]
        episode_no = list_2[1][list_2[1].index('x')+1:]
        episode_name = list_2[2][0:list_2[2].index('.')]
        while(len(season_no) < padding_season):
            season_no = '0'+season_no
        if(len(season_no) > padding_season):
            season_no = season_no[-1*padding_season:]
        while(len(episode_no) < padding_episode):
            episode_no = '0'+episode_no
        if(len(episode_no) > padding_episode):
            episode_no = episode_no[-1*padding_episode:]
        if file_name.endswith(".mp4"):
            os.rename(path+'/'+file_name, path+'/' +
                      list_2[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.mp4')
        if(file_name.endswith('.srt')):
            os.rename(path+'/'+file_name, path+'/' +
                      list_2[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.srt')
    pass


def renamed_Sherlock_series(padding_season, padding_episode):
    # rename Logic for sherlock series
    path = r'./Subtitles/Sherlock'
    season_no = ''
    episode_no = ''
    for file_name in os.listdir(path):
        list_3 = file_name[file_name.index('.')+1:]
        season_no = list_3[1]+list_3[2]
        list_3_2 = list_3[list_3.index('E')+1:]
        episode_no = list_3_2[0]+list_3_2[1]
        while(len(season_no) < padding_season):
            season_no = '0'+season_no
        if(len(season_no) > padding_season):
            season_no = season_no[-1*padding_season:]
        while(len(episode_no) < padding_episode):
            episode_no = '0'+episode_no
        if(len(episode_no) > padding_episode):
            episode_no = episode_no[-1*padding_episode:]
        if file_name.endswith(".mp4"):
            os.rename(path+'/'+file_name, path+'/'+'Sherlock' +
                      ' - Season '+season_no+' Episode '+episode_no+'.mp4')
        if(file_name.endswith('.srt')):
            os.rename(path+'/'+file_name, path+'/'+'Sherlock' +
                      ' - Season '+season_no+' Episode '+episode_no+'.srt')
    pass


def renamed_Suits_series(padding_season, padding_episode):
    # rename Logic for suits series
    path = r'./Subtitles/Suits'
    season_no = ''
    episode_no = ''
    episode_name = ''
    for file_name in os.listdir(path):
        list_4 = file_name.split(' - ')
        season_no = list_4[1][0:list_4[1].index('x')]
        episode_no = list_4[1][list_4[1].index('x')+1:]
        list_3_1 = list_4[2].split('.480')
        list_3_2 = list_3_1[0].split('.720')
        list_3_3 = list_3_2[0].split('.1080')
        list_3_4 = list_3_3[0].split('.HDTV')
        episode_name = list_3_4[0].split('.en')[0]
        while(len(season_no) < padding_season):
            season_no = '0'+season_no
        if(len(season_no) > padding_season):
            season_no = season_no[-1*padding_season:]
        while(len(episode_no) < padding_episode):
            episode_no = '0'+episode_no
        if(len(episode_no) > padding_episode):
            episode_no = episode_no[-1*padding_episode:]
        if file_name.endswith(".mp4"):
            if not os.path.isfile(path+'/'+list_4[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.mp4'):
                os.rename(path+'/'+file_name, path+'/' +
                          list_4[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.mp4')
            else:
                os.remove(path+'/'+file_name)
        if(file_name.endswith('.srt')):
            if not os.path.isfile(path+'/'+list_4[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.srt'):
                os.rename(path+'/'+file_name, path+'/' +
                          list_4[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.srt')
            else:
                os.remove(path+'/'+file_name)
    pass


def renamed_How_I_Met_Your_Mother_series(padding_season, padding_episode):
    # rename Logic for how i met your mother series.
    path = r'./Subtitles/How I Met Your Mother'
    season_no = ''
    episode_no = ''
    episode_name = ''
    for file_name in os.listdir(path):
        list_5 = file_name.split(' - ')
        season_no = list_5[1][0:list_5[1].index('x')]
        episode_no = list_5[1][list_5[1].index('x')+1:]
        list_3_1 = list_5[2].split('.480')
        list_3_2 = list_3_1[0].split('.720')
        list_3_3 = list_3_2[0].split('.1080')
        list_3_4 = list_3_3[0].split('.HDTV')
        episode_name = list_3_4[0].split('.en')[0]
        while(len(season_no) < padding_season):
            season_no = '0'+season_no
        if(len(season_no) > padding_season):
            season_no = season_no[-1*padding_season:]
        while(len(episode_no) < padding_episode):
            episode_no = '0'+episode_no
        if(len(episode_no) > padding_episode):
            episode_no = episode_no[-1*padding_episode:]
        if file_name.endswith(".mp4"):
            if not os.path.isfile(path+'/'+list_5[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.mp4'):
                os.rename(path+'/'+file_name, path+'/' +
                          list_5[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.mp4')
            else:
                os.remove(path+'/'+file_name)
        if(file_name.endswith('.srt')):
            if not os.path.isfile(path+'/'+list_5[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.srt'):
                os.rename(path+'/'+file_name, path+'/' +
                          list_5[0]+' - Season '+season_no+' Episode '+episode_no+' - '+episode_name+'.srt')
            else:
                os.remove(path+'/'+file_name)
    pass


renamed_FIR_series(6)
renamed_Game_of_Thrones_series(3, 3)
renamed_How_I_Met_Your_Mother_series(3, 3)
renamed_Sherlock_series(3, 3)
renamed_Suits_series(3, 3)