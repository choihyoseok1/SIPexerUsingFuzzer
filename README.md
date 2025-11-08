# SIPexerUsingFuzzer

SIPexer를 이용한 Fuzzer입니다.

기본 Config.json 형식
```
{
"method": "INVITE",
"fuser": "ChoiHyoSeok",
"fdomain": "localhost",
"tuser": "CapstoneDesign",
"tdomain": "localhost",
"viabranch": "$uuid",
"rport": ";rport",
"fromtag": "$uuid",
"totag": "",
"callid": "$uuid",
"cseqnum": "$randseq",
"date": "$daterfc1123",
"sdpuser": "HelloIamSDP",
"sdpsessid": "$timestamp",
"sdpsessversion": "$timestamp",
"sdpaf": "IP4",
"sdprtpport": "30000",
"sdpafieldfuzz1": "",
"sdpafieldfuzz2": "",
"sdpafieldfuzz3": "$randstr(5)"
}
```

Json이 적용되는 Field 구조

SIP Part

```
{{.method}} {{.ruri}} SIP/2.0
Via: SIP/2.0/{{.viaproto}} {{.viaaddr}}{{.rport}};branch=z9hG4bKSG.{{.viabranch}}
From: {{if .fname}}"{{.fname}}" {{end}}<sip:{{if .fuser}}{{.fuser}}@{{end}}{{.fdomain}}>;tag={{.fromtag}}
To: {{if .tname}}"{{.tname}}" {{end}}<sip:{{if .tuser}}{{.tuser}}@{{end}}{{.tdomain}}>
Call-ID: {{.callid}}
CSeq: {{.cseqnum}} {{.method}}
{{if .subject}}Subject: {{.subject}}{{else}}$rmeol{{end}}
{{if .date}}Date: {{.date}}{{else}}$rmeol{{end}}
{{if .contacturi}}Contact: {{.contacturi}}{{if .contactparams}};{{.contactparams}}{{end}}{{else}}$rmeol{{end}}
{{if .expires}}Expires: {{.expires}}{{else}}$rmeol{{end}}
{{if .useragent}}User-Agent: {{.useragent}}{{else}}$rmeol{{end}}
Content-Length: 0
```

SDP Part

```
v=0{{.cr}}
o={{.sdpuser}} {{.sdpsessid}} {{.sdpsessversion}} IN {{.sdpaf}} {{.localip}}{{.cr}}
s=call{{.cr}}
c=IN {{.sdpaf}} {{.localip}}{{.cr}}
t=0 0{{.cr}}
m=audio {{.sdprtpport}} RTP 0 8 101{{.cr}}
a=rtpmap:0 pcmu/8000{{.sdpafieldfuzz1}}{{.cr}}
a=rtpmap:8 pcma/8000{{.sdpafieldfuzz2}}{{.cr}}
a=rtpmap:101 telephone-event/8000{{.sdpafieldfuzz3}}{{.cr}}
a=sendrecv{{.cr}}
```

SIPexer_Fuzzer_Tool.py에서 내부 설정 수정 가능

설정

사용할 JSON 설정 파일명
```config_file = "config.json"```

SIP 요청을 보낼 대상 주소 (예: "udp:127.0.0.1:5060")
```target_address = "udp:127.0.0.1:5060"```

SIPexer 각 메시지 간 Timeout 시간 (응답 대기 시간, 응답 없을시 메시지 포기 후 다음 메시지로)
```sipexer_timeout_ms = "32000"```

SIPexer 메시지의 T1 Timeout 시간 (재전송 대기 시간, 응답 없을 시 메시지 재전송)
```sipexer_t1_timer_ms = "500"```

패킷 전송 개수 (각 패킷마다 랜덤값은 따로 설정됨)
```rc_count = "10"```

```go.build .```
명령어 이후 실행

폴더 내의 python server mini_server.py를 통해 체크 가능함


