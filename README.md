#### HTTP接口项目

[接口文档地址]: https://www.showdoc.cc/carpediem915?page_id=4166555219832737

##### 一、环境准备：

1. Springboot2.x
2. JDK 1.8或以上版本 (1.8.0_181)
3. Maven 3.2或以上版本（3.6.1）
4. MySQL 5.7
5. IntelliJ IDEA

#### 二、实现步骤
1. 创建maven项目
2. HTTP接口实现（GET、POST）
3. Maven打包生成jar包
```
cd workspace/Java/JmeterDemo
mvn package
java -jar spring-boot-0.0.1-SNAPSHOT.jar
```
4.项目部署
```
# 拉取Java 8,也可以不提前瞎子啊，运行容器的时候会自动下载
docker pull java:8
通过filezilla上传jar包到虚拟机
# 移动jar包位置
mv spring-boot-0.0.1-SNAPSHOT.jar ~/docker-files/
cd docker-files/
# 创建并编写dockerfile文件
vim springboot_dockerfile

    FROM java:8
    MAINTAINER hcm<630134082@qq.com>
    ADD spring-boot-0.0.1-SNAPSHOT.jar webapp.jar
    CMD java -jar webapp.jar

# 构建webapp镜像
docker build -f ./springboot_dockerfile -t webapp .
# 通过镜像运行容器
docker run -id  -p 9000:8888 webapp
```

#### 接口自动化测试

一、环境准备：

1. Python 3.7
2. Requests 2.22.0

#### 接口性能测试