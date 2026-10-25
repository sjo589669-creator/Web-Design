# PLUG·IN — 브라우저를 입히는 법

중간고사 대체 과제 · 학번 2601981 조서형

패션 코디를 주제로, 브라우저 확장 프로그램을 '액세서리'에 비유한 패션 잡지 스타일 브로슈어(16쪽)입니다.
HTML5 시맨틱 태그와 CSS3만으로 조판한 뒤 PDF로 출력했습니다.

## 소주제
1. 플러그인이란 무엇인가
2. 나만의 필수 확장 프로그램 큐레이션
3. 확장 프로그램 설치 전 확인할 위험 신호

## 파일
| 파일 | 설명 |
|---|---|
| `index.html` | 브로슈어 전체 소스 (한 페이지 = `<section class="page">` 하나, 210×270mm) |
| `render_pdf.py` | Chromium(Playwright)으로 `index.html`을 PDF로 출력하는 스크립트 |

## 실행 방법
- 브라우저에서 `index.html`을 열면 바로 볼 수 있습니다. (인쇄 → PDF로 저장 시 배경 그래픽 켜기)
- PDF 출력: `python render_pdf.py index.html book.pdf`

## 사용한 수업 내용
- 시맨틱 태그(`header`, `nav`, `section`, `article`, `aside`, `footer`), 앵커와 id 링크
- 목록 태그, 테이블 `rowspan`, 입력 양식(`form`, `fieldset`, `legend`, `input`, `label`)
- 선택자(클래스·아이디·후손·자손·속성·구조 선택자, `::first-letter`)
- 박스·가시·위치(`relative`/`absolute`, `z-index`)·유동(`float`)·글자·그림자·그레이디언트 속성
