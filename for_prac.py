import simpy
def test_condition(env):
    t1, t2 = env.timeout(1, value = 'spam'), env.timeout(2, value = 'eggs') # 1초가 지났을 때, return으로 value 값을 받는다. 즉, 1초가 지나면 t1은 return으로 스팸을 받는 것.
    ret = yield t1 | t2 # |는 or 이며 &는 and임. 스팸 혹은 계란이 완성 될 때 까지 기다림.
    assert ret == {t1:'spam'}, 'spam 완성' # assert는 조건문임. assert 조건, '메시지'
    t1, t2 = env.timeout(1, value = 'spam'), env.timeout(2, value = 'eggs')
    ret = yield t1 & t2 # 둘 다 완성될 때 까지 기다림
    assert ret == {t1: 'spam', t2: 'eggs'}, '스팸, 계란 완성'
    e1, e2, e3 = [env.timeout(i) for i in range (3)]
    yield (e1|e2) & e3
    assert all(e.triggered for e in [e1, e2, e3]), '요리 끝'
env = simpy.Environment()
env.process(test_condition(env))
env.run()