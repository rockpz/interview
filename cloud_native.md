# 云原生笔记

## 1 云原生简介

### 1.1 定义

低心智负担、敏捷的、以可扩展、可复制的方式最大化的利用云的能力、发挥云的价值的最佳路径
愿景是生在云上、长在云上、全新的软件开发、发布和运维模式

### 1.2 云原生的技术范畴

1. 云应用定义与开发流程
应用定义与镜像制作
CI/CD
消息和streaming
数据库

2. 云应用编排与管理
应用编排与调度
服务发现与治理
远程调用
API网关
Service Mesh

3. 监控与可观测性
监控
日志
Traceing
混沌工程

4. 云原生底层技术
容器运行时
云原生存储技术
云原生网络技术

5. 云原生工具集
流程自动化与配置管理
容器镜像仓库
云原生安全技术
云端密码管理

6. Serverless
Faas
Baas
Serverless计费

## 1.3 云原生思想的两个理论基础

不可变基础设施 容器镜像 自包含 可漂移
云应用编排理论 自描述，自运维 流程自动化 容易水平扩展 可快速复制的管控系统与支撑组件

## 1.4 云原生关键技术点

1. 自包含、可定制的应用镜像
2. 应用快速部署与隔离能力
3. 应用基础设施创建和销毁的自动化管理
4. 可复制的管控系统与支撑组件

## 1.5 课程拓扑图

1. 基础
容器基础知识
kubernetes基础知识
应用编排与管理
应用配置管理
应用存储与持久化数据卷
应用监控与可观测性
应用服务与网络

2. 进阶
容器技术进阶
kubernetes进阶
深入理解etcd
调度与资源管理
GPU与硬件加速器
API编程范式
kubernetes网络模型剖析
CNI与CNI网络插件
集群安装配置与验证
容器与集群安全
CRI与安全容器
多容器运行时

## 3 kubernetes核心概念

### 3.1 什么是kubernetes

自动化、工业级的容器编排平台
核心功能
服务发现与负载均衡
容器自动装箱
存储编排
自动容器恢复
自动发布与回滚
配置与密文管理
批量执行
水平伸缩

调度
异常自动恢复
负载水平伸缩

## 3.2 kubernetes架构

master
Apiserver
Controller
Scheduler
Etcd

node
Pod
kubelet
Container Runtime
Storage Plugin
Network Plugin
Kube-proxy

## 3.3 kubernetes核心概念

1. Pod
最小的调度以及资源单元
由一个或者多个容器组成
定义容器运行的方式(Command、环境变量等)
提供给容器共享的运行环境(网络、进程空间)

2. Volume
声明在Pod中的容器可访问的文件目录
可以被挂载在Pod中一个(或者多个)容器的指定路径下
支持多种后端存储的抽象(本地存储、分布式存储、云储存...)

3. Deployment
定义一组Pod的副本数目、版本等
通过控制器(Controller)维持Pod的数目(自动恢复失败的Pod)
通过控制器以指定的策略控制版本(滚动升级、重新生成、回滚等)

4. Service
提供访问一个或多个Pod实例的稳定访问地址
支持多种访问方式实现(ClusterIP、NodePort、LoadBalancer)

5. Namespaces
一个集群内部的逻辑隔离机制(鉴权、资源额度)
每个资源都属于一个Namespace
同一个Namespace中的资源命名唯一
不同Namespace中的资源可重名

### 3.4 kubernetes API基础知识

HTTP + JSON/YAML
kubectl
UI
curl

apiVersion: v1
kind: Pod
metadata:
 name: banana
 labels:
 color: yellow
spec:
 containers:
 - name: nginx
   image: nginx
   ports:
   - containerPort: 80

Label
一组Key:Value
可以被selector所查询(select color=red)
资源集合的默认表达形式(例如：service对应的一组Pod)

