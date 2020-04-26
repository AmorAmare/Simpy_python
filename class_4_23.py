import simpy

def car(env, name, bcs, driving_time, charge_duration):
    yield env.timeout(driving_time)
    print('%s arriving at %d' %(name, env.now))
    with bcs.request() as req:   # bcs.request()의 return값을 req로 받음.
        yield req                # req의 결과값을 기다림. 서버를 요청하는 구문. 위 아래를 하나의 문법으로 생각
        print('%s starting to charge at %s' %(name, env.now))
        yield env.timeout(charge_duration)
        print('%s leaving the bcs at %s' % (name, env.now))

env = simpy.Environment()
bcs = simpy.Resource(env, capacity=2)
for i in range(4):
    env.process(car(env, 'Car %d' % i, bcs, i*2,5))
env.run()
#-----------------------------------------------
import simpy

def my_callback(event):
    print("Called back from", event)

env = simpy.Environment()
event = env.event()  # event를 만들 때, 꼭 필요함. 이벤트의 수명은 1번. 또 쓸려면 또 만들어야 함.
event.callbacks.append(my_callback)
#-------------------------------------------------
import simpy
class School:
    def __init__(self, env):
        self.env = env
        self.class_ends = env.event()
        self.pupil_pros = [env.process(self.pupil()) for i in range(3) ]
        self.bell_proc = env.process(self.bell())
    def bell(self):
        for i in range(2):
            yield self.env.timeout(45)
            self.class_ends.succeed()
            self.class_ends = self.env.event() # 이벤트 수명이 다 되어 다시 생성
            print('수업 끝')
    def pupil(self):
        for i in range(2):
            print(' /ㅇ/', 'end=')
            yield self.class_ends
env = simpy.Environment()
school = School(env)
env.run()