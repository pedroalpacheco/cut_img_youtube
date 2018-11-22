'''Extrai link de imagem inicial de video do youtube'''


def extraiImg(url):
    arrayvideo = url.split('v=')
    lkimage = 'https://i.ytimg.com/vi/' + arrayvideo[1] + '/hqdefault.jpg'
    print(lkimage)


extraiImg('https://www.youtube.com/watch?v=zab985qDgnU')