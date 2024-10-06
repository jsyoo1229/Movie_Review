## 1. 目標と機能
* 目標<br>
ユーザーが映画のリストを探索し、映画の詳細情報を確認できるウェブベースの映画情報提供サービスを提供します。

* 機能<br>  
最新映画情報の提供: TMDB APIを使用して、最新の公開作の情報を提供します。  
レビュー作成機能: ユーザーが映画レビューを投稿できます。  
ユーザーインタラクション機能の提供: ユーザーは会員登録、ログイン、プロフィール管理、検索などの機能を通じてサービスとやり取りできます。

## 1.2 開発環境
Django, HTML, CSS, JavaScript, Bootstrap, TMDB API

## 2. URL 構造（モノリシック）
* main
<table>
    <tr>
        <th>URL</th>
        <th>機能</th>
        <th>HTMLファイル名</th>
        <th>備考</th>
    </tr>
    <tr>
        <td>'/'</td>
        <td>HomeView</td>
        <td>index.html</td>
        <td>メインホームページ</td>
    </tr>
</table>    

* movies
<table>
    <tr>
        <th>URL</th>
        <th>機能</th>
        <th>HTMLファイル名</th>
        <th>備考</th>
    </tr>
    <tr>
        <td>'movies/'</td>
        <td>movie_list</td>
        <td>post_list.html</td>
        <td>レビューリスト</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/'</td>
        <td>movie_detail</td>
        <td>post_detail.html</td>
        <td>レビュー詳細情報</td>
    </tr>
    <tr>
        <td>'movies/create/'</td>
        <td>movie_create</td>
        <td>form.html</td>
        <td>レビュー作成</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/update/'</td>
        <td>movie_update</td>
        <td>form.html</td>
        <td>レビュー編集</td>
    </tr>
    <tr>
        <td>'movies/&lt;int:pk&gt;/delete/'</td>
        <td>movie_delete</td>
        <td>post_confirm_delete.html</td>
        <td>レビュー削除</td>
    </tr>
    <tr>
        <td>'movies/comments/&lt;int:pk&gt;/'</td>
        <td>comment</td>
        <td>-</td>
        <td>コメント作成</td>
    </tr>
    <tr>
        <td>'movies/theater/&lt;int:pk&gt;/'</td>
        <td>theater_movie</td>
        <td>movie_detail.html</td>
        <td>劇場上映中の映画詳細情報</td>
    </tr>
    <tr>
        <td>'movies/end_of_release_movies/'</td>
        <td>EOR_MovieList</td>
        <td>EOR_movie_list.html</td>
        <td>公開終了映画リスト</td>
    </tr>
</table>    

* accounts
<table>
    <tr>
        <th>URL</th>
        <th>機能</th>
        <th>HTMLファイル名</th>
        <th>備考</th>
    </tr>
    <tr>
        <td>'accounts/signup/'</td>
        <td>signup</td>
        <td>form.html</td>
        <td>会員登録</td>
    </tr>
    <tr>
        <td>'accounts/login/'</td>
        <td>login</td>
        <td>form.html</td>
        <td>ログイン</td>
    </tr>
    <tr>
        <td>'accounts/logout/'</td>
        <td>logout</td>
        <td>-</td>
        <td>ログアウト</td>
    </tr>
    <tr>
        <td>'accounts/profile/'</td>
        <td>profile</td>
        <td>profile.html</td>
        <td>ユーザープロフィール</td>
    </tr>
</table>

## 3. 要求仕様と機能仕様
![Movie_要求仕様と機能仕様](https://github.com/jsyoo1229/Movie_Review/assets/112743397/3ab82f4f-aae5-4fa9-aca8-cb2090385e72)

## 4. プロジェクトフォルダ構造
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
┗ 📜requirements.txt <br>

## 5. 開発スケジュール(WBS)
![Movie_WBS](https://github.com/jsyoo1229/Movie_Review/assets/112743397/faecd16f-a784-4d6f-ad6e-1c36bb3f5503)

## 6. ワイヤーフレーム
* Home
![Movie  Home](https://github.com/jsyoo1229/Movie_Review/assets/112743397/ebd2826f-916d-4c3a-b0a7-76efd655e2bc)

* 映画リスト
![Movie  Movie_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/22ddf0a8-4a0e-45fa-8407-569d8fe22d21)

* レビュリスト
![Movie  Review_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/5716f279-0c17-49c6-916e-00668ee89cc5)
  
* レビュー作成フォーム
![Movie  Review_Form](https://github.com/jsyoo1229/Movie_Review/assets/112743397/9eac70dc-9a48-43f1-bc12-e9e93c1cec8c)

## 7. 画面設計  
* Home
![Home](https://github.com/jsyoo1229/Movie_Review/assets/112743397/14400be2-be16-487c-8e02-5a178f2b227d)

* ログイン
![LogIn](https://github.com/jsyoo1229/Movie_Review/assets/112743397/f70595a2-af63-49b3-bd75-00322338ba24)

* 会員登録
![SignUp](https://github.com/jsyoo1229/Movie_Review/assets/112743397/8d3ab81f-e422-45d2-b313-41ba35c10dfb)

* 映画リスト
![Movie_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/23124fb2-7f9e-4a64-a0ea-3490e3568633)

* レビュリスト
![Review_List](https://github.com/jsyoo1229/Movie_Review/assets/112743397/7f44c5bc-c0d5-4215-b5e1-d3eb8340897b)

* レビュー作成フォーム
![Review_Form](https://github.com/jsyoo1229/Movie_Review/assets/112743397/3d9e334b-e63a-4a04-906d-c7a9a915732f)

## 8. データベースモデリング（ERD）
![Movie_ERD](https://github.com/jsyoo1229/Movie_Review/assets/112743397/4321c32a-2174-4d09-9c8a-f93531ee2acd)

## 9. アーキテクチャ
![Movie_Architecture](https://github.com/jsyoo1229/Movie_Review/assets/112743397/bc0d6870-eacf-4a82-833b-ee377e462a70)

## 10. 主な機能
![Movie_主な機能](https://github.com/jsyoo1229/Movie_Review/assets/112743397/27094297-e8bd-4361-aada-e9470aae85fa)

TMDBのAPIで取得した最新映画データをユーザーに提供する機能です。

## 11. エラー解決
* APIの使用
  一番大変だったのは、APIで映画データを操作することでした。まだAPI通信に慣れていないので、とても難しかったですが、CHAT GPTを活用して実装することができました。今後学ぶことになるDRFの基本を少し味わえた気がします。

* CSSエラー
  有料のBootstrapを使ったのですが、そのBootstrapのUIに新しくフォームを組み込む際に、CSSエラーが頻繁に発生しました。いろいろ試行錯誤した結果、クラス名を新しく入力してフォームコードに適用することで、どうにか対処できました。予期しないエラーだったのでとても驚きましたが、CSSの技術が向上する良い経験となりました。

## 12. 感想
* 多くの経験が必要
確かに理論的に理解することと、実際にやってみることの違いを感じました。頭では理解していると思っていましたが、いざ自分でやってみると、コードの流れが非常に混乱することがあり、Pythonの基礎もまだまだ足りないと感じました。特に、外部APIを通じてデータを取得するコードを書いていると、Pythonの基礎が非常に重要であることを実感しました。これからは自分でミニプロジェクトを多く作って、スキルを身につけていく必要があると感じました。
