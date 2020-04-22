import simpy # 모듈 불러오기. C에선 라이브러리를 include로 불러왔다면 python은 import로 부름
def car(env): #def 함수선언. def 함수이름(인수)
    while True: # While True 반복문
        print('Start parking at %d' % env.now) #print('내용'). 변수를 넣고 싶을 경우 print('내용 %d' %숫자)등으로 포맷을 맞춰줘야함.
        #print('Start parking at {}' .format(env.now))를 사용하면 알아서 format을 맞춰줌.
        parking_duration = 5 # C와는 다르게 형식선언을 안해줌.
        yield env.timeout(parking_duration) # yield event(time) 형태이지만, event 대신 process가 올 경우, 그 process가 끝날 때까지 진행한다.

        print('Start driving at %d' % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

#interrupt()로 일부로 진행되는 일을 중간에 멈추게 할 수 있다. object.action.interrupt()

env = simpy.Environment() # Environment를 만드느 것.
env.process(car(env)) 
env.run(until=1000) # 시간을 제한함.