## 3. URL 구조
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
        <td>home.html (예시)</td>
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
        <td>movie_list.html</td>
        <td>영화 목록</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/'</td>
        <td>movie_detail</td>
        <td>movie_detail.html</td>
        <td>영화 상세 정보</td>
    </tr>
    <tr>
        <td>'movies/create/'</td>
        <td>movie_create</td>
        <td>movie_form.html (예시)</td>
        <td>영화 생성</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/update/'</td>
        <td>movie_update</td>
        <td>movie_form.html (예시)</td>
        <td>영화 수정</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/delete/'</td>
        <td>movie_delete</td>
        <td>-</td>
        <td>영화 삭제</td>
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
        <td>theater_movie_detail.html (예시)</td>
        <td>극장 상영 영화 상세 정보</td>
    </tr>
    <tr>
        <td>'movies/end_of_release_movies/'</td>
        <td>EOR_MovieList</td>
        <td>EOR_movie_list.html (예시)</td>
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
        <td>signup.html (예시)</td>
        <td>회원가입</td>
    </tr>
    <tr>
        <td>'accounts/login/'</td>
        <td>login</td>
        <td>login.html (예시)</td>
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
        <td>profile.html (예시)</td>
        <td>사용자 프로필</td>
    </tr>
</table>
