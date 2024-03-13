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
![Movie_ERD](https://github.com/jsyoo1229/Movie_Review/assets/112743397/4321c32a-2174-4d09-9c8a-f93531ee2acd)

 ## 8. Architecture

 graph TD
    subgraph config ["config (Project Level)"]
        urlsConfig["urls.py"]
        settings["settings.py"]
    end

    subgraph accounts ["accounts App"]
        urlsAccounts["urls.py"]
        viewsAccounts["views.py"]
        formsAccounts["forms.py"]
        modelsUser["User (Django Auth Model)"]
    end

    subgraph movies ["movies App"]
        urlsMovies["urls.py"]
        viewsMovies["views.py"]
        formsMovies["forms.py"]
        modelsMovies["models.py"]
    end

    urlsConfig --> urlsAccounts
    urlsConfig --> urlsMovies
    urlsConfig --> HomeView
    urlsConfig --> staticFiles{"static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"}

    urlsAccounts --> signup
    urlsAccounts --> login
    urlsAccounts --> logout
    urlsAccounts --> profile

    urlsMovies --> movie_list
    urlsMovies --> movie_detail
    urlsMovies --> movie_create
    urlsMovies --> movie_update
    urlsMovies --> movie_delete
    urlsMovies --> comment_create["comments/<int:pk>/"]
    urlsMovies --> theater_movie_detail["theater/<int:pk>/"]
    urlsMovies --> EOR_MovieList["end_of_release_movies/"]

    viewsAccounts --> formsAccounts
    viewsAccounts --> modelsUser

    viewsMovies --> formsMovies
    viewsMovies --> modelsMovies

    formsAccounts --> modelsUser
    formsMovies --> modelsMovies

    modelsMovies --> modelsUser

    classDef app fill:#f9f,stroke:#333,stroke-width:2px;
    classDef django fill:#bbf,stroke:#333,stroke-width:2px;
    classDef file fill:#dfd,stroke:#333,stroke-width:2px;
    classDef code fill:#ffd,stroke:#333,stroke-width:4px;

    class config,accounts,movies app;
    class User django;
    class urlsConfig,urlsAccounts,urlsMovies,settings file;
    class viewsAccounts,viewsMovies,formsAccounts,formsMovies,modelsMovies code;






