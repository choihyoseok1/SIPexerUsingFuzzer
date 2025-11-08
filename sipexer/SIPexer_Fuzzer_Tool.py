import subprocess

# --- 설정 ---

# 사용할 JSON 설정 파일명
config_file = "config.json"

# SIP 요청을 보낼 대상 주소 (예: "udp:127.0.0.1:5060" 또는 "udp:your-server-ip:5060")
target_address = "udp:127.0.0.1:5060"

# SIPexer 각 메시지 간 Timeout 시간 (응답 대기 시간, 응답 없을시 메시지 포기 후 다음 메시지로)
sipexer_timeout_ms = "32000"

# SIPexer 메시지의 T1 Timeout 시간 (재전송 대기 시간, 응답 없을 시 메시지 재전송)
sipexer_t1_timer_ms = "500" 

# 패킷 전송 개수 (각 패킷마다 랜덤값은 따로 설정됨)
rc_count = "1"

# 실행할 전체 명령어: ./sipexer -ff config.json -fe [target_address]
command = [ "./sipexer" , 
            "-ff", config_file, 
            "-fe", 
            "-timeout", sipexer_timeout_ms, 
            "-timer-t1", sipexer_t1_timer_ms,
            "-rc", rc_count, 
            target_address]
 
result = subprocess.run(command)
