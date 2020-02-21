from mycroft import MycroftSkill, intent_file_handler


class UpdatedMskFifteen(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fifteen.msk.updated.intent')
    def handle_fifteen_msk_updated(self, message):
        self.speak_dialog('fifteen.msk.updated')


def create_skill():
    return UpdatedMskFifteen()

