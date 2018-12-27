from sys import argv

def count_lines(fname):
    n = 1
    with open(fname, 'rb') as f:
        for line in f: n += 1
    return n

def _insert_text(fname, text, line_no):
    n = 1
    b_text = text.encode('ASCII')
    with open(fname, 'wb+') as f:
        for line in f:
            if n == line_no: f.writelines(b_text)
            else: continue
            n += 1

def insert_text(fname, text, line_no):
    
    with open(fname,  'rb') as f:
        data = f.readlines()
    
    data[line_no] = text.encode('ASCII')

    with open(fname, 'wb') as f:
        f.writelines(data)

def secret_math(x,y,z):
    result = ( x**3 + y**2 ) / z
    return int(result)

def choose_line(n_lines, fname):
    f = fname.split('/')[-1]
    d_chars = []

    for c in f[:3]:
        d_char = ord(c)
        print(c, d_char)
        d_chars.append(ord(c))

    x0, x1, x2 = d_chars[:3]
    y = secret_math(x0, x1, x2)
    print('n_lines', n_lines)
    print('secret math', y)
    line_no = y % n_lines

    #print('d_chars', x0, x1, x2)

    print('line_no', line_no)
    return line_no


if __name__ == '__main__':
    fname = argv[1]
    text = argv[2]

    lines = count_lines(fname)
    line_no = choose_line(lines, fname)
    insert_text(fname, text, line_no)
