from collections import deque

bullet_price = int(input())
gun_size = int(input())
bullets = list(map(int,input().split(' ')))
locks = deque(map(int,input().split(' ')))
intelligence_value = int(input())

bullets_shot = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    
    if current_lock >= current_bullet:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')
    
    bullets_shot += 1
    
    if bullets_shot%gun_size==0 and bullets:
        print('Reloading!')

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${intelligence_value-(bullets_shot*bullet_price)}')
else:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')