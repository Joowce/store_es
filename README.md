# elastic search CSV 파일 업로드

> 참고
> https://www.elastic.co/blog/indexing-csv-elasticsearch-ingest-node

공공데이터 중에서 [상가(상권)정보](https://www.data.go.kr/dataset/15012005/fileData.do) 파일데이터를 elastic search에 업로드

## 과정
1. csv 파일에서 한 줄씩 읽음
2. 해당 줄에 존재하는 **"** 을 **'** 로 변경
3. elastic-search 에 request를 보내기 위해서 elastic-search에
`{ store : read_line }`의 형태를 가진 document를
indexing하는 요청을 보냄
4. elastic-search에 미리 설정해둔 pipeline을 통과


---

## pipeline
#### grok processer
store field에 저장된 문자열을 grok pattern을 통해 각각 다른 field의 값으로 저장 

```
"grok": {
    "field": "store",
    "patterns": ["%{DATA: bizesId},%{DATA: bizesNm}, %{DATA: brchNm}, ....]
}
```

> 나중에는 "%{}"로 수정해야함
#### remove processor
이전의 line을 저장한 field 삭제
#### (후에 추가 예정)
숫자값을 가지는 데 문자열로 저장되어 있는 field를 숫자로 변환 **(convert 이용)**
> ex) flrNo (층수)


---

## 문제점
#### 너무 느리다
한번의 요청에 하나의 document씩 보내져서 너무 느리다.
동시에 보내거나 bulk를 이용해 여러 개씩 보내는 게 더 나을 듯