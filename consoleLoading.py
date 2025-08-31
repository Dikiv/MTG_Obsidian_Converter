import itertools
import time
import sys

class ConsoleLoading():
    def __init__(self):
        self.done = False
    
    def runLoading(self):
        for c in itertools.cycle(['Untap.', 'Untap..', 'Untap...', 'Upkeep.', 'Upkeep..', 'Upkeep...', 'Draw.', 'Draw..', 'Draw...']):
            if self.done:
                break
            sys.stdout.write('\r' + c)
            sys.stdout.flush()
            time.sleep(0.2)
        sys.stdout.write('\rDone!     ')


    def stopLoading(self):
        self.done = True

#l = ConsoleLoading()
#t = threading.Thread(target = l.runLoading)
#t.start()