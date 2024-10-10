# Movie_Review 
- [日本語 README](README.jp.md)
## 1. 목표와 기능
* 목표<br>
사용자가 영화 목록을 탐색하고, 영화의 상세 정보를 확인할 수 있는 웹 기반 영화 정보 제공 서비스를 제공합니다.

* 기능<br>  
최신 영화 정보 제공: TMDB API를 이용하여, 최신 개봉작들의 정보를 제공합니다.
리뷰 작성 기능: 사용자가 직접 영화 리뷰를 남길 수 있습니다.
사용자 인터랙션 기능 제공: 사용자가 회원가입, 로그인, 프로필 관리, 검색 등의 기능을 통해 서비스와 상호작용할 수 있게 합니다.

## 1.2 개발 환경
Django, html, css, js, bootstrap, TMDB API


## 2. URL 구조 (모놀리식)
* main
<table>
    <tr>
        <th>URL</th>
        <th>Function</th>
        <th>HTML File Name</th>
        <th>Note</th>
    </tr>
    <tr>
        <td>'/'</td>
        <td>HomeView</td>
        <td>index.html</td>
        <td>메인 홈페이지</td>
    </tr>
</table>    

* movies
<table>
    <tr>
        <th>URL</th>
        <th>Function</th>
        <th>HTML File Name</th>
        <th>Note</th>
    </tr>
    <tr>
        <td>'movies/'</td>
        <td>movie_list</td>
        <td>post_list.html</td>
        <td>리뷰 목록</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/'</td>
        <td>movie_detail</td>
        <td>post_detail.html</td>
        <td>리뷰 상세 정보</td>
    </tr>
    <tr>
        <td>'movies/create/'</td>
        <td>movie_create</td>
        <td>form.html</td>
        <td>리뷰 생성</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/update/'</td>
        <td>movie_update</td>
        <td>form.html</td>
        <td>리뷰 수정</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/delete/'</td>
        <td>movie_delete</td>
        <td>post_confirm_delete.html</td>
        <td>리뷰 삭제</td>
    </tr>
    <tr>
        <td>'movies/comments/&lt;int:pk&gt;/'</td>
        <td>comment</td>
        <td>-</td>
        <td>댓글 생성</td>
    </tr>
    <tr>
        <td>'movies/theater/&lt;int:pk&gt;/'</td>
        <td>theater_movie</td>
        <td>movie_detail.html</td>
        <td>극장 상영 영화 상세 정보</td>
    </tr>
    <tr>
        <td>'movies/end_of_release_movies/'</td>
        <td>EOR_MovieList</td>
        <td>EOR_movie_list.html</td>
        <td>개봉 종료 영화 목록</td>
    </tr>
</table>    

* accounts
<table>
    <tr>
        <th>URL</th>
        <th>Function</th>
        <th>HTML File Name</th>
        <th>Note</th>
    </tr>
    <tr>
        <td>'accounts/signup/'</td>
        <td>signup</td>
        <td>form.html</td>
        <td>회원가입</td>
    </tr>
    <tr>
        <td>'accounts/login/'</td>
        <td>login</td>
        <td>form.html</td>
        <td>로그인</td>
    </tr>
    <tr>
        <td>'accounts/logout/'</td>
        <td>logout</td>
        <td>-</td>
        <td>로그아웃</td>
    </tr>
    <tr>
        <td>'accounts/profile/'</td>
        <td>profile</td>
        <td>profile.html</td>
        <td>사용자 프로필</td>
    </tr>
</table>

## 3. 요구사항 명세와 기능 명세
![Movie_요구사항과_기능명세](https://github.com/jsyoo1229/Movie_Review/assets/112743397/3ab82f4f-aae5-4fa9-aca8-cb2090385e72)


## 4. 프로젝트 폴더 구조
┣ 📂accounts <br>
┃ ┣ 📂migrations <br> 
┃ ┣ 📂__pycache__ <br>
┃ ┣ 📜.py <br>
┃ ┣ 📜admin.py <br>
┃ ┣ 📜apps.py <br>
┃ ┣ 📜forms.py <br>
┃ ┣ 📜models.py <br>
┃ ┣ 📜tests.py <br>
┃ ┣ 📜urls.py <br>
┃ ┣ 📜views.py <br>
┃ ┗ 📜__init__.py <br>
┣ 📂movies <br>
┃ ┣ 📂migrations <br>
┃ ┣ 📂__pycache__ <br>
┃ ┣ 📜admin.py <br>
┃ ┣ 📜apps.py <br>
┃ ┣ 📜forms.py <br>
┃ ┣ 📜models.py <br>
┃ ┣ 📜tests.py <br>
┃ ┣ 📜urls.py <br>
┃ ┣ 📜views.py <br>
┃ ┗ 📜__init__.py <br>
┣ 📂static <br>
┃ ┣ 📂css <br>
┃ ┣ 📂fonts <br>
┃ ┣ 📂images <br>
┃ ┣ 📂js <br>
┣ 📂templates <br>
┃ ┣ 📂accounts <br>
┃ ┣ 📂base <br>
┃ ┣ 📂movies <br>
┣ 📂venv <br>
┣📜.gitignore <br>
┣ 📜db.sqlite3 <br>
┣ 📜manage.py <br>
┣ 📜README.md <br>
┗ 📜requirements.txt



## 5. 개발일정(WBS)
![Movie_WBS](https://github.com/jsyoo1229/Movie_Review/assets/112743397/faecd16f-a784-4d6f-ad6e-1c36bb3f5503)

## 6. 와이어프레임
* Home
![Movie  Home](https://github.com/jsyoo1229/Movie_Review/assets/112743397/ebd2826f-916d-4c3a-b0a7-76efd655e2bc)

* 영화 리스트
![Movie  Movie_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/22ddf0a8-4a0e-45fa-8407-569d8fe22d21)

* 리뷰 리스트
![Movie  Review_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/5716f279-0c17-49c6-916e-00668ee89cc5)
  
* 리뷰 작성 폼
![Movie  Review_Form](https://github.com/jsyoo1229/Movie_Review/assets/112743397/9eac70dc-9a48-43f1-bc12-e9e93c1cec8c)


## 7. 화면 설계  
* Home
![Home](https://github.com/jsyoo1229/Movie_Review/assets/112743397/14400be2-be16-487c-8e02-5a178f2b227d)

*로그인
![LogIn](https://github.com/jsyoo1229/Movie_Review/assets/112743397/f70595a2-af63-49b3-bd75-00322338ba24)

*회원가입
![SignUp](https://github.com/jsyoo1229/Movie_Review/assets/112743397/8d3ab81f-e422-45d2-b313-41ba35c10dfb)

* 영화 리스트
![Movie_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/23124fb2-7f9e-4a64-a0ea-3490e3568633)

* 리뷰 리스트
![Review_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/7f44c5bc-c0d5-4215-b5e1-d3eb8340897b)

* 리뷰 작성 폼
![Review_Form](https://github.com/jsyoo1229/Movie_Review/assets/112743397/3d9e334b-e63a-4a04-906d-c7a9a915732f)



## 8. 데이터베이스 모델링(ERD)
![Movie_ERD](https://github.com/jsyoo1229/Movie_Review/assets/112743397/4321c32a-2174-4d09-9c8a-f93531ee2acd)

 ## 9. Architecture
![Movie_Architecture](https://github.com/jsyoo1229/Movie_Review/assets/112743397/bc0d6870-eacf-4a82-833b-ee377e462a70)

 ## 10. 메인 기능
 ![Movie_메인기능](https://github.com/jsyoo1229/Movie_Review/assets/112743397/27094297-e8bd-4361-aada-e9470aae85fa)

 TMDB의 API로 받아온 최신 영화 데이터들을, 사용자에게 제공하는 기능입니다.

 ## 11. 에러 해결
 * API 사용
   아무래도 가장 큰 난관은 API로 영화 데이터를 조작하는 일이었습니다. 아직, API 통신에는 익숙치 않아서, 상당히 힘들었지만.
   CHAT GPT를 활용해, 구현할 수 있었습니다. 앞으로 배우게 될, DRF를 맛보는 느낌이었습니다.

 * CSS 오류
   유료로 구입한 부트스트랩을 사용했는데, 그 부트스트랩의 UI에 새로 Form을 입히거나 할 때, CSS 오류가 나는 경우가 잦았습니다.
   이리 저리 해보다, class명을 새로 입력한 form 코드에 입력하는 식으로, 어떻게든 해낼 수 있었습니다.
   예상치 못한 오류라, 많이 당황했지만, CSS 기술이 느는 좋은 경험이라 느꼈습니다.

## 12. 느낀점
* 많은 경험 필요
확실히 이론적으로 이해하는 것과, 직접 해보는 것의 차이를 느꼈습니다. 머리로는 이해했다고 생각했었지만,
막상 직접 해보니, 코드 흐름이 굉장히 헷갈리기도 하고, 파이썬 기초도 많이 부족하다고 느꼈습니다.
특히, 외부 API를 통해, 데이터를 받아오는 코드를 짜면서, 파이썬 기초가 정말 중요하구나 하고 느꼈습니다.
스스로, 많은 미니 프로젝트를 만들어 보면서, 익힐 필요가 있겠구나 싶습니다.








