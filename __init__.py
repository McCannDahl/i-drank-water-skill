from mycroft import MycroftSkill, intent_file_handler


class IDrankWater(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('water.drank.i.intent')
    def handle_water_drank_i(self, message):
        self.speak_dialog('water.drank.i')


def create_skill():
    return IDrankWater()

