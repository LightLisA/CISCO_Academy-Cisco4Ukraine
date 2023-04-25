def outer(par):
    loc = par

    def inner():
        return loc

    return inner


var = 1
fun = outer(var)
print(fun())


################################################################################
def make_closure(par):
    loc = par

    def power(p):
        return p ** loc

    return power


fsqr = make_closure(2)
fcub = make_closure(3)

for i in range(5):
    print(i, fsqr(i), fcub(i))


################################################################################
def replace_spaces(replacement='*'):
    def new_replacement(text):
        return text.replace(' ', replacement)

    return new_replacement


stars = replace_spaces()
print(stars("And Now for Something Completely Different"))


################################################################################
def tag(tg):
    tg2 = tg
    tg2 = tg[0] + '/' + tg[1:]

    def inner(str):
        return tg + str + tg2

    return inner


b_tag = tag('<b>')
print(b_tag('Monty Python'))

################################################################################
