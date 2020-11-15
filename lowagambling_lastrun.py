#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.1.3),
    on 十一月 14, 2020, at 19:39
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2020.1.3'
expName = 'lowagambling'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='\\\\Mac\\Home\\Desktop\\LowaGamblingpsychopy\\lowagambling_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1680, 1050], fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "LOAD_DECKS"
LOAD_DECKSClock = core.Clock()
allCards = data.importConditions("conditions.xlsx")

# default borrowed value and networth
borrow = float(2000)
net_worth = float(2000)


# Store each card deck as seperate 
A_cards = list(filter(lambda x: x["DECK_NAME"] == "A", allCards))
B_cards = list(filter(lambda x: x["DECK_NAME"] == "B", allCards))
C_cards = list(filter(lambda x: x["DECK_NAME"] == "C", allCards))
D_cards = list(filter(lambda x: x["DECK_NAME"] == "D", allCards))

# Total number of trials
totalReps = 100

# image path
img_0 = 'Resourse/no_card_left.png'
img_1 = 'Resourse/deckback.png'

# default image for each deck
img_a = img_1
img_b = img_1
img_c = img_1
img_d = img_1


# Card select at each deck
A_idx = 0
B_idx = 0
C_idx = 0
D_idx = 0

# Default text
borrowed_text = "借款: {}".format(f'{borrow:.0f}')
net_worth_text = "总收入: {}".format(f'{net_worth:.0f}')

# Default allowed keys
allowed_keys = ['1', '2', '3', '4']

# initializating arguements
current_card_property = dict()
current_color = 0
current_win = 0
current_loss = 0
respX = 0

# Initialize components for Routine "INSTR"
INSTRClock = core.Clock()
instrtext = visual.TextStim(win=win, name='instrtext',
    text='欢迎参加本次实验！\n在你面前的是四张牌，你的任务是\n抽取任意一张，翻牌后会获得相应\n的奖金，并加进你的2000元借款中，\n注意，有些时候，你也很会受到一\n定的罚金，将会从你获得的总收入\n中扣除。你的目的是获得尽可能多\n的收入。\nA,B,C,D对应着键盘的1，2，3，4\n\n<请按空格键继续>',
    font='Microsoft yahei',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

# Initialize components for Routine "TRIAL"
TRIALClock = core.Clock()
deck_a = visual.ImageStim(
    win=win,
    name='deck_a', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
deck_b = visual.ImageStim(
    win=win,
    name='deck_b', 
    image='sin', mask=None,
    ori=0, pos=(-0.17, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
deck_c = visual.ImageStim(
    win=win,
    name='deck_c', 
    image='sin', mask=None,
    ori=0, pos=(0.17, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
deck_d = visual.ImageStim(
    win=win,
    name='deck_d', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
resp = keyboard.Keyboard()
text_a = visual.TextStim(win=win, name='text_a',
    text='A',
    font='Microsoft yahei',
    pos=(-0.5, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_b = visual.TextStim(win=win, name='text_b',
    text='B',
    font='Microsoft yahei',
    pos=(-0.17, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_c = visual.TextStim(win=win, name='text_c',
    text='C',
    font='Microsoft yahei',
    pos=(0.17, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_d = visual.TextStim(win=win, name='text_d',
    text='D',
    font='Arial',
    pos=(0.5, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
borrow_value = visual.TextStim(win=win, name='borrow_value',
    text='default text',
    font='Microsoft yahei',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
net_worth_value = visual.TextStim(win=win, name='net_worth_value',
    text='default text',
    font='Microsoft yahei',
    pos=(0, 0.40), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);

# Initialize components for Routine "FEEDBACK"
FEEDBACKClock = core.Clock()
deck_a_feedback = visual.ImageStim(
    win=win,
    name='deck_a_feedback', 
    image='sin', mask=None,
    ori=0, pos=(-0.5, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
deck_b_feedback = visual.ImageStim(
    win=win,
    name='deck_b_feedback', 
    image='sin', mask=None,
    ori=0, pos=(-0.17, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-2.0)
deck_c_feedback = visual.ImageStim(
    win=win,
    name='deck_c_feedback', 
    image='sin', mask=None,
    ori=0, pos=(0.17, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-3.0)
deck_d_feedback = visual.ImageStim(
    win=win,
    name='deck_d_feedback', 
    image='sin', mask=None,
    ori=0, pos=(0.5, 0), size=(0.25, 0.35),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-4.0)
chosen_card = visual.Rect(
    win=win, name='chosen_card',
    width=(0.25, 0.35)[0], height=(0.25, 0.35)[1],
    ori=0, pos=[0,0],
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=1.0, fillColorSpace='rgb',
    opacity=1, depth=-5.0, interpolate=True)
text_a_feedback = visual.TextStim(win=win, name='text_a_feedback',
    text='A',
    font='Microsoft yahei',
    pos=(-0.5, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-6.0);
text_b_feedback = visual.TextStim(win=win, name='text_b_feedback',
    text='B',
    font='Microsoft yahei',
    pos=(-0.17, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-7.0);
text_c_feedback = visual.TextStim(win=win, name='text_c_feedback',
    text='C',
    font='Microsoft yahei',
    pos=(0.17, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-8.0);
text_d_feedback = visual.TextStim(win=win, name='text_d_feedback',
    text='D',
    font='Microsoft yahei',
    pos=(0.5, 0.20), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-9.0);
borrow_value_feedback = visual.TextStim(win=win, name='borrow_value_feedback',
    text='default text',
    font='Microsoft yahei',
    pos=(0, 0.45), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-10.0);
net_worth_value_feedback = visual.TextStim(win=win, name='net_worth_value_feedback',
    text='default text',
    font='Microsoft yahei',
    pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-11.0);
feedback_trial = visual.TextStim(win=win, name='feedback_trial',
    text='default text',
    font='Microsoft yahei',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-12.0);

# Initialize components for Routine "END"
ENDClock = core.Clock()
thank_you = visual.TextStim(win=win, name='thank_you',
    text='谢谢您参与本次实验',
    font='Microsoft yahei',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "LOAD_DECKS"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
LOAD_DECKSComponents = []
for thisComponent in LOAD_DECKSComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
LOAD_DECKSClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "LOAD_DECKS"-------
while continueRoutine:
    # get current time
    t = LOAD_DECKSClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=LOAD_DECKSClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in LOAD_DECKSComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "LOAD_DECKS"-------
for thisComponent in LOAD_DECKSComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "LOAD_DECKS" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "INSTR"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
INSTRComponents = [instrtext, key_resp]
for thisComponent in INSTRComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
INSTRClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "INSTR"-------
while continueRoutine:
    # get current time
    t = INSTRClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=INSTRClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrtext* updates
    if instrtext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrtext.frameNStart = frameN  # exact frame index
        instrtext.tStart = t  # local t and not account for scr refresh
        instrtext.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrtext, 'tStartRefresh')  # time at next scr refresh
        instrtext.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in INSTRComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "INSTR"-------
for thisComponent in INSTRComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrtext.started', instrtext.tStartRefresh)
thisExp.addData('instrtext.stopped', instrtext.tStopRefresh)
# the Routine "INSTR" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=totalReps, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "TRIAL"-------
    continueRoutine = True
    # update component parameters for each repeat
    net_worth = net_worth - float(current_loss) + float(current_win)
    
    borrowed_text = "借款: {}".format(f'{borrow:.0f}')
    net_worth_text = "总收入: {}".format(f'{net_worth:.0f}')
    deck_a.setImage(img_a)
    deck_b.setImage(img_b)
    deck_c.setImage(img_c)
    deck_d.setImage(img_d)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    borrow_value.setText(borrowed_text)
    net_worth_value.setText(net_worth_text)
    # keep track of which components have finished
    TRIALComponents = [deck_a, deck_b, deck_c, deck_d, resp, text_a, text_b, text_c, text_d, borrow_value, net_worth_value]
    for thisComponent in TRIALComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    TRIALClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "TRIAL"-------
    while continueRoutine:
        # get current time
        t = TRIALClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=TRIALClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *deck_a* updates
        if deck_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_a.frameNStart = frameN  # exact frame index
            deck_a.tStart = t  # local t and not account for scr refresh
            deck_a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_a, 'tStartRefresh')  # time at next scr refresh
            deck_a.setAutoDraw(True)
        
        # *deck_b* updates
        if deck_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_b.frameNStart = frameN  # exact frame index
            deck_b.tStart = t  # local t and not account for scr refresh
            deck_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_b, 'tStartRefresh')  # time at next scr refresh
            deck_b.setAutoDraw(True)
        
        # *deck_c* updates
        if deck_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_c.frameNStart = frameN  # exact frame index
            deck_c.tStart = t  # local t and not account for scr refresh
            deck_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_c, 'tStartRefresh')  # time at next scr refresh
            deck_c.setAutoDraw(True)
        
        # *deck_d* updates
        if deck_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_d.frameNStart = frameN  # exact frame index
            deck_d.tStart = t  # local t and not account for scr refresh
            deck_d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_d, 'tStartRefresh')  # time at next scr refresh
            deck_d.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # AllowedKeys looks like a variable named `allowed_keys`
            if not type(allowed_keys) in [list, tuple, np.ndarray]:
                if not isinstance(allowed_keys, str):
                    logging.error('AllowedKeys variable `allowed_keys` is not string- or list-like.')
                    core.quit()
                elif not ',' in allowed_keys:
                    allowed_keys = (allowed_keys,)
                else:
                    allowed_keys = eval(allowed_keys)
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=list(allowed_keys), waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_a* updates
        if text_a.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_a.frameNStart = frameN  # exact frame index
            text_a.tStart = t  # local t and not account for scr refresh
            text_a.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_a, 'tStartRefresh')  # time at next scr refresh
            text_a.setAutoDraw(True)
        
        # *text_b* updates
        if text_b.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_b.frameNStart = frameN  # exact frame index
            text_b.tStart = t  # local t and not account for scr refresh
            text_b.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_b, 'tStartRefresh')  # time at next scr refresh
            text_b.setAutoDraw(True)
        
        # *text_c* updates
        if text_c.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_c.frameNStart = frameN  # exact frame index
            text_c.tStart = t  # local t and not account for scr refresh
            text_c.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_c, 'tStartRefresh')  # time at next scr refresh
            text_c.setAutoDraw(True)
        
        # *text_d* updates
        if text_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_d.frameNStart = frameN  # exact frame index
            text_d.tStart = t  # local t and not account for scr refresh
            text_d.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_d, 'tStartRefresh')  # time at next scr refresh
            text_d.setAutoDraw(True)
        
        # *borrow_value* updates
        if borrow_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            borrow_value.frameNStart = frameN  # exact frame index
            borrow_value.tStart = t  # local t and not account for scr refresh
            borrow_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(borrow_value, 'tStartRefresh')  # time at next scr refresh
            borrow_value.setAutoDraw(True)
        
        # *net_worth_value* updates
        if net_worth_value.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            net_worth_value.frameNStart = frameN  # exact frame index
            net_worth_value.tStart = t  # local t and not account for scr refresh
            net_worth_value.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(net_worth_value, 'tStartRefresh')  # time at next scr refresh
            net_worth_value.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in TRIALComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "TRIAL"-------
    for thisComponent in TRIALComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('deck_a.started', deck_a.tStartRefresh)
    trials.addData('deck_a.stopped', deck_a.tStopRefresh)
    trials.addData('deck_b.started', deck_b.tStartRefresh)
    trials.addData('deck_b.stopped', deck_b.tStopRefresh)
    trials.addData('deck_c.started', deck_c.tStartRefresh)
    trials.addData('deck_c.stopped', deck_c.tStopRefresh)
    trials.addData('deck_d.started', deck_d.tStartRefresh)
    trials.addData('deck_d.stopped', deck_d.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
    trials.addData('resp.keys',resp.keys)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    trials.addData('text_a.started', text_a.tStartRefresh)
    trials.addData('text_a.stopped', text_a.tStopRefresh)
    trials.addData('text_b.started', text_b.tStartRefresh)
    trials.addData('text_b.stopped', text_b.tStopRefresh)
    trials.addData('text_c.started', text_c.tStartRefresh)
    trials.addData('text_c.stopped', text_c.tStopRefresh)
    trials.addData('text_d.started', text_d.tStartRefresh)
    trials.addData('text_d.stopped', text_d.tStopRefresh)
    trials.addData('borrow_value.started', borrow_value.tStartRefresh)
    trials.addData('borrow_value.stopped', borrow_value.tStopRefresh)
    trials.addData('net_worth_value.started', net_worth_value.tStartRefresh)
    trials.addData('net_worth_value.stopped', net_worth_value.tStopRefresh)
    # the Routine "TRIAL" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "FEEDBACK"-------
    continueRoutine = True
    routineTimer.add(2.500000)
    # update component parameters for each repeat
    # initializating arguements
    current_card_property = dict()
    current_color = []
    current_win = []
    current_loss = []
    respX = 0
    
    # chose which deck
    if resp.keys[0] == '1':
        current_card_property = dict(A_cards[A_idx])
        respX = -0.5
    
        if A_idx == 39:
            img_a = img_0 # set the image to non_exist
            allowed_keys.remove('1') # remove the allowed key for preventing bug
        else:
            A_idx += 1
    
    elif resp.keys[0] == '2':
        current_card_property = dict(B_cards[B_idx])
        respX = -0.17
    
        if B_idx == 39:
            img_b = img_0
            allowed_keys.remove('2')
        else:
            B_idx += 1
    
    elif resp.keys[0] == '3':
        current_card_property = dict(C_cards[C_idx])
        respX = 0.17
    
        if C_idx == 39:
            img_c = img_0
            allowed_keys.remove('3')
        else:
            C_idx += 1
    
    
    elif resp.keys[0] == '4':
        current_card_property = dict(D_cards[D_idx])
        respX = 0.5
    
        if D_idx == 39:
            img_d = img_0
            allowed_keys.remove('4')
        else:
            D_idx += 1
    
    current_color = current_card_property["COLOR"]
    current_win = current_card_property["EARNINGS"]
    current_loss = current_card_property["LOSSES"]
    
    
    
    
    feedback_text = "你赢了{}元, 但是你输了{}元". format(current_win, current_loss)
    
    if net_worth <= 0:
        countinueRountine = False
    deck_a_feedback.setImage(img_a)
    deck_b_feedback.setImage(img_b)
    deck_c_feedback.setImage(img_c)
    deck_d_feedback.setImage(img_d)
    chosen_card.setPos((respX, 0))
    chosen_card.setFillColor(current_color)
    borrow_value_feedback.setText(borrowed_text)
    net_worth_value_feedback.setText(net_worth_text)
    feedback_trial.setText(feedback_text)
    # keep track of which components have finished
    FEEDBACKComponents = [deck_a_feedback, deck_b_feedback, deck_c_feedback, deck_d_feedback, chosen_card, text_a_feedback, text_b_feedback, text_c_feedback, text_d_feedback, borrow_value_feedback, net_worth_value_feedback, feedback_trial]
    for thisComponent in FEEDBACKComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    FEEDBACKClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "FEEDBACK"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = FEEDBACKClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=FEEDBACKClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *deck_a_feedback* updates
        if deck_a_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_a_feedback.frameNStart = frameN  # exact frame index
            deck_a_feedback.tStart = t  # local t and not account for scr refresh
            deck_a_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_a_feedback, 'tStartRefresh')  # time at next scr refresh
            deck_a_feedback.setAutoDraw(True)
        if deck_a_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > deck_a_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                deck_a_feedback.tStop = t  # not accounting for scr refresh
                deck_a_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(deck_a_feedback, 'tStopRefresh')  # time at next scr refresh
                deck_a_feedback.setAutoDraw(False)
        
        # *deck_b_feedback* updates
        if deck_b_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_b_feedback.frameNStart = frameN  # exact frame index
            deck_b_feedback.tStart = t  # local t and not account for scr refresh
            deck_b_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_b_feedback, 'tStartRefresh')  # time at next scr refresh
            deck_b_feedback.setAutoDraw(True)
        if deck_b_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > deck_b_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                deck_b_feedback.tStop = t  # not accounting for scr refresh
                deck_b_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(deck_b_feedback, 'tStopRefresh')  # time at next scr refresh
                deck_b_feedback.setAutoDraw(False)
        
        # *deck_c_feedback* updates
        if deck_c_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_c_feedback.frameNStart = frameN  # exact frame index
            deck_c_feedback.tStart = t  # local t and not account for scr refresh
            deck_c_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_c_feedback, 'tStartRefresh')  # time at next scr refresh
            deck_c_feedback.setAutoDraw(True)
        if deck_c_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > deck_c_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                deck_c_feedback.tStop = t  # not accounting for scr refresh
                deck_c_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(deck_c_feedback, 'tStopRefresh')  # time at next scr refresh
                deck_c_feedback.setAutoDraw(False)
        
        # *deck_d_feedback* updates
        if deck_d_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            deck_d_feedback.frameNStart = frameN  # exact frame index
            deck_d_feedback.tStart = t  # local t and not account for scr refresh
            deck_d_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(deck_d_feedback, 'tStartRefresh')  # time at next scr refresh
            deck_d_feedback.setAutoDraw(True)
        if deck_d_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > deck_d_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                deck_d_feedback.tStop = t  # not accounting for scr refresh
                deck_d_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(deck_d_feedback, 'tStopRefresh')  # time at next scr refresh
                deck_d_feedback.setAutoDraw(False)
        
        # *chosen_card* updates
        if chosen_card.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            chosen_card.frameNStart = frameN  # exact frame index
            chosen_card.tStart = t  # local t and not account for scr refresh
            chosen_card.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(chosen_card, 'tStartRefresh')  # time at next scr refresh
            chosen_card.setAutoDraw(True)
        if chosen_card.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > chosen_card.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                chosen_card.tStop = t  # not accounting for scr refresh
                chosen_card.frameNStop = frameN  # exact frame index
                win.timeOnFlip(chosen_card, 'tStopRefresh')  # time at next scr refresh
                chosen_card.setAutoDraw(False)
        
        # *text_a_feedback* updates
        if text_a_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_a_feedback.frameNStart = frameN  # exact frame index
            text_a_feedback.tStart = t  # local t and not account for scr refresh
            text_a_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_a_feedback, 'tStartRefresh')  # time at next scr refresh
            text_a_feedback.setAutoDraw(True)
        if text_a_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_a_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_a_feedback.tStop = t  # not accounting for scr refresh
                text_a_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_a_feedback, 'tStopRefresh')  # time at next scr refresh
                text_a_feedback.setAutoDraw(False)
        
        # *text_b_feedback* updates
        if text_b_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_b_feedback.frameNStart = frameN  # exact frame index
            text_b_feedback.tStart = t  # local t and not account for scr refresh
            text_b_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_b_feedback, 'tStartRefresh')  # time at next scr refresh
            text_b_feedback.setAutoDraw(True)
        if text_b_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_b_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_b_feedback.tStop = t  # not accounting for scr refresh
                text_b_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_b_feedback, 'tStopRefresh')  # time at next scr refresh
                text_b_feedback.setAutoDraw(False)
        
        # *text_c_feedback* updates
        if text_c_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_c_feedback.frameNStart = frameN  # exact frame index
            text_c_feedback.tStart = t  # local t and not account for scr refresh
            text_c_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_c_feedback, 'tStartRefresh')  # time at next scr refresh
            text_c_feedback.setAutoDraw(True)
        if text_c_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_c_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_c_feedback.tStop = t  # not accounting for scr refresh
                text_c_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_c_feedback, 'tStopRefresh')  # time at next scr refresh
                text_c_feedback.setAutoDraw(False)
        
        # *text_d_feedback* updates
        if text_d_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_d_feedback.frameNStart = frameN  # exact frame index
            text_d_feedback.tStart = t  # local t and not account for scr refresh
            text_d_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_d_feedback, 'tStartRefresh')  # time at next scr refresh
            text_d_feedback.setAutoDraw(True)
        if text_d_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_d_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                text_d_feedback.tStop = t  # not accounting for scr refresh
                text_d_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_d_feedback, 'tStopRefresh')  # time at next scr refresh
                text_d_feedback.setAutoDraw(False)
        
        # *borrow_value_feedback* updates
        if borrow_value_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            borrow_value_feedback.frameNStart = frameN  # exact frame index
            borrow_value_feedback.tStart = t  # local t and not account for scr refresh
            borrow_value_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(borrow_value_feedback, 'tStartRefresh')  # time at next scr refresh
            borrow_value_feedback.setAutoDraw(True)
        if borrow_value_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > borrow_value_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                borrow_value_feedback.tStop = t  # not accounting for scr refresh
                borrow_value_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(borrow_value_feedback, 'tStopRefresh')  # time at next scr refresh
                borrow_value_feedback.setAutoDraw(False)
        
        # *net_worth_value_feedback* updates
        if net_worth_value_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            net_worth_value_feedback.frameNStart = frameN  # exact frame index
            net_worth_value_feedback.tStart = t  # local t and not account for scr refresh
            net_worth_value_feedback.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(net_worth_value_feedback, 'tStartRefresh')  # time at next scr refresh
            net_worth_value_feedback.setAutoDraw(True)
        if net_worth_value_feedback.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > net_worth_value_feedback.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                net_worth_value_feedback.tStop = t  # not accounting for scr refresh
                net_worth_value_feedback.frameNStop = frameN  # exact frame index
                win.timeOnFlip(net_worth_value_feedback, 'tStopRefresh')  # time at next scr refresh
                net_worth_value_feedback.setAutoDraw(False)
        
        # *feedback_trial* updates
        if feedback_trial.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            feedback_trial.frameNStart = frameN  # exact frame index
            feedback_trial.tStart = t  # local t and not account for scr refresh
            feedback_trial.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_trial, 'tStartRefresh')  # time at next scr refresh
            feedback_trial.setAutoDraw(True)
        if feedback_trial.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_trial.tStartRefresh + 1.5-frameTolerance:
                # keep track of stop time/frame for later
                feedback_trial.tStop = t  # not accounting for scr refresh
                feedback_trial.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_trial, 'tStopRefresh')  # time at next scr refresh
                feedback_trial.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FEEDBACKComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "FEEDBACK"-------
    for thisComponent in FEEDBACKComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('deck_a_feedback.started', deck_a_feedback.tStartRefresh)
    trials.addData('deck_a_feedback.stopped', deck_a_feedback.tStopRefresh)
    trials.addData('deck_b_feedback.started', deck_b_feedback.tStartRefresh)
    trials.addData('deck_b_feedback.stopped', deck_b_feedback.tStopRefresh)
    trials.addData('deck_c_feedback.started', deck_c_feedback.tStartRefresh)
    trials.addData('deck_c_feedback.stopped', deck_c_feedback.tStopRefresh)
    trials.addData('deck_d_feedback.started', deck_d_feedback.tStartRefresh)
    trials.addData('deck_d_feedback.stopped', deck_d_feedback.tStopRefresh)
    trials.addData('chosen_card.started', chosen_card.tStartRefresh)
    trials.addData('chosen_card.stopped', chosen_card.tStopRefresh)
    trials.addData('text_a_feedback.started', text_a_feedback.tStartRefresh)
    trials.addData('text_a_feedback.stopped', text_a_feedback.tStopRefresh)
    trials.addData('text_b_feedback.started', text_b_feedback.tStartRefresh)
    trials.addData('text_b_feedback.stopped', text_b_feedback.tStopRefresh)
    trials.addData('text_c_feedback.started', text_c_feedback.tStartRefresh)
    trials.addData('text_c_feedback.stopped', text_c_feedback.tStopRefresh)
    trials.addData('text_d_feedback.started', text_d_feedback.tStartRefresh)
    trials.addData('text_d_feedback.stopped', text_d_feedback.tStopRefresh)
    trials.addData('borrow_value_feedback.started', borrow_value_feedback.tStartRefresh)
    trials.addData('borrow_value_feedback.stopped', borrow_value_feedback.tStopRefresh)
    trials.addData('net_worth_value_feedback.started', net_worth_value_feedback.tStartRefresh)
    trials.addData('net_worth_value_feedback.stopped', net_worth_value_feedback.tStopRefresh)
    trials.addData('feedback_trial.started', feedback_trial.tStartRefresh)
    trials.addData('feedback_trial.stopped', feedback_trial.tStopRefresh)
    thisExp.nextEntry()
    
# completed totalReps repeats of 'trials'


# ------Prepare to start Routine "END"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
ENDComponents = [thank_you]
for thisComponent in ENDComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
ENDClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "END"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = ENDClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=ENDClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thank_you* updates
    if thank_you.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thank_you.frameNStart = frameN  # exact frame index
        thank_you.tStart = t  # local t and not account for scr refresh
        thank_you.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thank_you, 'tStartRefresh')  # time at next scr refresh
        thank_you.setAutoDraw(True)
    if thank_you.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thank_you.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            thank_you.tStop = t  # not accounting for scr refresh
            thank_you.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thank_you, 'tStopRefresh')  # time at next scr refresh
            thank_you.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ENDComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "END"-------
for thisComponent in ENDComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thank_you.started', thank_you.tStartRefresh)
thisExp.addData('thank_you.stopped', thank_you.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
