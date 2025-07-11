# AI 코드 버전 관리 가이드

## 워크플로우

### 1. 프로젝트 초기화
```bash
mkdir my-project
cd my-project
git init
git branch -m main
```

### 2. AI가 코드 생성 시 버전 관리 프로세스

#### Step 1: 코드 생성
AI가 새 기능을 구현하거나 코드를 생성할 때:
- 먼저 현재 상태를 확인 (`git status`)
- 변경사항 검토 (`git diff`)

#### Step 2: 의미있는 단위로 커밋
```bash
# 파일 추가
git add <파일명>

# 커밋 메시지는 변경 내용을 명확히 설명
git commit -m "feat: 사용자 인증 기능 추가

- JWT 토큰 기반 인증 구현
- 로그인/로그아웃 API 엔드포인트 추가
- 사용자 세션 관리 기능 포함

🤖 Generated with Claude Code"
```

#### Step 3: 브랜치 전략
```bash
# 새 기능 개발 시
git checkout -b feature/기능명

# 버그 수정 시
git checkout -b fix/버그설명

# 실험적 기능
git checkout -b experiment/실험명
```

### 3. 커밋 메시지 규칙

- `feat:` 새로운 기능 추가
- `fix:` 버그 수정
- `refactor:` 코드 리팩토링
- `docs:` 문서 수정
- `test:` 테스트 추가/수정
- `chore:` 빌드 프로세스 또는 보조 도구 변경

### 4. 버전 태그 관리
```bash
# 마일스톤 달성 시 태그 추가
git tag -a v1.0.0 -m "첫 번째 안정 버전"

# 태그 목록 확인
git tag -l
```

### 5. 변경 이력 확인
```bash
# 커밋 히스토리 보기
git log --oneline --graph

# 특정 파일의 변경 이력
git log -p 파일명
```

## AI 코드 생성 시 주의사항

1. **작은 단위로 커밋**: 한 번에 너무 많은 변경사항을 커밋하지 않기
2. **테스트 후 커밋**: 코드가 정상 작동하는지 확인 후 커밋
3. **의미있는 커밋 메시지**: 나중에 이해할 수 있도록 명확하게 작성
4. **브랜치 활용**: main 브랜치를 보호하고 기능별로 브랜치 생성

## 롤백 및 복구

```bash
# 마지막 커밋 취소 (변경사항은 유지)
git reset --soft HEAD~1

# 특정 커밋으로 되돌리기
git revert <커밋해시>

# 작업 중인 변경사항 임시 저장
git stash
git stash pop  # 복원
```