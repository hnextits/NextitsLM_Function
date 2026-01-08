"""
청크 기반 문서 요약 테스트
큰 문서를 여러 청크로 나눠서 요약합니다.
"""

import sys
from pathlib import Path
from src import SGLangClient, MDParser

# 프로젝트 루트 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))


def main():
    """청크 기반 문서 요약 테스트"""
    print("\n" + "="*80)
    print("청크 기반 문서 요약 테스트: 원가관리회계.md")
    print("="*80)
    
    # 클라이언트 초기화
    print("\n🔧 SGLang 클라이언트 초기화...")
    client = SGLangClient(endpoints=[
        "http://localhost:port",
        "http://localhost:port"
    ])
    client.timeout = 180.0  # 3분
    
    parser = MDParser()
    
    # 문서 읽기
    doc_path = Path(__file__).parent
    
    if not doc_path.exists():
        print(f"\n❌ 오류: 문서를 찾을 수 없습니다: {doc_path}")
        return
    
    print(f"\n📄 문서 읽기: {doc_path.name}")
    content = parser.read_file(str(doc_path))
    
    # 문서 정보
    print(f"\n📊 문서 정보:")
    print(f"   - 파일명: {doc_path.name}")
    print(f"   - 문자 수: {len(content):,} 문자")
    print(f"   - 예상 토큰: ~{len(content)//4:,} tokens")
    
    # 청크로 분할 (5,000 문자 = ~1,250 토큰, 안전하게 처리)
    chunk_size = 5000
    chunks = parser.chunk_text(content, chunk_size=chunk_size, overlap=200)
    
    print(f"\n📦 청크 분할:")
    print(f"   - 청크 크기: {chunk_size:,} 문자")
    print(f"   - 총 청크 수: {len(chunks)}개")
    
    # 각 청크 요약
    print("\n" + "="*80)
    print("⏳ 청크별 요약 생성 중...")
    print("="*80)
    
    summaries = []
    
    for i, chunk in enumerate(chunks, 1):
        print(f"\n[청크 {i}/{len(chunks)}] 요약 중... ({len(chunk):,} 문자)")
        
        try:
            # 간단한 프롬프트로 각 청크 요약
            simple_prompt = f"""
다음 텍스트를 단원별로 간결하게 요약하세요. 한국어로만 작성하세요.

# 입력 텍스트
{chunk}

# 작업
위 텍스트의 주요 단원과 핵심 내용을 요약하세요. 각 단원마다 2-3문장으로 정리하세요.
"""
            
            # 직접 API 호출 (간단한 프롬프트)
            endpoint = client._get_next_endpoint()
            summary = client._call_sglang(endpoint, simple_prompt, max_tokens=2000)
            
            summaries.append(f"## 청크 {i}\n\n{summary}")
            print(f"   ✅ 완료 ({len(summary)} 문자)")
            
        except Exception as e:
            print(f"   ❌ 오류: {e}")
            summaries.append(f"## 청크 {i}\n\n(요약 실패)")
    
    # 최종 결과 결합
    final_summary = "\n\n---\n\n".join(summaries)
    
    # 결과 출력
    print("\n" + "="*80)
    print("✅ 전체 요약 생성 완료!")
    print("="*80)
    
    print("\n" + "="*80)
    print("📝 요약 결과")
    print("="*80)
    print()
    print(final_summary)
    print()
    print("="*80)
    
    # 통계
    print(f"\n📊 요약 통계:")
    print(f"   - 원본 길이: {len(content):,} 문자")
    print(f"   - 요약 길이: {len(final_summary):,} 문자")
    print(f"   - 압축률: {len(final_summary)/len(content)*100:.1f}%")
    print(f"   - 청크 수: {len(chunks)}개")
    
    # 결과 저장
    output_dir = Path(__file__).parent.parent / "results"
    output_dir.mkdir(exist_ok=True)
    
    output_path = output_dir / f"summary_chunked_{doc_path.stem}.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("="*80 + "\n")
        f.write(f"원본 문서: {doc_path.name}\n")
        f.write(f"생성 시간: {client.get_timestamp()}\n")
        f.write(f"청크 수: {len(chunks)}개\n")
        f.write("="*80 + "\n\n")
        f.write(final_summary)
    
    print(f"\n💾 요약 결과 저장: {output_path}")
    
    print("\n" + "="*80)
    print("🎉 테스트 완료!")
    print("="*80)


if __name__ == "__main__":
    main()
