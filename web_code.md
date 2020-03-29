# web框架源码

## nginx
处理事件的核心函数, event模块里
处理socket读写事件和定时器事件
获取负载均衡锁，监听端口接受连接
调用epoll模块的ngx_epoll_process_events
然后处理超时事件和在延后队列里的所有事件
nginx大部分的工作量都在这里
ngx_process_events_and_timers(cycle);

取舍

uv_loop_alive(env->event_loop())

kubernetes入门
master/worker
controller/apiserver/etcd/sheduler
pod/deployment/service/daemonset
微服务架构，及微服务能解决的问题
对应微服务的语言生态，如JAVA、GO、Python等
基础的软件配置管理，如代码管理、CI/CD、版本管理
基础的生产维护管理，如变更管理、流程管理、监控、成本管理等
其它运维知识，如基础网络、中间件、运维工具等

kubernetes中service是核心，我们并不需要太多关心kubernetes里面是怎么工作的，我们只需要关心它给我们提供什么service。它需要拥有一个唯一的名字、以及ip:port来对外提供服务。提供service的是容器，为了保证service的高可用，提供service的容器不能只有一个，需要一组，这一组容器我们把它叫做pod。pod是kubernetes最基本的操作单元！

充满好奇心，接受新事物，不轻易下结论
踏踏实实学习，不急功近利
学习，分享，写作
有使命感，因为相信，所以看见
执行力强，耐得住寂寞，拼的是业余时间
懂世故，而不世故
会授权，团队精神
热爱生活，热爱读书，喜欢旅行

目标：精通某一学科或者技能？紧跟一些最新的趋势？
选择一到两个预期效果可以帮助设定目标，设定里程碑，3个月为宜
排除干扰，选择特定时间段来学习
终身学习本身就是一种成功，少一些功利性的学习
多读书 培训班 视频 直播 播客 电子书 论坛
多看高手的作品，空杯心态，谦虚
推翻自己，才能进步

云原生时代

217
1-云原生时代的在线教育DevOps之道

2-高质量完成应用容器化

3-快速交付云原生应用的3种发布策略详解

4-GitOps之应用安全发布模型实践

5-阿里云云原生DevSecOps实践

6-容器化应用痛点剖析：问题诊断、监控及运维

225
1-Apache Dubbo 2019年度总结与展望
1-Nacos权限控制初探,保障微服务安全
2-Spring Cloud Hoxton 新版本介绍 & 未来展望
3-Dubbo 2.7.6 新特性
4-接入 Sentinel 让 N 个 9 成为可能
6-Arthas 在线应用诊断实践

219
1-使用函数计算十分钟构建支付宝小程序的后端
2-如何借助 Serverless 技术降低闲置计算资源成本
3-基于函数计算实现 Serverless 自动化运维
4-Serverless 工作流适用场景及最佳实践
5-搭建基于 Serverless 的在线转换工具
6-快速开发一个分布式 Puppeteer 网页截图服务