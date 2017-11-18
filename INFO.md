
pip install --upgrade google-api-python-client

1. shiro反序列化的payload  ping -c 3|| ping -n 3 测试靶场环境时，失效。采用随机payload来避免。

目标:
1.插件例行运行起来   crontab
2.web端有记录每次运行开始时间、结束时间、总ip数，总域名数，已扫描数
3.所有报警都在web展示

shiro.py中的jar文件路径需要配置，类似这种场景可能需要集中化配置解决。


任务写到文件中可以更随机化