import ginkgo
import time
import logg

class test():
    '''开停播，循环'''
    def strat_stop():
        a = ginkgo.Ginkgo()
        o = int(ginkgo.Config().counts)
        i =1
        while i < o:
            #开播
            
            a.log.logger.warning('这是第' + str(i) + '播放')

            a.Kaibo()

            time.sleep(int(ginkgo.Config().time))

            #停播
            a.Tingbo()
            i += 1


if __name__ == "__main__":
    test.strat_stop()

        
    