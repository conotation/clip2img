# ClipToImage
- 클립보드에 있는 이미지를 바탕 화면에 파일로 생성

#### 최초 생성
PIL 라이브러리 다운로드
```bash
pip install Image
```
#### Export
EXE 변환 라이브러리 설치
```bash
pip install pyinstaller
```
EXE 변환
```bash
pyinstaller --onefile --noconsole fileName.py
# --noconsole 옵션 : 콘솔창이 나타나지않는 옵션
# --onefile 옵션 : 외부 라이브러리 압축
```
##### 이미지 저장 경로
 \- 바탕화면 -> C2I 폴더에 저장