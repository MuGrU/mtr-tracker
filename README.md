# network-tracker
>Traceroute ISP information and location with API to http://ip-api.com

## Installation

Dependencies:

```sh
mtr packet
root access
```


## Motivation

My self-study to cover the lack of information about the ISP's to troubleshoot routing switching performance issues.
The mtr-tracker uses mtr package to ping and trace route internet hubs and AS in order to disclosure its location and Service Provider.
## Disclamer

*** EDUCATIONAL PURPOSE ONLY. ***

- This is an estimated GEO location based on APIs from Internet database.

```sh

 ##     ## ######## ########          ######## ########     ###     ######  ##    ## ######## ########  
 ###   ###    ##    ##     ##            ##    ##     ##   ## ##   ##    ## ##   ##  ##       ##     ## 
 #### ####    ##    ##     ##            ##    ##     ##  ##   ##  ##       ##  ##   ##       ##     ## 
 ## ### ##    ##    ########  #######    ##    ########  ##     ## ##       #####    ######   ########  
 ##     ##    ##    ##   ##              ##    ##   ##   ######### ##       ##  ##   ##       ##   ##   
 ##     ##    ##    ##    ##             ##    ##    ##  ##     ## ##    ## ##   ##  ##       ##    ##  
 ##     ##    ##    ##     ##            ##    ##     ## ##     ##  ######  ##    ## ######## ##     ##  
 _______________________________________________________________________________________________________
                                                                                                        

Tracing route to: www.github.com
It can take a while... Get some coffee :)

[WEB]: www.github.com
	[+] DNS Resolution: 0.023554
	[+] Connetion Time: 0.424796
	[+] Start Transfer: 1.146495
	[+] Total Time: 1.547805

 1.|-- GPT-2731GN2A4P.GPT-2731GN2A4P (192.168.15.1)
	[+] Loss%: [0.0] Snt: [10] Last: [0.51] Avg: [0.47] Best: [0.39] Wrst%: [0.57] StDev%: [0.07] 
	[ Private range or Reserved range ]

 3.|-- 187-100-166-108.dsl.telesp.net.br (187.100.166.108)
	[+] Loss%: [0.0] Snt: [10] Last: [3.14] Avg: [2.8] Best: [1.85] Wrst%: [4.46] StDev%: [0.77] 
	[+] Region: Sao Paulo
	[+] Country: Brazil
	[+] City: São Paulo
	[+] ISP: Vivo
	[+] Lat & Lon: -23.5505 -46.6333
	[+] Zipcode: 01000-000
	[+] AS: AS27699 TELEFÔNICA BRASIL S.A

 4.|-- 152-255-170-160.user.vivozap.com.br (152.255.170.160)
	[+] Loss%: [0.0] Snt: [10] Last: [1.94] Avg: [2.79] Best: [1.94] Wrst%: [5.08] StDev%: [0.92] 
	[+] Region: Espirito Santo
	[+] Country: Brazil
	[+] City: Cariacica
	[+] ISP: Vivo
	[+] Lat & Lon: -20.3495 -40.3999
	[+] Zipcode: 29140-000
	[+] AS: AS26599 TELEFÔNICA BRASIL S.A

 5.|-- 84.16.7.228 (84.16.7.228)
	[+] Loss%: [0.0] Snt: [10] Last: [5.07] Avg: [4.73] Best: [3.66] Wrst%: [5.59] StDev%: [0.66] 
	[+] Region: Virginia
	[+] Country: United States
	[+] City: Ashburn
	[+] ISP: Telefonica International Wholesale Network
	[+] Lat & Lon: 39.0438 -77.4874
	[+] Zipcode: 20149
	[+] AS: AS12956 TELEFONICA GLOBAL SOLUTIONS SL

 6.|-- 5.53.3.143 (5.53.3.143)
	[+] Loss%: [0.0] Snt: [10] Last: [115.67] Avg: [115.25] Best: [113.74] Wrst%: [119.67] StDev%: [1.89] 
	[+] Region: Madrid
	[+] Country: Spain
	[+] City: Madrid
	[+] ISP: Telefonica Global Solutions SL
	[+] Lat & Lon: 40.5156 -3.66234
	[+] Zipcode: 28050
	[+] AS: AS12956 TELEFONICA GLOBAL SOLUTIONS SL

 7.|-- 213.140.43.206 (213.140.43.206)
	[+] Loss%: [0.0] Snt: [10] Last: [118.77] Avg: [118.23] Best: [117.55] Wrst%: [119.51] StDev%: [0.7] 
	[+] Region: Madrid
	[+] Country: Spain
	[+] City: Madrid
	[+] ISP: Telefonica International Wholesale Network
	[+] Lat & Lon: 40.5149 -3.66524
	[+] Zipcode: 28760
	[+] AS: AS12956 TELEFONICA GLOBAL SOLUTIONS SL

 8.|-- 84.16.15.165 (84.16.15.165)
	[+] Loss%: [20.0] Snt: [10] Last: [135.67] Avg: [137.06] Best: [135.36] Wrst%: [140.59] StDev%: [1.95] 
	[+] Region: Madrid
	[+] Country: Spain
	[+] City: Madrid
	[+] ISP: Telefonica International Wholesale Network
	[+] Lat & Lon: 40.5156 -3.66234
	[+] Zipcode: 28050
	[+] AS: AS12956 TELEFONICA GLOBAL SOLUTIONS SL

 9.|-- ae-12.r04.miamfl02.us.bb.gin.ntt.net (129.250.9.85)
	[+] Loss%: [0.0] Snt: [10] Last: [118.3] Avg: [118.35] Best: [117.76] Wrst%: [119.62] StDev%: [0.56] 
	[+] Region: Florida
	[+] Country: United States
	[+] City: Miami
	[+] ISP: NTT America, Inc.
	[+] Lat & Lon: 25.7617 -80.1918
	[+] Zipcode: 33102
	[+] AS: AS2914 NTT America, Inc.

 10.|-- ae-3.r23.miamfl02.us.bb.gin.ntt.net (129.250.3.141)
	[+] Loss%: [0.0] Snt: [10] Last: [118.45] Avg: [118.35] Best: [117.59] Wrst%: [119.64] StDev%: [0.66] 
	[+] Region: Florida
	[+] Country: United States
	[+] City: Miami
	[+] ISP: NTT America, Inc.
	[+] Lat & Lon: 25.7617 -80.1918
	[+] Zipcode: 33102
	[+] AS: AS2914 NTT America, Inc.

 11.|-- ae-4.r24.asbnva02.us.bb.gin.ntt.net (129.250.2.86)
	[+] Loss%: [0.0] Snt: [10] Last: [152.62] Avg: [154.01] Best: [151.68] Wrst%: [158.64] StDev%: [2.38] 
	[+] Region: Virginia
	[+] Country: United States
	[+] City: Ashburn
	[+] ISP: NTT America, Inc.
	[+] Lat & Lon: 39.0438 -77.4874
	[+] Zipcode: 20149
	[+] AS: AS2914 NTT America, Inc.

 12.|-- ae-2.r05.asbnva02.us.bb.gin.ntt.net (129.250.2.22)
	[+] Loss%: [0.0] Snt: [10] Last: [136.42] Avg: [137.31] Best: [135.67] Wrst%: [143.63] StDev%: [2.32] 
	[+] Region: Virginia
	[+] Country: United States
	[+] City: Ashburn
	[+] ISP: NTT America, Inc.
	[+] Lat & Lon: 39.0438 -77.4874
	[+] Zipcode: 20149
	[+] AS: AS2914 NTT America, Inc.

 13.|-- ce-0-9-0-2.r05.asbnva02.us.ce.gin.ntt.net (129.250.194.78)
	[+] Loss%: [0.0] Snt: [10] Last: [139.9] Avg: [137.21] Best: [136.27] Wrst%: [139.9] StDev%: [1.03] 
	[+] Region: New Jersey
	[+] Country: United States
	[+] City: Jersey City
	[+] ISP: NTT America, Inc.
	[+] Lat & Lon: 40.7182 -74.0476
	[+] Zipcode: 07302
	[+] AS: AS2914 NTT America, Inc.

 17.|-- lb-140-82-113-4-iad.github.com (140.82.113.4)
	[+] Loss%: [0.0] Snt: [10] Last: [126.55] Avg: [126.38] Best: [125.42] Wrst%: [128.07] StDev%: [0.85] 
	[+] Region: California
	[+] Country: United States
	[+] City: San Francisco
	[+] ISP: GitHub, Inc.
	[+] Lat & Lon: 37.7823 -122.391
	[+] Zipcode: 94107
	[+] AS: AS36459 GitHub, Inc.


```

## Release History

* 1.0
    * Work in progress
      - Write analysis report, create graphs and plot map with location and possible bottlenecks
