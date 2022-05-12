def tagify(tag):
    tags = {
        "capitalist": "\033[1m\033[38;2;255;243;0mCapit\033[38;2;0;128;0malist\033[m",
        "leftist": "\033[1m\033[38;2;255;0;0mLeftist\033[m",
        "libertarian": "\033[1m\033[38;2;255;243;0mLibertarian\033[m",
        "rightist": "\033[1m\033[38;2;0;0;255mRightist\033[m",
        "fascist": "\033[1m\033[38;2;20;20;20mFac\033[38;2;203;171;114mis\033[38;2;196;196;196mt\033[m",
        "welfarist": "\033[1m\033[38;2;250;250;250mWelf\033[38;2;250;100;75marist\033[m",
        "regulationist": "\033[1m\033[38;2;38;0;153mRegulat\033[38;2;255;255;255mionist\033[m",
        "individualist": "\033[1m\033[38;2;0;255;218mIndividualist\033[m",
        "anarchist": "\033[1m\033[38;2;10;10;10mAnarchist\033[m",
        "collectivist": "\033[1m\033[38;2;137;0;20mCollectivist\033[m"
    }

    try:
        return tags[tag]
    except KeyError:
        return f"\033[1m\033[28;2;142;142;142m{tag}\033[m"