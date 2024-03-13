## 3. URL 구조 (모놀리식)
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

## 6. 와이어프레임
*Home
![Movie  Home](https://github.com/jsyoo1229/Movie_Review/assets/112743397/ebd2826f-916d-4c3a-b0a7-76efd655e2bc)

* 영화 리스트
![Movie  Movie_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/22ddf0a8-4a0e-45fa-8407-569d8fe22d21)

* 리뷰 리스트
![Movie  Review_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/5716f279-0c17-49c6-916e-00668ee89cc5)
  
* 리뷰 작성 폼
![Movie  Review_Form](https://github.com/jsyoo1229/Movie_Review/assets/112743397/9eac70dc-9a48-43f1-bc12-e9e93c1cec8c)
  


## 7. 데이터베이스 모델링(ERD)
![Movie_ERD](https://github.com/jsyoo1229/Movie_Review/assets/112743397/4321c32a-2174-4d09-9c8a-f93531ee2acd)

 ## 8. Architecture
![Movie_Architecture](https://github.com/jsyoo1229/Movie_Review/assets/112743397/bc0d6870-eacf-4a82-833b-ee377e462a70)

 






