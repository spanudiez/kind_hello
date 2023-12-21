# ansible_test



```console

[root@localhost hello]# curl http://192.168.64.138:31157
<html>
<head>
    <title>Yo</title>
</head>
<body>
    <h1>Hello, ca va?</h1>
</body>
</html>
[root@localhost hello]# ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: ens33: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:18:bd:51 brd ff:ff:ff:ff:ff:ff
    inet 192.168.64.139/24 brd 192.168.64.255 scope global noprefixroute dynamic ens33
       valid_lft 1637sec preferred_lft 1637sec
    inet6 fe80::26ca:b88d:1fda:caf2/64 scope link noprefixroute
       valid_lft forever preferred_lft forever
3: virbr0: <BROADCAST,MULTICAST> mtu 1500 qdisc noqueue state DOWN group default qlen 1000
    link/ether 52:54:00:e3:88:e8 brd ff:ff:ff:ff:ff:ff
4: virbr0-nic: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master virbr0 state DOWN group default qlen 1000
    link/ether 52:54:00:e3:88:e8 brd ff:ff:ff:ff:ff:ff
5: docker0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN group default
    link/ether 02:42:1d:46:4d:e6 brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.1/16 scope global docker0
       valid_lft forever preferred_lft forever
[root@localhost hello]#

```
