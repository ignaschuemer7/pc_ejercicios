def match_duration(hours,minutes,seconds):
    """
    Parameters
    ----------
    hours : int
        There are the hours you will convert to seconds.
    minutes :int
        There are the minutes you will convert to seconds.
    seconds : int
        There are the seconds .

    Returns
    -------
    matchseconds : int
        Is the time of the match in seconds.
    """
    matchseconds = seconds + minutes * 60 + hours*3600
    return matchseconds

print("el partido duro",match_duration(11,6,23),"segundos")

    
