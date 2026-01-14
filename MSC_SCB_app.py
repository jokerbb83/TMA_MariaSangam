# -*- coding: utf-8 -*-
"""MSC_SCB_app (스코어보드)

- 관리자 앱(공통 로직)이 있는 파일을 그대로 실행하되,
  MSC_APP_MODE=scoreboard 로 고정해서 3개 탭(경기기록/월별/개인별)만 보이게 합니다.
- 관리자 앱 파일을 수정하면, 이 스코어보드 앱에도 자동 반영됩니다.

※ 주의: 이 파일에는 Streamlit 호출을 두지 말아야 합니다.
       (set_page_config 등은 '관리자 앱 파일' 안에서 가장 먼저 실행되도록 유지)
"""

import os
import runpy
from pathlib import Path

# =========================================================
# ✅ 스코어보드(일반회원용) 설정 - 여기만 바꾸면 됨
# =========================================================
# - 세션 파일(sessions.json) 완전 읽기 전용 (어떤 경우에도 저장/삭제 금지)
# - 스코어보드 전용 타이틀/컬러/푸터
SCB_TITLE = ""  # 예: "마리아상암포바 스코어보드 (Beta)"  (빈칸이면 자동: "<동호회명> 스코어보드")
SCB_BRAND_COLOR = "#3b82f6"         # 메인 컬러(블루)
SCB_BRAND_COLOR_HOVER = "#2563eb"   # hover 컬러
SCB_SECTION_GRAD_END = "#eff6ff"    # 섹션 카드 그라데이션 끝 컬러
SCB_FOOTER_HTML = (
    '<div style="margin: 26px 0 10px; text-align:center; color:#9ca3af; font-size:0.82rem;">'
    "Scoreboard (Read-only) · Powered by Studioroom"
    "</div>"
)

# ✅ 스코어보드 모드로 고정 + 세션 저장 막기(읽기전용)
os.environ["MSC_APP_MODE"] = "scoreboard"
os.environ["MSC_SESSIONS_READONLY"] = "1"

# ✅ 스코어보드 전용 브랜딩(관리자 앱이 env를 읽어서 적용)
if SCB_TITLE.strip():
    os.environ["MSC_SCB_TITLE"] = SCB_TITLE.strip()
os.environ["MSC_SCB_BRAND_COLOR"] = SCB_BRAND_COLOR.strip()
os.environ["MSC_SCB_BRAND_COLOR_HOVER"] = SCB_BRAND_COLOR_HOVER.strip()
os.environ["MSC_SCB_SECTION_GRAD_END"] = SCB_SECTION_GRAD_END.strip()
os.environ["MSC_SCB_FOOTER_HTML"] = SCB_FOOTER_HTML

HERE = Path(__file__).resolve().parent

# ✅ 연결 대상(관리자 앱) 후보들
CANDIDATES = [
    "MSC_app_admin_linked_v2.py",     # ✅ 최신 연동용 관리자 앱
    "MSC_app_admin_linked.py",        # (구버전)
    "MSC_app.py",
    "MSC_app - 복사본 (9).py",
]

target = None
for name in CANDIDATES:
    p = HERE / name
    if p.exists():
        target = p
        break

if target is None:
    raise FileNotFoundError("연결할 관리자 앱 파일을 찾지 못했어. (MSC_app_admin_linked_v2.py / MSC_app_admin_linked.py / MSC_app.py / MSC_app - 복사본 (9).py 중 하나가 필요)")

# ✅ 관리자 앱을 그대로 실행 (수정사항 자동 반영)
runpy.run_path(str(target), run_name="__main__")
