# -*- coding: utf-8 -*-
"""MSC 옵저버(스코어보드) 전용 앱

✅ 이 파일은 관리자용 'MSC_app.py'를 import해서 실행합니다.
   따라서 MSC_app.py를 수정하면, 이 옵저버 앱도 자동으로 동일하게 반영됩니다.

사용법:
- 이 파일을 Streamlit에서 실행하면 '옵저버 모드'로 MSC_app.py가 렌더링됩니다.
"""

import os

os.environ["MSC_APP_MODE"] = "observer"

import MSC_app  # noqa: F401
