from PIL import Image, ImageFont, ImageDraw

def bigger_text(big,small,text_size=12):

    font = ImageFont.truetype('arialbd.ttf', text_size) #load the font
    size = font.getsize(big)  #calc the size of text in pixels
    image = Image.new('1', size, 1)  #create a b/w image
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), big, font=font) #render the text to the bitmap
    lines =[]
    for rownum in range(size[1]): 
    #scan the bitmap:
    # print ' ' for black pixel and 
    # print '#' for white one
        line = []
        for colnum in range(size[0]):
            if image.getpixel((colnum, rownum)): line.append(' '),
            else: line.append(small),
        im_line = ''.join(line)
        lines += [im_line]
        # break
    return lines

def con_cat(c1,c2):

    return map(lambda x,y:x + ' '*5 + y,c1,c2)



def play_bigger_text(big,small,text_size=12):

    if type(big) == type([]) and type(small) == type([]) :
        list_ = map(lambda x,y: bigger_text(x,y),big,small)
        print list_
        lines = reduce(con_cat,list_)
        for item in lines:
            print item

    elif type(big) == type('') and type(small) == type(''):
        lines = bigger_text(big,small,text_size=12)
        for item in lines:
            print item
    else:
        print '*_*'


# big = 'Python'
# small = 'L'
# lines1 = bigger_text(big,small)

# big = 'Pil'
# small = 'U'
# lines2 = bigger_text(big,small)
# lines = map(lambda x,y:x + ' '*5 + y,lines1,lines2)


# for item in lines:
#     print item
if __name__ =='__main__':
    big = ['H I','L U','M E I']
    small = ['R','U','N']
    play_bigger_text(big,small)