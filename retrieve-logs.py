import json
import requests

def get_api_response(url, headers=None, params=None):
  """
  REST API를 실행하고 응답 값을 저장하는 함수

  Args:
    url: API 엔드포인트 URL
    headers: (선택 사항) API 요청에 포함할 헤더
    params: (선택 사항) API 요청에 포함할 쿼리 매개변수

  Returns:
    response: API 응답 객체
  """
  try:
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()  # HTTP 에러 발생 시 예외 발생

    # 쿼리 파라미터가 있을 경우 URL에 추가
    if params:
      request_url = f"{url}?{'&'.join([f'{k}={v}' for k, v in params.items()])}"
    else:
      request_url = url

    # 요청 URL 출력
    print(f"Request URL: {request_url}")  # request url 출력

    # 응답 JSON을 보기 좋게 출력
    json_data = response.json()
    formatted_json = json.dumps(json_data, indent=4, ensure_ascii=False)
    print(formatted_json)

    return response
  except requests.exceptions.RequestException as e:
    print(f"API 요청 에러: {e}")
    return None

# API 엔드포인트 URL
api_url = "http://13.209.176.153:8080/ssc/api/v1/events"

# API 요청 헤더 (Authorization 헤더에 FortifyToken UnifiedLoginToken 세팅 필요)
headers = {
  "Content-Type": "application/json",
  "Authorization": "FortifyToken ZGQwYTZjZWUtMTI5NS00ZmU0LWE4N2QtNmQyYWMzNzhjMWI1"
}
######################################
# API 요청 쿼리 매개변수 (선택 사항)
# Name	Description	(Type)
# fields:	Output fields (string)
# start:	A start offset in object listing (integer)
# limit:	A maximum number of returned objects in listing, if '-1' or '0' no limit is applied (integer)
# withoutCount:	Disable computing the total object count for the 'count' field (boolean)
# q:	A search query (string)
# orderby:	Fields to order by (string)
######################################
# 응답 json 출력 샘플
# "id": 1191,
# "projectVersionId": null,
# "eventType": "WEBUI_LOGIN_SUCCESS",
# "userName": "ikkb77",
# "detailedNote": "[Security Event]",
# "entityId": null,
######################################
params = {
  "fields": "eventType,userName",
  "start": 0,
  "limit": 0,
  "withoutCount": False,
  "q": "eventType:WEBUI_LOGIN_SUCCESS"
}

# API 실행 및 응답 저장
response = get_api_response(api_url, headers, params)

if response:
  # 응답 상태 코드 출력
  print(response.status_code)
  # 응답 헤더 출력
  print(response.headers)
  # 응답 데이터 출력
  print(response.json())