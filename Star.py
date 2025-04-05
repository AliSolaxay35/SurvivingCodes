def star_recursive(n, i=1, direction='up'):
    if direction == 'up':
        print('*' * i)
        if i < n:
            star_recursive(n, i+1, direction)
        else:
            star_recursive(n, i-1, 'down')
    else:
        if i > 0:
            print('*' * i)
            star_recursive(n, i-1, direction)

star_recursive(5)