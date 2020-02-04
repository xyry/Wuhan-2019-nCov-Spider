# Wuhan 2019-nCov Spider
 Wuhan 2019-nCov Spider 数据简单爬取以及在linux上实行每隔一段时间运行

使用Beautifulsoup爬取数据

在linux上定时执行使用crontab指令

- 命令为

```shell
*/60 * * * * python3 文件地址/get_2019-nCov_data.py

```

- 定时任务的写法

每五分钟执行 */5 * * * *

每小时执行   0 * * * *

每2小时执行   0 */2 * * *

每天执行    0 0 * * *

每周执行    0 0 * * 0

每月执行    0 0 1 * *

每年执行    0 0 1 1 *

这种写法应该是正确的

每小时Wuhan_2019-nCoV.txt 就会多一条记录，如下所示

> 数据来源：https://3g.dxy.cn/newh5/view/pneumonia 当前时间：2020-01-31 13:00:01
> 确诊人数：9720   疑似人数：15238   治愈人数：176   死亡人数：213
>
> 数据来源：https://3g.dxy.cn/newh5/view/pneumonia 当前时间：2020-01-31 14:00:02
> 确诊人数：9731   疑似人数：15238   治愈人数：176   死亡人数：213
>
> 数据来源：https://3g.dxy.cn/newh5/view/pneumonia 当前时间：2020-01-31 15:00:01
> 确诊人数：9731   疑似人数：15238   治愈人数：176   死亡人数：213