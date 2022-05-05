from console.ansi import get_color_escape, set_color

darkblue = get_color_escape(0, 0, 175)
yellow = get_color_escape(255, 255, 0)
red = get_color_escape(255, 0, 0)
blue = get_color_escape(0, 0, 255)
BOLD = '\033[1m'

class Ideology:
    def __init__(self, name, description, al, lr, tags, contradicts) -> None:
        self.name = name
        self.description = description
        self.al = al
        self.lr = lr
        self.contradicts = contradicts

    def tag(self, tag):
        #* Might want to change this to a dictionary to lower the time complexity...

        match tag:
            case 'capitalist':
                return "\033[1m\033[38;2;255;243;0mCapit\033[1m\033[38;2;0;128;0malist\033[m"
            case 'leftist':
                return "\033[1m\033[38;2;255;0;0mLeftist\033[m"
            case 'libertarian':
                return "\033[1m\033[38;2;255;243;0mLibert\033[1m\033[38;2;30;30;30marian\033[m"
            case 'rightist':
                return "\033[1m\033[38;2;0;0;255mRightist\033[m"
            case 'fascist':
                return "\033[1m\033[38;2;30;30;30mFacist\033[m"
            case 'welfarist':
                return "\033[1m\033[38;2;250;250;250mWelf\033[38;2;250;100;75marist\033[m"
            case 'regulationist':
                return "\033[1m\033[38;2;38;0;153mRegulat\033[38;2;255;255;255mionist\033[m"

    def info(self) -> None:
        #! This is a mess.
        print("\033[1m" + self.name + "\033[m")
        print("\n\"" + self.description + "\"")
        print(f"\n{set_color(BOLD + 'Authoritarian', darkblue)}-{set_color(BOLD + 'Libertarian', yellow)}: " + str(self.al))
        print(f"{set_color(BOLD + 'Left', red)}-{set_color(BOLD + 'Right', blue)}: " + str(self.lr))
        print("Tags: " + ", ".join([self.tag(tag) for tag in self.tags]))
        print("Contradicts: " + ", ".join([self.tag(tag) for tag in self.contradicts]))