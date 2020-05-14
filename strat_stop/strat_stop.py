from ginkgo import Ginkgo
import time


class Test():

    def strat_stop(self):

        # Ginkgo继承了Config，可以直接使用a.log（self.log在config里面）
        # 如果再次调用congfig，会导致运行两遍log，打印两次
        a = Ginkgo()
        
        i =1
        while i < int(a.counts):
            #开播
            
            a.log.logger.warning('这是第' + str(i) + '播放')
           

            a.Kaibo()

            time.sleep(int(a.time))

            #停播
            a.Tingbo()
            i = i +1


if __name__ == "__main__":
    Test().strat_stop()

        
    