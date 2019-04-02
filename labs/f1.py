fpl = 2.25
laps = 45
cont = 50
qlap = 80.45
pen = 0.35

tot = (fpl * laps) * ((100 + cont) / 100)
print('Starting fuel: ' + str(tot) + ' kg')

rfuel = tot - 5
tflap = qlap + ((rfuel / 10) * 0.35)
print('First lap: ' + str(tflap) + ' seconds')
