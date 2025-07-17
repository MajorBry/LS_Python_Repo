import c4_5_mod1, c4_5_mod2, os

print(__name__)
print(__file__)
print(os.path.abspath(__file__))
assets = os.path.abspath(f'{__file__}/../assets')
print(assets)
image = f'{assets}/foo.png'
print(image)
