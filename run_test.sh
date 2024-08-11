#!/bin/bash

# Test 폴더로 이동
cd ./Test

# "_test.py"로 끝나는 모든 파일에 대해 unittest 실행
for test_file in *_test.py
do
    if [ -f "$test_file" ]; then
        echo "테스트 실행 중: $test_file"
        python -m unittest -v "$test_file"
    fi
done

# 원래 디렉토리로 돌아가기
cd ..