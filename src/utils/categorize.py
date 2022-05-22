def al(value):
    if value < -1:
        return "\033[1m\033[38;2;255;255;255mOmni-\033[38;2;0;255;0mEgoist"
    elif value < -0.75:
        return "\033[1m\033[38;2;0;255;218mUltra-\033[38;2;10;10;10mAnarchist"
    elif value < -0.5:
        return "\033[1m\033[38;2;10;10;10mAnarchist"
    elif value < -0.25:
        return "\033[1m\033[38;2;500;200;110mLite-\033[38;2;10;10;10mAnarchism"
    elif value <= 0:
        return "\033[1m\033[38;2;119;136;153mCentrist"
    elif value < 0.25:
        return "\033[1m\033[38;2;500;200;110mLite-\033[38;2;63;81;181mAuthoritarian"
    elif value < 0.5:
        return "\033[1m\033[38;2;63;81;181mAuthoritarian"
    elif value < 0.75:
        return "\033[1m\033[38;2;0;255;218mUltra-\033[38;2;63;81;181mAuthoritarian"
    else:
        return "\033[1m\033[38;2;255;255;255mOmni-\033[1m\033[38;2;255;165;0mForceist"

def lr(value):
    if value < -1:
        return "\033[1m\033[38;2;255;255;255mOmni-\033[38;2;183;29;222mShareist"
    elif value < -0.75:
        return "\033[1m\033[38;2;0;255;218mUltra-Marxist"
    elif value < -0.5:
        return "\033[1m\033[38;2;237;29;38mMarxist"
    elif value < -0.25:
        return "\033[1m\033[38;2;500;200;110mLite-\033[38;2;237;29;38mMarxist"
    elif value <= 0:
        return "\033[1m\033[38;2;119;136;153mCentrist"
    elif value < 0.25:
        return "\033[1m\033[38;2;500;200;110mLite-\033[38;2;255;243;0mCapit\033[38;2;0;128;0malist\033[m"
    elif value < 0.5:
        return "\033[1m\033[38;2;255;243;0mCapit\033[38;2;0;128;0malist\033[m"
    elif value < 0.75:
        return "\033[1m\033[38;2;0;255;218mUltra-\033[38;2;255;243;0mCapit\033[38;2;0;128;0malist\033[m"
    else:
        return "\033[1m\033[38;2;255;255;255mOmni-\033[38;2;10;10;10mMarketist"
    