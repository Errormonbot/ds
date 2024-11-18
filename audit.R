rm(list=ls()) #will remove ALL objects
Base="D:"
FileDir=paste0(Base,'/MN')
dir.create(FileDir)
FileDirLog=paste0(FileDir,'/log')
dir.create(FileDirLog)
FileDirRun=paste0(FileDirLog,'/Run0001')
dir.create(FileDirRun)
StartTime=Sys.time()
debugLog=paste0(FileDirRun,'/debug.Log')
infoLog=paste0(FileDirRun,'/info.Log')
errorLog=paste0(FileDirRun,'/error.Log')
#######################################
write(paste0('Start Debug Log File',format(StartTime,"%Y/%d/%m %H:%M:%S")),file=debugLog,append=FALSE)
write(paste0('Start Information Log File',format(StartTime,"%Y/%d/%m %H:%M:%S")),file=infoLog,append=FALSE)
write(paste0('Start Error Log File',format(StartTime,"%Y/%d/%m %H:%M:%S")),file=errorLog,append=FALSE)
StopTime=Sys.time()
#######################################
write(paste0('Stop Debug Log File',format(StartTime,"%Y/%d/%m %H:%M:%S")),file=debugLog,append=TRUE)
write(paste0('Stop Information Log File',format(StartTime,"%Y/%d/%m %H:%M:%S")),file=infoLog,append=TRUE)
write(paste0('Stop Error Log File',format(StartTime,"%Y/%d/%m %H:%M:%S")),file=errorLog,append=TRUE)

