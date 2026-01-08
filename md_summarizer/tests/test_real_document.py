"""
실제 문서 요약 테스트
"""

import sys, traceback
from pathlib import Path

# 프로젝트 루트 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src import SGLangClient, MDParser


def main():
    """실제 문서 요약 테스트"""
    print("\n" + "="*80)
    print("실제 문서 요약 테스트: 원가관리회계.md")
    print("="*80)
    
    # 클라이언트 초기화
    print("\n🔧 SGLang 클라이언트 초기화...")
    client = SGLangClient(endpoints=[
        "http://localhost:port",
        "http://localhost:port"
    ])
    client.timeout = 300.0  # 5분으로 증가 (긴 문서 처리용)
    
    parser = MDParser()
    
    # 문서 읽기
    doc_path = Path(__file__).parent / "sample_documents" / "원가관리회계.md"
    
    if not doc_path.exists():
        print(f"\n❌ 오류: 문서를 찾을 수 없습니다: {doc_path}")
        print("\n다음 경로에 문서를 배치하세요:")
        print(f"  {doc_path}")
        return
    
    print(f"\n📄 문서 읽기: {doc_path.name}")
    content = parser.read_file(str(doc_path))
    
    # 문서 정보
    print(f"\n📊 문서 정보:")
    print(f"   - 파일명: {doc_path.name}")
    print(f"   - 크기: {doc_path.stat().st_size:,} bytes")
    print(f"   - 문자 수: {len(content):,} 문자")
    print(f"   - 예상 토큰: ~{len(content)//4:,} tokens")
    
    # 헤더 추출
    headers = parser.extract_headers(content)
    print(f"   - 헤더 수: {len(headers)}개")
    
    if headers:
        print(f"\n📑 문서 구조 (상위 5개 헤더):")
        for i, header in enumerate(headers[:5], 1):
            indent = "  " * (header['level'] - 1)
            print(f"   {indent}{'#' * header['level']} {header['text']}")
    
    # 요약 생성
    print("\n" + "="*80)
    print("⏳ 요약 생성 중...")
    print("   - 예상 소요 시간: 30초 ~ 1분")
    print("   - 듀얼 GPU 사용: GPU 0, GPU 1")
    print("="*80)
    
    try:
        summary = client.generate_answer(content, max_tokens=8192)
        
        # 결과 출력
        print("\n" + "="*80)
        print("✅ 요약 생성 완료!")
        print("="*80)
        
        print("\n" + "="*80)
        print("📝 요약 결과")
        print("="*80)
        print()
        print(summary)
        print()
        print("="*80)
        
        # 통계
        print("\n📊 요약 통계:")
        print(f"   - 원본 길이: {len(content):,} 문자")
        print(f"   - 요약 길이: {len(summary):,} 문자")
        print(f"   - 압축률: {len(summary)/len(content)*100:.1f}%")
        print(f"   - 줄 수: {summary.count(chr(10)) + 1}줄")
        
        # 결과 저장
        output_dir = Path(__file__).parent.parent / "results"
        output_dir.mkdir(exist_ok=True)
        
        output_path = output_dir / f"summary_{doc_path.stem}_11회차.md"
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write(f"원본 문서: {doc_path.name}\n")
            f.write(f"생성 시간: {client.get_timestamp()}\n")
            f.write("="*80 + "\n\n")
            f.write(summary)
        
        print(f"\n💾 요약 결과 저장: {output_path}")
        
        print("\n" + "="*80)
        print("🎉 테스트 완료!")
        print("="*80)
        
    except Exception as e:
        print("\n" + "="*80)
        print("❌ 오류 발생!")
        print("="*80)
        print(f"\n오류 내용: {e}")
        print("\n해결 방법:")
        print("1. SGLang 서버가 실행 중인지 확인:")
        print("   bash scripts/start_sglang_dual.sh")
        print("\n2. 서버 상태 확인:")
        print("   curl http://localhost:30000/health")
        print("   curl http://localhost:30001/health")
        print("\n3. 로그 확인:")
        print("   tail -f logs/sglang_gpu0.log")
        print("   tail -f logs/sglang_gpu1.log")
        
        print("\n상세 오류:")
        traceback.print_exc()


if __name__ == "__main__":
    main()
