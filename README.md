# Wuhan 2019-nCov Spider
 Wuhan 2019-nCov Spider 数据简单爬取以及在linux上实行每隔一段时间运行,使用Beautifulsoup爬取数据

## Requirement

### bs4安装

```shell
 conda install -c vfonov bs4 
```

链接 https://anaconda.org/vfonov/bs4 

## 在linux上定时执行使用crontab指令

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

## 2020年2月20日更新

因为原网页也进行了更新，最终显示效果应该是这样的

> 数据来源：https://3g.dxy.cn/newh5/view/pneumonia 当前时间：2020-02-20 15:30:40
> 确诊人数：74677   疑似人数：4922   治愈人数：16285   死亡人数：2121   累计确诊人数增加：401

另外在把爬虫传到了新服务器时，发现了一些问题，使用crontab定时执行python文件的时候，运行不成功。从网上查资料发现 **crontab 执行的所有路径都必须是绝对路径** 

所以要么把python加入到环境变量要么写绝对路径

1. 写绝对路径

   ```
   #每分钟执行一次
   * * * * * /root/miniconda3/bin/python3.7  /home/covid-19/get_2019-nCov_data.py
   #每天12点执行一次
   0 12 * * * /root/miniconda3/bin/python3.7  /home/covid-19/get_2019-nCov_data.py
   
   ```

2. 添加PYTHONPATH

   ```
   这个方法弄好再写
   
   ```

   