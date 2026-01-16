<div align="center">
  <p>
      <img width="1792" height="310" alt="Data PreProcessing banner Nextits" src="https://github.com/user-attachments/assets/9b3a903e-0eec-44f8-ab44-3c2f93c47beb" />
  </p>

[English](../README.md) | 한국어 | [简体中文](./README_zh.md)

<!-- icon -->
![python](https://img.shields.io/badge/python-3.11~3.12-aff.svg)
![os](https://img.shields.io/badge/os-linux%2C%20win%2C%20mac-pink.svg)
[![License](https://img.shields.io/badge/license-Apache_2.0-green)](../LICENSE)



**Nextits Function은 문서 요약, 마인드맵 생성, 지능형 검색 기능을 제공하는 통합 AI 기능 시스템입니다**

</div>

# Nextits Function
[![Framework](https://img.shields.io/badge/Python-3.11+-blue)](#)
[![AI](https://img.shields.io/badge/AI-SGLang-orange)](#)
[![Features](https://img.shields.io/badge/Features-Summarizer%20%7C%20Mindmap%20%7C%20Search-green)](#)

> [!TIP]
> Nextits Function은 문서 처리, 지식 시각화, 지능형 정보 검색을 위한 강력한 AI 기반 기능을 제공합니다.
>
> 문서 요약, 마인드맵 생성, 요약이 포함된 웹 검색을 효율적으로 처리합니다.


**Nextits Function**은 **지능형 문서 처리 및 지식 관리** 기능을 제공하는 종합 AI 기능 시스템입니다. 요약, 시각화, 검색을 위한 세 가지 핵심 모듈을 제공합니다.

### 핵심 기능

- **문서 요약기 (md_summarizer/)**  
  SGLang 기반 문서 요약 시스템으로 FastAPI 서버, 마크다운 파싱, 계층적 요약을 지원합니다.

- **마인드맵 생성기 (mindmap/)**  
  이모지 지원, 세그먼트 처리, 지식 관리를 위한 Weaviate 통합을 통한 문서 자동 마인드맵 생성.

- **지능형 검색 (search/)**  
  Google Search API, 웹 크롤링(Wikipedia, Namuwiki, Nate News), AI 기반 요약이 통합된 검색 파이프라인.

## 📣 최근 업데이트

### 2026.01: AI 기능 시스템 공개

- **문서 요약기**:
  - SGLang 기반 고성능 추론
  - 마크다운 문서 파싱 및 청킹
  - 계층적 요약 생성
  - 비동기 지원 FastAPI 서버

- **마인드맵 생성기**:
  - 자동 마인드맵 구조 생성
  - 이모지 강화 시각화
  - 문서 세그먼트 처리
  - Weaviate 벡터 데이터베이스 통합

- **지능형 검색**:
  - Google Custom Search 통합
  - 다중 소스 웹 크롤링
  - AI 기반 콘텐츠 요약
  - 중복 필터링 및 결과 순위 지정

## 🚀 빠른 시작

### 설치

```bash
# 저장소 클론
git clone https://github.com/hnextits/NextitsLM_Function.git
cd NextitsLM_Function

# 각 모듈의 의존성 설치
cd md_summarizer
pip install -r requirements.txt

cd ../mindmap
pip install -r requirements.txt

cd ../search
pip install -r requirements.txt
```

### 문서 요약기 사용법

```bash
# SGLang 서버 시작
cd md_summarizer/scripts
./start_sglang_single.sh

# API 서버 실행
cd ../src
python api_server.py

# 예제 실행
python examples/usage_example.py
```

### 마인드맵 생성기 사용법

```python
from mindmap.mindmap_generator import MindmapGenerator

# 생성기 초기화
generator = MindmapGenerator()

# 문서에서 마인드맵 생성
mindmap = await generator.generate_mindmap(document_text)
```

### 검색 파이프라인 사용법

```python
from search.pipeline import search_and_summarize

# 검색 및 요약
results = search_and_summarize(
    query="검색 쿼리",
    num_results=10
)
```

## 📦 모듈 구조

```
skill/
├── md_summarizer/          # 문서 요약 모듈
│   ├── src/
│   │   ├── api_server.py   # FastAPI 서버
│   │   ├── sglang_client.py # SGLang 클라이언트
│   │   ├── md_parser.py    # 마크다운 파서
│   │   └── summary_index.py # 요약 인덱싱
│   ├── scripts/            # 서버 관리 스크립트
│   ├── config/             # 설정 파일
│   └── tests/              # 단위 테스트
│
├── mindmap/                # 마인드맵 생성 모듈
│   ├── mindmap_generator.py # 메인 생성기
│   ├── segment_processor.py # 문서 세그먼트 처리
│   ├── weaviate_service.py  # 벡터 DB 서비스
│   └── config.py           # 설정
│
└── search/                 # 검색 파이프라인 모듈
    ├── pipeline.py         # 메인 검색 파이프라인
    ├── google_search.py    # Google Search 클라이언트
    ├── summarizer.py       # 콘텐츠 요약기
    ├── util.py             # 유틸리티 함수
    └── crawler/            # 웹 크롤러
        ├── wikipedia.py
        ├── namuwiki.py
        └── natenews.py
```

## 🔧 설정

### 문서 요약기

`md_summarizer/config/model_config.yaml` 편집:

```yaml
model:
  name: "Model"
  max_tokens: 
  temperature: 

server:
  host: "0.0.0.0"
  port: 8000
```

### 마인드맵 생성기

`mindmap/config.py` 편집:

```python
class Config:
    WEAVIATE_URL = "http://localhost:8080"
    MODEL_NAME = "Model"
    MAX_SEGMENTS = 50
```

### 검색 파이프라인

환경 변수 설정 또는 설정 편집:

```bash
export GOOGLE_API_KEY="your_api_key"
export GOOGLE_CX_ID="your_cx_id"
```

## 🎯 주요 기능

### 문서 요약기
- **고성능 추론**: SGLang 기반 효율적인 모델 서빙
- **계층적 요약**: 다단계 문서 요약
- **비동기 처리**: async/await 지원 FastAPI
- **유연한 파싱**: 마크다운 문서 구조 분석

### 마인드맵 생성기
- **자동 구조화**: AI 기반 마인드맵 구조 생성
- **시각적 강화**: 이모지 기반 노드 장식
- **지식 관리**: Weaviate 벡터 데이터베이스 통합
- **세그먼트 처리**: 지능형 문서 청킹

### 지능형 검색
- **다중 소스 크롤링**: Wikipedia, Namuwiki, Nate News 지원
- **스마트 필터링**: 중복 제거 및 관련성 순위 지정
- **AI 요약**: 자동 콘텐츠 요약
- **설정 가능한 파이프라인**: 유연한 검색 및 처리 워크플로우

## 📊 성능

- **요약기**: 10K 토큰을 약 2초에 처리
- **마인드맵**: 복잡한 마인드맵을 약 5초에 생성
- **검색**: 10개 결과를 약 10초에 검색 및 요약

## 🧪 테스트

```bash
# 문서 요약기 테스트
cd md_summarizer
pytest tests/

# 마인드맵 생성기 테스트
cd mindmap
python -m pytest

# 검색 파이프라인 테스트
cd search
python -m pytest
```

## 🛠️ 개발

### 요구사항

- Python 3.11 이상
- CUDA 11.0 이상 (GPU 사용 시)
- 충분한 메모리 (최소 16GB 권장)

### 개발 환경 설정

```bash
# 가상 환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 개발 의존성 설치
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## 📝 라이선스

이 프로젝트는 Apache 2.0 라이선스 하에 배포됩니다. 자세한 내용은 [LICENSE](../LICENSE) 파일을 참조하세요.

## 🙏 감사의 말

이 프로젝트는 다음 오픈소스 프로젝트들의 도움을 받았습니다:

- **[SGLang](https://github.com/sgl-project/sglang)**: 고성능 LLM 서빙 프레임워크
- **[Weaviate](https://github.com/weaviate/weaviate)**: 지식 관리를 위한 벡터 데이터베이스

## 🎓 Citation

이 프로젝트를 연구에 사용하시는 경우, 다음 논문들을 인용해주세요:

### SGLang
```bibtex
@misc{zheng2023sglang,
  title={SGLang: Efficient Execution of Structured Language Model Programs},
  author={Lianmin Zheng and Liangsheng Yin and Zhiqiang Xie and Jeff Huang and Chuyue Sun and Cody Hao Yu and Shiyi Cao and Christos Kozyrakis and Ion Stoica and Joseph E. Gonzalez and Clark Barrett and Ying Sheng},
  year={2023},
  url={https://github.com/sgl-project/sglang}
}
```

## 🌐 데모 사이트

시스템을 직접 사용해보세요: [https://quantuss.hnextits.com/](https://quantuss.hnextits.com/)

## 👥 기여자

이 프로젝트는 다음 팀원들이 개발했습니다:

- **Lim** - [junseung_lim@hnextits.com](mailto:junseung_lim@hnextits.com)
- **Jeong** - [jeongnext@hnextits.com](mailto:jeongnext@hnextits.com)
- **Ryu** - [fbgjungits@hnextits.com](mailto:fbgjungits@hnextits.com)

## 📧 문의

프로젝트에 대한 문의사항이나 제안사항이 있으시면 이슈를 등록해주세요.

## 🌟 기여

기여를 환영합니다! Pull Request를 보내주시거나 이슈를 등록해주세요.

---

<div align="center">
Made with 🩸💦😭 by Nextits Team
</div>
