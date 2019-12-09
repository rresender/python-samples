import re

def extract_color(line):
    for m in re.finditer(r"(.*?)#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})", line, re.S):
        g1 = m.group(0)
        g2 = str('#')+m.group(2)
        if g1 != g2:
            print(g2)

def process_css(css):
    lines = css.split('\n')
    for s in lines:
        extract_color(s)

# lines = int(input())
# for line in range(lines):
#     process_css(input())

t1= """
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
    background: -webkit-linear-gradient(top, #f9f9f9, #fff);
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}   
"""
t2 =  """
#BED
{
    color: #FfFdF8; background-color:#aef;
    font-size: 123px;
}
#Cab
{
    background-color: #ABC;
    border: 2px dashed #fff;
}
"""
process_css(t1)
process_css(t2)



    
    