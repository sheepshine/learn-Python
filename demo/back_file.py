import os
import time
source=['source/']
target_dir='backup/'
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'
print(target)
zip_command="zip -qr'%s' %s" % (target,''.join(source))
#zip_command=zipfile.ZipFile(zipName,'w',zipfile.ZIP._DEFLATED)

if os.system(zip_command)==0:
	print('成功备份',target)
else:
	print('备份失败')