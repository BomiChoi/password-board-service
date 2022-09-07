# Password Board Service

원티드 프리온보딩 백엔드 기업 과제

## 목차

1. [프로젝트 개요](#프로젝트-개요)
2. [프로젝트 기술 스택](#프로젝트-기술-스택)
3. [개발 기간](#개발-기간)
4. [팀 구성](#팀-구성)
5. [역할](#역할)
6. [ERD](#ERD)
7. [API 목록](#API-목록)
8. [프로젝트 시작 방법](#프로젝트-시작-방법)

<br>

## 프로젝트 개요

비밀번호로 인증하는 게시판 기능을 제공하는 Django 기반 API 서버입니다.

<br>

## 과제 요구사항 분석

### 1. 게시글 올리기 (Create)

- 제목과 본문에 이모지 포함 가능 → utf8mb4로 설정
- 비밀번호: 6자 이상, 숫자 1개 이상 반드시 포함 → bcrypt로 암호화
    - 입력한 비밀번호가 조건에 부합하지 않는 경우 ValidationError 반환
- (선택) 현재 날씨 : Real-time Weather API([https://www.weatherapi.com/](https://www.weatherapi.com/)) 사용
    - 게시글 작성 시 자동으로 데이터베이스에 추가 → DRF GenericView의 perform_create 메소드 오버라이드

### 2. 게시글 수정 및 삭제 (Update/Delete)

- 비밀번호가 일치하지 않는 경우 PermissionDenied 반환
- Delete의 경우 DRF GenericView의 destroy 메소드를 오버라이드하여 구현

### 3. 게시글 목록 보기 (Read)

- 최신 글 순서로 정렬 → created_at 필드 기준으로 Ordering
- (선택) 스크롤 시 추가 로드(20개씩) → LimitOffsetPagination 적용

<br>

## 프로젝트 기술 스택

### Backend

<section>
<img src="https://img.shields.io/badge/Django-092E20?logo=Django&logoColor=white"/>
<img src="https://img.shields.io/badge/Django%20REST%20Framework-092E20?logo=Django&logoColor=white"/>
</section>

### DB

<section>
<img src="https://img.shields.io/badge/MySQL-4479A1?logo=MySQL&logoColor=white"/>
</section>

### Tools

<section>
<img src="https://img.shields.io/badge/GitHub-181717?logo=GitHub&logoColor=white"/>
<img src="https://img.shields.io/badge/Postman-FF6C37?logo=Postman&logoColor=white">
<img src="https://img.shields.io/badge/Swagger-85EA2D?logo=swagger&logoColor=black">
</section>



<br>

## 개발 기간

- 2022/09/06~2022/09/07

<br>

## 팀 구성

개인 프로젝트

<br>

## 역할

1. 요구사항 분석
2. 모델 및 API 설계
3. API 구현
4. 프로젝트 문서 작성

<br>

## ERD

![](../../../Desktop/스크린샷 2022-09-07 오후 1.55.52.png)

<br>

## API 목록

https://documenter.getpostman.com/view/17766148/VVBQXUJs

<br>

## 프로젝트 시작 방법

1. 로컬에서 실행할 경우

```bash
# 프로젝트 clone(로컬로 내려받기)
git clone -b develop --single-branch ${github 주소}
cd ${디렉터리 명}

# 가상환경 설정
python -m venv ${가상환경명}
source ${가상환경명}/bin/activate
# window (2 ways) 
# 1> ${가상환경명}/Scripts/activate
# 2> activate

# 라이브러리 설치
pip install -r requirements.txt
# 실행
python manage.py runserver
```

<br>
