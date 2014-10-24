def get_points(file_name):
    f = open(file_name)
    lines = f.readlines()
    f.close()
    points = [[float(i) for i in line.strip().split()] for line in lines]
    return points
    
def get_lines(alf_file_name):
    f = open(alf_file_name)
    lines = f.readlines()[1:]
    f.close()
    pt2pt = [[int(i) for i in line.strip().split()] for line in lines]
    return pt2pt
    
def same_pt(a,b):
    if a[0] in b or a[1] in b:
        return True
        
def get_bd(segmt):
    bd = []
    bd.append(segmt.pop())
    has_next =True
    
    while(has_next):
        bd_len = len(bd)
        last_seg = bd[-1]
        last_pt = last_seg[1]
        for i in segmt:
            if last_pt == i[0]:
                bd.append(i[:])
                segmt.remove(i)
                break
            else:
                if last_pt == i[1]:
                    bd.append([i[1],i[0]])
                    segmt.remove(i)
                    break
        if bd_len == len(bd):
            has_next = False
    return bd
                
def test():
    pts = get_points("xy.txt")
    segmt = get_lines("xy.txt-alf")
    bd = get_bd(segmt)
    f = open("bd_points","w")
    for k in bd:
        pt = pts[k[0]]
        f.write(str(pt[0]) + "," + str(pt[1]) + "\n")
    f.close()
    
if __name__ == "__main__":
    test()