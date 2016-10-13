# encoding: utf-8

from igetui.pb import get_req_pb2 as pb


class Transmission(object):

    def __init__(self):
        self.type = 0
        pass

    def get_action_chains(self):
        # set action chain
        action_chain1 = pb.ActionChain()
        action_chain1.actionId = 1
        action_chain1.type = pb.ActionChain.Goto
        action_chain1.next = 10030

        # app startup
        app_startup = pb.AppStartUp()
        app_startup.android = ""
        app_startup.symbia = ""
        app_startup.ios = ""

        # start up app
        action_chain2 = pb.ActionChain()
        action_chain2.actionId = 10030
        action_chain2.type = pb.ActionChain.startapp
        action_chain2.appid = ""
        action_chain2.autostart = (True if self.type == 1 else False)
        action_chain2.appstartupid.CopyFrom(app_startup)
        action_chain2.failedAction = 100
        action_chain2.next = 100

        # end
        action_chain3 = pb.ActionChain()
        action_chain3.actionId = 100
        action_chain3.type = pb.ActionChain.eoa

        return [action_chain1, action_chain2, action_chain3]
