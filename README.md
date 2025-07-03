# na_auto_foward_bot

## 소개

**na_auto_foward_bot**은 Telegram 채널의 모든 메시지를 지정한 Telegram 그룹(또는 채팅방)으로 자동 포워딩해주는 텔레그램 봇입니다.

## 주요 특징

- 채널의 메시지를 실시간으로 특정 그룹 또는 채팅방에 전달
- 간단한 환경 변수 설정(.env 파일)
- python-telegram-bot 라이브러리를 사용한 비동기 처리

## 사용 방법

### 1. 저장소 클론

```bash
git clone [YOUR_REPO_URL]
cd na_auto_foward_bot
```

### 2. 환경 변수 설정

- **copy.env** 파일을 **.env**로 이름을 바꾼 후 원하는 값으로 채워주세요.

copy.env (예시)
```
BOT_TOKEN= 여러분의_텔레그램_봇_토큰
CHANNEL_ID= 모니터링_할_채널_ID
TARGET_GROUP_ID= 포워드할_타깃_그룹_or_채팅룸_ID
```

- `CHANNEL_ID`와 `TARGET_GROUP_ID`는 각각 정수형(Chat ID)이어야 하며, 마이너스(-)가 붙는 경우도 있습니다.

### 3. 패키지 설치

아래 명령어로 필요한 패키지를 설치하세요:

```bash
pip install -r requirements.in
```

### 4. 봇 실행

```bash
python na_auto_foward_bot.py
```

## 주의 사항

- 채널, 그룹(혹은 개인 채팅)의 ID를 정확하게 입력해야 합니다.
- 봇이 채널, 그룹 내에서 관리자 권한이 있어야 메시지를 전달할 수 있습니다.

---

# na_auto_foward_bot (English)

## Introduction

**na_auto_foward_bot** is a Telegram bot that automatically forwards all messages from a specified channel to a Telegram group (or chat).

## Features

- Real-time message forwarding from a Telegram channel to a target group or chat
- Simple environment variable setup using a .env file
- Asynchronous implementation with python-telegram-bot

## How to Use

### 1. Clone the repository

```bash
git clone [YOUR_REPO_URL]
cd na_auto_foward_bot
```

### 2. Set Environment Variables

- Rename **copy.env** to **.env** and fill in your information.

copy.env (Example)
```
BOT_TOKEN= your_bot_token
CHANNEL_ID= channel_id_to_monitor
TARGET_GROUP_ID= target_group_or_chat_id
```

- Both `CHANNEL_ID` and `TARGET_GROUP_ID` must be integer Chat IDs. They may start with a minus sign (-).

### 3. Install Requirements

Install required packages via:

```bash
pip install -r requirements.in
```

### 4. Run the Bot

```bash
python na_auto_foward_bot.py
```

## Notes

- Be sure to use the correct channel and group (or chat) IDs.
- The bot needs sufficient permissions in both the channel and the target group to forward messages.