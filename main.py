from messageLogs_functions import *
from analyzePodMessages import *
from analyzeAllPodsInDeviceLog import *
from utils_report import *

    # Copied from analyzeMessageLogsRev3 then configure for new Device Log
    # Need this to work with either format - change logic stepwise to be
    # more modular until done

def main(thisPath, thisFile, outFile, vFlag):
    # configure default values to return if something goes wrong
    df = []
    podState = []
    actionFrame = []
    actionSummary = []
    # decide how to manage this
    filename = thisPath + '/' + thisFile
    fileType, podFrame, podDict, fault_report = persist_read_file(filename)


    if fileType == "unknown":
        print('Did not recognize file type')
    else:
        if fileType == "messageLog":
            print('__________________________________________\n')
            print('  This file uses MessageLog, {:s}'.format(thisFile))
            print('__________________________________________\n')
            numChunks = 1 # number of pods in log file is always 1
            df, podState, actionFrame, actionSummary = analyzePodMessages(thisFile,
                podFrame, podDict, fault_report, outFile, vFlag, numChunks)

        elif fileType == "deviceLog":
            print('__________________________________________\n')
            print('  This file uses Device Communication Log, {:s}'.format(thisFile))
            print('__________________________________________\n')
            df, podState, actionFrame, actionSummary = analyzeAllPodsInDeviceLog(thisFile,
                podFrame, podDict, fault_report, outFile, vFlag)

    return df, podState, actionFrame, actionSummary
