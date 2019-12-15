
def generateREADME(__version__):
    with open('README.md', 'r', encoding='UTF-8') as fr:
        content = fr.readlines()
    new = content.copy()
    for idx, i in enumerate(content[:10]):
        if '[![image]'in i and 'Pypi' in i:
            version_line = i[:i.find('Pypi-')+5] \
            + __version__ \
            + i[i.find('-green.svg'):]
            new[idx] = version_line

    with open('README.md', 'w', encoding='UTF-8') as fo:
        fo.write(''.join(new))
    with open('docs/README.md', 'w', encoding='UTF-8') as fo:
        fo.write(''.join(new))

if __name__ == "__main__":
    generateREADME('0.0.7.2.5')