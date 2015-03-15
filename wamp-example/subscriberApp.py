#!/usr/bin/env python

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner

class Component (ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print ("READY!")        
        self.received = 0

        def on_event(data):
            print "Received message: {}".format(data)
        
        try:
            yield self.subscribe(on_event, u'com.example.test-topic')
            print "Subscribed to test-topic"
        except Exception as e:
            print("Could not subscribe to test-topic: {}".format(e))

    def onDisconnect(self):
        reactor.stop()

if __name__ == '__main__':
    runner = ApplicationRunner(url = u'ws://localhost:8080/ws', realm = u'realm1')
    runner.run(Component)
