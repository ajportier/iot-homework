#!/usr/bin/env python

from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from autobahn.twisted.util import sleep
from autobahn.twisted.wamp import ApplicationSession, ApplicationRunner
import time,datetime

def getData():
    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    data = "It is now {}".format(timestamp)
    return data

class Component(ApplicationSession):
    @inlineCallbacks
    def onJoin(self, details):
        print ("READY!")
        while True:
            data = getData()
            print "Sending message: {}".format(data)
            self.publish(u'com.example.test-topic', data)
            yield sleep(1)

if __name__ == '__main__':
    runner = ApplicationRunner(url = u'ws://localhost:8080/ws', realm = u'realm1')
    runner.run(Component)
