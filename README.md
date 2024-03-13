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



## 7. 데이터베이스 모델링(ERD)

erDiagram
    User {
        int id PK "Primary Key"
        string username "Username"
        string email "Email"
    }
    
    Post {
        int id PK "Primary Key"
        int author_id FK "Foreign Key to User"
        string title "Post Title"
        string overview "Brief Overview, nullable"
        string poster_path "Poster Path with default value"
        url trailer_url "Trailer URL, nullable"
        date release_date "Release Date, nullable"
        text content "Main Content"
        image thumb_image "Thumbnail Image, blank allowed"
        file file_upload "File Upload, blank allowed"
        datetime created_at "Creation Timestamp"
        date updated_at "Last Update Date"
        int view_count "View Count with default value"
    }
    
    Comment {
        int id PK "Primary Key"
        int post_id FK "Foreign Key to Post"
        int author_id FK "Foreign Key to User"
        text message "Comment Message"
        email email "Email, nullable and blank allowed"
        url website "Website URL, nullable and blank allowed"
        datetime created_at "Creation Timestamp"
        date updated_at "Last Update Date"
    }
    
    User ||--o{ Post : "has many"
    Post ||--o{ Comment : "has many"
    User ||--o{ Comment : "has many"

