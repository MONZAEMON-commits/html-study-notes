# 02_css_basics(CSSの基本)
| 学習ステップ                   | 内容                                                     | 具体例                                                |
| :----------------------------- | :------------------------------------------------------- | :---------------------------------------------------- |
| **① 基本構文を理解する**       | CSSの書き方・指定方法・コメントの使い方                  | `p { color: red; } /* コメント */`                    |
| **② 選択子(セレクタ)を覚える** | 要素・クラス・IDなど、どの部分にスタイルを適用するか指定 | `.class名`, `#id名`, `div p` など                     |
| **③ 基本プロパティを使う**     | 色・文字サイズ・背景・余白など                           | `color`, `font-size`, `margin`, `padding`             |
| **④ レイアウトを学ぶ**         | 要素の位置・整列・横並びなど                             | `display`, `position`, `flexbox`, `grid`              |
| **⑤ 装飾とデザイン**           | 枠線・影・丸み・アニメーション                           | `border`, `box-shadow`, `border-radius`, `transition` |
| **⑥ 実践(HTMLと連携)**         | HTMLファイルと組み合わせてデザイン調整                   | `<link rel="stylesheet" href="style.css">`            |

## 基本構文
```css
セレクタ {
  プロパティ: 値;
}
```
### セレクタ(selector)とは？
CSSが「どのHTML要素にスタイルを当てるか」を決める指定のこと。<br>
| 種類           | 書き方       | 対象                        | 例                            |
| :------------- | :----------- | :-------------------------- | :---------------------------- |
| 要素セレクタ   | `p`          | 特定のタグ                  | `<p>テキスト</p>`             |
| クラスセレクタ | `.name`      | `class="name"` が付いた要素 | `<p class="name">...</p>`     |
| IDセレクタ     | `#main`      | `id="main"` が付いた要素    | `<div id="main">...</div>`    |
| 子孫セレクタ   | `div p`      | div内のp要素                | `<div><p>...</p></div>`       |
| グループ化     | `h1, h2, h3` | 複数要素をまとめて指定      | `h1, h2, h3 { color: blue; }` |

### プロパティ(property)と値(value)
スタイルの「項目」と「設定内容」をペアで指定します。<br>
| プロパティ           | 値        | 意味             |
| :------------------- | :-------- | :--------------- |
| `color`              | `red`     | 文字色           |
| `background-color`   | `skyblue` | 背景色           |
| `font-size`          | `16px`    | 文字サイズ       |
| `width` / `height`   | `200px`   | 幅・高さ         |
| `margin` / `padding` | `10px`    | 余白(外側／内側) |

### CSSの書き込み場所(3パターン)
| 方法                  | 書き方                                     | 特徴                                          |
| :-------------------- | :----------------------------------------- | :-------------------------------------------- |
| **外部CSS**(おすすめ) | `<link rel="stylesheet" href="style.css">` | HTMLとCSSを分離できる。複数ページで共有可能。 |
| **内部CSS**           | `<style>p { color: red; }</style>`         | 1ページ内で完結。テストや学習用に便利。       |
| **インラインCSS**     | `<p style="color:red;">テキスト</p>`       | 一部の要素だけ変更。基本は避ける。            |

### 基本のまとめ
| 要素       | 意味               | 例                             |
| :--------- | :----------------- | :----------------------------- |
| セレクタ   | どのHTMLに当てるか | `p`, `.class`, `#id`           |
| プロパティ | 何を変えるか       | `color`, `font-size`, `margin` |
| 値         | どう変えるか       | `red`, `16px`, `auto`          |
| コメント   | メモ書き           | `/* これはコメント */`         |

CSSの基本ルール：「どれが勝つか」は決まっている<br>
同じ要素に複数のスタイルが当たるとき、<br>
CSSは次の順で「どれを適用するか」を判断します<br>

| 優先順位                               | 条件                                    | 例                         |
| :------------------------------------- | :-------------------------------------- | :------------------------- |
| **① インラインスタイル**               | HTMLタグ内に直接書かれたCSS             | `<p style="color:red;">`   |
| **② IDセレクタ**                       | `#id名` で指定されたスタイル            | `#main { color:blue; }`    |
| **③ クラス／属性／疑似クラスセレクタ** | `.class名`, `[type=text]`, `:hover`など | `.notice { color:green; }` |
| **④ 要素セレクタ**                     | `p`, `h1`, `div` など                   | `p { color:gray; }`        |
| **⑤ *(全称セレクタ)**                  | すべての要素に当たる                    | `* { color:black; }`       |

## ボックスモデルの理解

| 名前        | 説明                               | CSSプロパティ例            |
| :---------- | :--------------------------------- | :------------------------- |
| **content** | 実際のテキストや画像の領域         | `width`, `height`          |
| **padding** | 内容と枠線の間の余白               | `padding: 10px;`           |
| **border**  | 枠線そのもの                       | `border: 1px solid black;` |
| **margin**  | 要素の外側の余白(他の要素との間隔) | `margin: 20px;`            |

## ブロックボックスとインラインボックスについて
### 1. すべての要素は「ボックス」でできている。<br>
HTMLの要素はすべて「ボックス」として描画されます。<br>
そのボックスには大きく2種類あります👇
| 種類                   | 英語       | 主な用途                                     |
| :--------------------- | :--------- | :------------------------------------------- |
| **ブロックボックス**   | Block Box  | 段落・セクションのように**縦方向に並ぶ要素** |
| **インラインボックス** | Inline Box | 文章中に**横方向に並ぶ要素**                 |

### 2. ブロックボックス(Block Box)<br>
▶ 特徴
- 縦方向に積み重なる(次の要素は改行される)
- 幅は親要素いっぱい(デフォルトで width: 100%)
- margin や padding が上下左右すべて有効
- width, height を指定できる<br>

▶ 代表的なタグ<br>
`<div>, <p>, <h1>～<h6>, <section>, <ul>, <ol>, <table>` など<br>

### 3. インラインボックス(Inline Box)<br>
▶ 特徴
- 横方向に並ぶ(文章の流れに沿う)
- width や height は指定しても効かない(文字サイズや内容で決まる)
- margin や padding の上下は効かない(左右のみ有効)
- 改行を入れない限り、同じ行に並ぶ<br>

▶ 代表的なタグ<br>
`<span>, <a>, <strong>, <em>, <b>, <i>, <img>` など<br>

## 基本プロパティ(color,font)について
### <a id="color"></a>文字色の指定 — color
書き方
```css
p {
  color: red;              /* 色名 */
  /* color: #ff0000; */    /* 16進数 */
  /* color: rgb(255,0,0); */ /* RGB値 */
}
```
| 方法       | 例                                                          | 説明                             |
| :--------- | :---------------------------------------------------------- | :------------------------------- |
| 名前指定   | `color: blue;`                                              | CSSで定義された色名(約140種類)   |
| 16進数     | `color: #1e90ff;`                                           | `#RRGGBB` 形式(正確な色)         |
| RGB / RGBA | `color: rgb(30,144,255);`<br>`color: rgba(30,144,255,0.5);` | `rgba`は透明度も指定できる(0～1) |

### <a id="font-family"></a>フォントの種類 — font-family
```css
p {
  font-family: "Noto Sans JP", "Meiryo", sans-serif;
}
```
**ルール**
- 複数指定でフォールバック(上から順に使用)
- スペースを含むフォント名は "ダブルクォート" で囲む
- 最後は汎用フォント(sans-serif / serif / monospace)で保険

### <a id="font-size"></a>文字サイズ — font-size
```css
p {
  font-size: 16px;
}
```
**単位の種類**
| 単位  | 意味                         | 備考                   |
| :---- | :--------------------------- | :--------------------- |
| `px`  | ピクセル                     | 固定サイズ(よく使う)   |
| `em`  | 親要素を基準にした相対サイズ | 柔軟なデザイン向け     |
| `%`   | 親要素に対する割合           | レスポンシブ対応に便利 |
| `rem` | ルート(html)要素を基準       | 全体スケール調整に便利 |

### <a id="font-weight"></a>太さ — font-weight
```css
p {
  font-weight: bold;
}
```
| 値       | 意味                                   |
| :------- | :------------------------------------- |
| `normal` | 標準(400)                              |
| `bold`   | 太字(700)                              |
| 数値     | 100～900で細かく指定(対応フォントのみ) |

### <a id="line-height"></a>行の高さ — line-height
```css
p {
  line-height: 1.6;
}
```
**ポイント**
- 単位なし(1.6など)→「フォントサイズ × 1.6」
- px指定も可能(例：24px)
- 文字が詰まりすぎる場合に調整
### <a id="font-style"></a>フォントスタイル・装飾 font-style
```css
a {
  text-decoration: none; /* リンク下線を消す */
}
em {
  font-style: italic; /* イタリック */
}
```
| プロパティ        | 値                                  | 効果             |
| :---------------- | :---------------------------------- | :--------------- |
| `font-style`      | `normal`, `italic`                  | 斜体にする       |
| `text-decoration` | `none`, `underline`, `line-through` | 下線や取り消し線 |

### font ショートハンド
`font: [font-style] [font-weight] [font-size]/[line-height] [font-family];`

```css
font: italic bold 16px/1.5 "Noto Sans JP", sans-serif;
```
**fontショートハンドまとめ**
| プロパティ                               | ショートハンドでの位置    | 例                           |
| :--------------------------------------- | :------------------------ | :--------------------------- |
| <a href="#font-style">`font-style`</a>   | 最初(任意)                | `italic`                     |
| `font-variant`                           | 2番目(任意)               | `small-caps`                 |
| <a href="#font-weight">`font-weight`</a> | 3番目(任意)               | `bold` / `700`               |
| <a href="#font-size">`font-size`</a>     | 必須(`line-height`より前) | `16px` / `1rem`              |
| <a href="#line-height">`line-height`</a> | `/` の後(任意)            | `1.5` / `24px`               |
| <a href="#font-family">`font-family`</a> | 最後(必須)                | `"Noto Sans JP", sans-serif` |

### 文字揃え — text-align
```css
p {
  text-align: center;
}
```
| 値        | 意味                   |
| :-------- | :--------------------- |
| `left`    | 左揃え(既定)           |
| `center`  | 中央揃え               |
| `right`   | 右揃え                 |
| `justify` | 両端揃え(新聞のように) |


### 基本プロパティ(font関連)まとめ

| 分類     | プロパティ                                                | 主な値                             |
| :------- | :-------------------------------------------------------- | :--------------------------------- |
| 文字の色 | <a href="#color">`color`</a>                              | `#333`, `red`, `rgba(255,0,0,0.5)` |
| フォント | <a href="#font-family">`font-family`</a>                  | `"Noto Sans JP"`, `sans-serif`     |
| サイズ   | <a href="#font-size">`font-size`</a>                      | `16px`, `1.2rem`                   |
| 太さ     | <a href="#font-weight">`font-weight`</a>                  | `normal`, `bold`, `700`            |
| 揃え     | <a href="#text-align">`text-align`</a>                    | `left`, `center`, `right`          |
| 行間     | <a href="#line-height">`line-height`</a>                  | `1.5`, `24px`                      |
| 装飾     | `text-decoration`, <a href="#font-style">`font-style`</a> | `underline`, `italic`              |

## 基本のプロパティ(background)について

### <a id="background-color"></a>背景色 — background-color

```css
div {
  background-color: skyblue;
}
```
**ポイント**
- 要素全体(padding＋content)に色がつく
- 色の指定方法は <a href="#color">color</a> と同じ(名前・16進数・RGBなど)

### <a id="background-image"></a>背景画像 — background-image
```css
div {
  background-image: url("images/bg.jpg");
}
```
**よく使う関連プロパティ：**
| プロパティ              | 意味           | 例                                  |
| :---------------------- | :------------- | :---------------------------------- |
| `background-repeat`     | 繰り返し設定   | `no-repeat`, `repeat-x`, `repeat-y` |
| `background-position`   | 位置           | `center`, `top`, `left 20px`        |
| `background-size`       | 画像サイズ     | `cover`, `contain`, `100% 100%`     |
| `background-attachment` | スクロール挙動 | `fixed`, `scroll`                   |

### <a id="background-repeat"></a>background-repeat(背景画像の繰り返し)
背景画像をどの方向に繰り返すかを指定するプロパティです。

```css
background-repeat: 値;
```
| 値          | 意味                                   | 説明               |
| :---------- | :------------------------------------- | :----------------- |
| `repeat`    | 縦横に繰り返す(デフォルト)             | タイル状に敷き詰め |
| `no-repeat` | 繰り返さない                           | 画像を1枚だけ表示  |
| `repeat-x`  | 横方向にのみ繰り返す                   | 横並びのパターンに |
| `repeat-y`  | 縦方向にのみ繰り返す                   | 縦に並ぶパターンに |
| `space`     | 隙間を均等に埋めて繰り返す             | (対応ブラウザ限定) |
| `round`     | 繰り返し数を自動調整して全体にフィット | (対応ブラウザ限定) |

### <a id="background-position"></a>background-position(背景画像の位置)
```css
background-position: 横位置 縦位置;
```
| 指定            | 意味                     |
| :-------------- | :----------------------- |
| `left top`      | 左上(初期値)             |
| `center center` | 中央                     |
| `right bottom`  | 右下                     |
| `50% 50%`       | 中央(パーセンテージ指定) |
| `20px 100px`    | 左から20px、上から100px  |

### <a id="background-size"></a>background-size(背景画像のサイズ)
```css
background-size: 値;
```
| 値            | 意味                                       | 説明                   |
| :------------ | :----------------------------------------- | :--------------------- |
| `auto`        | 元画像の大きさのまま                       | デフォルト             |
| `cover`       | 要素全体を覆うように拡大／トリミングされる | 背景全面にピッタリ     |
| `contain`     | 要素に収まるように縮小                     | 画像全体が見えるように |
| `100px 200px` | 幅100px・高さ200px                         | 明示的なサイズ指定     |
| `50% 50%`     | 幅・高さを要素サイズの割合で指定           |                        |

### <a id="background-attachment"></a>background-attachment(背景の固定)
```css
background-attachment: 値;
```
| 値       | 意味                                         |
| :------- | :------------------------------------------- |
| `scroll` | 背景が一緒にスクロール(デフォルト)           |
| `fixed`  | 背景が固定され、コンテンツだけが動く         |
| `local`  | 要素内のスクロールに合わせて動く(特定要素内) |

### backgroundショートハンド
```css
background: [color] [image] [repeat] [position] / [size] [attachment];
```
**注意点**
- positionとsizaを記載する場合は/が必須となる。それ以外は不要。

| プロパティ                                                   | ショートハンドでの位置 | 例              |
| :----------------------------------------------------------- | :--------------------- | :-------------- |
| <a href="#background-color">`background-color`</a>           | 最初                   | `#fafafa`       |
| <a href="#background-image">`background-image`</a>           | 2番目                  | `url("bg.jpg")` |
| <a href="#background-repeat">`background-repeat`</a>         | 3番目                  | `no-repeat`     |
| <a href="#background-position">`background-position`</a>     | 4番目(スラッシュの前)  | `center`        |
| <a href="#background-size">`background-size`</a>             | `/` の後               | `cover`         |
| <a href="#background-attachment">`background-attachment`</a> | 最後                   | `fixed`         |

## 基本のプロパティ(padding,margin,box-sizing)について
### padding(内側余白)について
書式
```css
padding: [値];
```
または、上下左右を個別に指定する場合：
```css
padding-top: [値];
padding-right: [値];
padding-bottom: [値];
padding-left: [値];
```
説明<br>
padding は、要素の内側の余白を設定するプロパティです。<br>
要素の内容(テキストや画像)と枠線(border)の間のスペースを作ります。<br>
- 値の単位には px, em, % などを使えます。
- 4方向をまとめて指定するショートハンドもあります。
- padding は 背景色や背景画像の領域にも影響します。

**値の指定方法(ショートハンド)**

| 指定数 | 書式                            | 意味                           | 例                             |
| :----: | :------------------------------ | :----------------------------- | :----------------------------- |
|  1つ   | `padding: 10px;`                | 全方向に同じ余白               | 上下左右10px                   |
|  2つ   | `padding: 10px 20px;`           | 上下＝10px、左右＝20px         |                                |
|  3つ   | `padding: 10px 20px 30px;`      | 上＝10px、左右＝20px、下＝30px |                                |
|  4つ   | `padding: 10px 20px 30px 40px;` | 上→右→下→左の順                | 上10px, 右20px, 下30px, 左40px |

例文
```css
.box {
  background-color: lightblue;
  padding: 20px;
}
```
説明<br>
- ボックスの中の文字や画像が、上下左右に20pxだけ内側へ離れる。
- 背景色は padding の範囲まで広がる。

**注意点**
- padding は 内側の余白であり、**外側の間隔(要素同士の距離)**は margin を使う。
- padding は要素の幅や高さに影響する(ボックスが大きくなる)。
 `→ box-sizing: border-box; を指定すると、幅の中に padding を含められる。`
- % 指定の場合、親要素の幅を基準に計算される。
- padding に負の値(マイナス値)は指定できない。

### padding(内側余白)まとめ
| 項目     | 内容                                               |
| :------- | :------------------------------------------------- |
| 目的     | 要素の内側に余白を作る                             |
| 主な書式 | `padding: 値;` ／ `padding-top/right/bottom/left:` |
| 値の順序 | 上 → 右 → 下 → 左                                  |
| 注意点   | 要素のサイズに影響する・負の値不可                 |

### margin(外側余白)について
構文
```css
margin: [値];
```
または、上下左右を個別に指定する場合：
```css
margin-top: [値];
margin-right: [値];
margin-bottom: [値];
margin-left: [値];
```
説明<br>
margin は、要素の外側にできる余白を設定するプロパティです。<br>
要素と要素の間の距離(上下・左右のスペース)を作るために使います。<br>
- padding は内側の余白、margin は外側の余白。
- 値は px, em, %, auto が使えます。
- margin は透明なスペースを作り、背景色には影響しません。

**値の指定方法(ショートハンド)**
| 指定数 | 書式                           | 意味                           | 例                             |
| :----: | :----------------------------- | :----------------------------- | :----------------------------- |
|  1つ   | `margin: 10px;`                | 全方向に同じ余白               | 上下左右10px                   |
|  2つ   | `margin: 10px 20px;`           | 上下＝10px、左右＝20px         |                                |
|  3つ   | `margin: 10px 20px 30px;`      | 上＝10px、左右＝20px、下＝30px |                                |
|  4つ   | `margin: 10px 20px 30px 40px;` | 上→右→下→左の順                | 上10px, 右20px, 下30px, 左40px |

例文
```css
.box {
  background-color: lightgreen;
  margin: 20px;
}
```
説明<br>
- .box の外側に20pxの余白ができ、他の要素と距離をとる。
- 背景色や枠線は含まれず、単にスペースが空くだけ。

**注意点**
- margin は 外側のスペースを作るプロパティ。
`→ 内容(テキスト)との距離を取りたい場合は padding を使う。`
- margin は **負の値(マイナス)**も指定できる。
`→ 要素を上や左に「引き寄せる」ような調整が可能。`
- **上下のmarginは重なり(marginの相殺)**が起きる。
`→ 隣り合うブロック要素で、上と下の margin が重なった場合、大きい方の値のみが適用される。`
- % 指定の場合、親要素の幅を基準に計算される(paddingと同じ)。

### margin(外側余白)まとめ
| 項目     | 内容                                             |
| :------- | :----------------------------------------------- |
| 目的     | 要素の外側に余白を作る                           |
| 主な書式 | `margin: 値;` ／ `margin-top/right/bottom/left:` |
| 値の順序 | 上 → 右 → 下 → 左                                |
| 特殊値   | `auto`(中央寄せ)、負の値(要素を詰める)           |
| 注意点   | 上下の`margin`は重なりやすい(marginの相殺)       |

### box-sizing(サイズ計算の仕組み)について
構文
```css
box-sizing: content-box | border-box;
```
説明<br>
box-sizing は、幅(width)や高さ(height)をどの範囲で計算するかを指定するプロパティです。<br>
CSSのボックスモデルでは、<br>
1つの要素は次のような層で構成されています👇<br>
```css
┌──────────────────────────────┐
│        margin(外側余白)     │
│ ┌──────────────────────────┐ │
│ │      border(枠線)       │ │
│ │ ┌──────────────────────┐ │ │
│ │ │ padding(内側余白)   │ │ │
│ │ │ ┌──────────────────┐ │ │ │
│ │ │ │ content(中身)   │ │ │ │
│ │ │ └──────────────────┘ │ │ │
│ │ └──────────────────────┘ │ │
│ └──────────────────────────┘ │
└──────────────────────────────┘
```
デフォルトでは、width は content(中身)だけ のサイズを指しますが、<br>
padding や border を含めて計算したい場合に使うのが box-sizing です<br>

値の意味

| 値            | 説明                                              | サイズの含まれる範囲       |
| :------------ | :------------------------------------------------ | :------------------------- |
| `content-box` | デフォルト。`width` は**中身(content)のみ**を指す | content                    |
| `border-box`  | `width` に **padding + border も含める**          | content + padding + border |

例文
```css
/* デフォルト動作(content-box) */
.box1 {
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  box-sizing: content-box;
}

/* paddingとborderを含めて200pxに収まる(border-box) */
.box2 {
  width: 200px;
  padding: 20px;
  border: 5px solid #333;
  box-sizing: border-box;
}
```
説明<br>
- .box1(content-box)は、200px(中身)＋ 20px×2(padding)＋ 5px×2(border)＝ 合計250pxの表示幅 になる。
- .box2(border-box)は、200pxの中にpaddingとborderを含むため、見た目の幅が200pxに収まる。

**注意点**
- ブラウザのデフォルトは content-box。
`→ そのままだと padding や border を追加するたびにサイズが変わる。`
- 一般的な開発では、全要素を border-box に統一することが多い。
```css
* {
  box-sizing: border-box;
}
```
- border-box にしておくと、デザイン崩れを防ぎやすく、余白を含めた正確な幅指定が可能になる。
- box-sizing は要素単位で指定できる(特定のブロックだけ変えることも可)。

### box-sizing(サイズ計算の仕組み)まとめ
| 項目         | 内容                                                        |
| :----------- | :---------------------------------------------------------- |
| 目的         | width / height に含まれる範囲を制御する                     |
| 主な値       | `content-box`(デフォルト), `border-box`                     |
| よく使う設定 | `* { box-sizing: border-box; }`                             |
| 注意点       | `border-box` にすると余白を含めても見た目サイズが変わらない |

## border(枠線)基本について
CSSの border は、要素の外枠を装飾するためのプロパティ。<br>
線の「太さ」「種類」「色」を組み合わせて指定します。<br>

### border(枠線)基本構文
```css
border: [border-width] [border-style] [border-color];
例文
div {
  border: 2px solid black;
}
```
border プロパティは、要素の外枠に線を描くためのCSSプロパティです。<br>
「太さ(width)」「線の種類(style)」「色(color)」を指定して、<br>
ボックスの輪郭をデザインします。<br>
3つの指定のうち、<br>
🟡 border-style は必須項目です。<br>
太さや色を省略した場合は、次の初期値が適用されます。<br>

| 項目           | 省略時の初期値               | 例                                            |
| :------------- | :--------------------------- | :-------------------------------------------- |
| `border-width` | `medium`(約3px)              | `1px`, `0.2em`, `thin`, `thick`               |
| `border-style` | `none`(線なし)               | `solid`, `dashed`, `dotted`, `double`, `none` |
| `border-color` | `currentColor`(文字色と同じ) | `#333`, `red`, `rgba(0,0,0,0.5)`              |

### 補足-枠線の種類(border-style)
border-style には、見た目のバリエーションがあります👇
| 値       | 見た目 | 説明                     |
| :------- | :----: | :----------------------- |
| `none`   |   ―    | 枠線なし(初期値)         |
| `solid`  |   ━    | 実線(最も一般的)         |
| `dashed` | ┄ ┄ ┄  | 破線(短い線の連続)       |
| `dotted` |  ⋯⋯⋯   | 点線(ドット状)           |
| `double` |   ═    | 二重線(2本の線)          |
| `groove` |   ▢    | 凹んだ3D効果の線         |
| `ridge`  |   ▢    | 浮き上がる3D効果の線     |
| `inset`  |   ▣    | 内側に沈み込むような線   |
| `outset` |   ▣    | 外側に浮き上がるような線 |

`💡 groove・ridge・inset・outset は、要素の background-color に応じて自動的に陰影が付きます。`

### 各辺ごとの指定
構文
```css
border-top: [width] [style] [color];
border-right: [width] [style] [color];
border-bottom: [width] [style] [color];
border-left: [width] [style] [color];
```
説明<br>
border は、上下左右の各辺を独立して指定することができます。<br>
部分的に異なる線を引きたい場合に使用します。<br>

例文
```css
div {
  border-top: 3px solid red;
  border-right: 3px dashed green;
  border-bottom: 3px double blue;
  border-left: 3px dotted orange;
}
```
注意点
- 各辺の構文も、通常の border と同様に [太さ] [スタイル] [色] の順で指定できます。
- border-style を忘れると線は描画されません。
- 上下左右すべてに異なるスタイルを設定することも可能。

### borderまとめ

| 項目           | 内容                                                                        |
| :------------- | :-------------------------------------------------------------------------- |
| 基本構文       | `border: [width] [style] [color];`                                          |
| 各辺構文       | `border-top/right/bottom/left: [width] [style] [color];`                    |
| スタイルの種類 | `solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset` |
| 注意点         | `border-style` は必須／線は padding の外側に描画される                      |


## 枠線の角を丸くする — border-radius
構文
```css
border-radius: [半径];
```
説明<br>
border-radius は、要素の角を丸くするプロパティです。<br>
値には丸める半径を指定し、単位は px や % を使います。<br>
指定した半径分だけ、角が円弧状になります。
単一の値を指定 → 4つの角すべてが同じ丸み。
複数値を指定 → 各角を個別に調整可能。

% 指定にすると、要素サイズに対して割合で丸みを設定できる。

| 値              | 効果                             |
| :-------------- | :------------------------------- |
| `5px`           | 角を少し丸くする                 |
| `50%`           | 丸い形(正方形の画像で円に)       |
| `10px 0 10px 0` | 各角を個別指定(左上から時計回り) |

例文
```css
button {
  border-radius: 50%;
  width: 60px;
  height: 60px;
}
```
## 影をつける — box-shadow
構文
```css
box-shadow: X方向 Y方向 ぼかし距離 色;
``` 
説明<br>
box-shadow は、要素の周囲に**影（シャドウ）**をつけるプロパティです。<br>
値はそれぞれ次の意味を持ちます。<br>
| 項目           | 説明                                     | 例                |
| :------------- | :--------------------------------------- | :---------------- |
| **X方向**      | 横のずらし距離（右が+、左が–）           | `5px`             |
| **Y方向**      | 縦のずらし距離（下が+、上が–）           | `5px`             |
| **ぼかし距離** | 影の広がり具合（値が大きいほど柔らかく） | `10px`            |
| **色**         | 影の色（rgbaで透明度指定が一般的）       | `rgba(0,0,0,0.3)` |

例文
```css
.box {
  width: 200px;
  height: 100px;
  background-color: white;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
}
```
説明<br>
- 下方向（Y軸）に4px、横方向に0px影を落とす。
- 透明度0.2の柔らかい影で、立体感を出す。

応用例（内側に影をつける）
```css
.box {
  box-shadow: inset 0 0 10px rgba(0, 0, 0, 0.3);
}
```
説明<br>
- inset をつけると影が「内側」に描かれる。
- 凹んだような見た目を作るときに使う。

**注意点**
- box-shadow は複数重ねることが可能（カンマ区切り）。
```css
box-shadow: 0 2px 4px rgba(0,0,0,0.2),
            0 6px 12px rgba(0,0,0,0.15);
```
- 影は border-radius に追従する。角丸ボックスでも自然に影がかかる。
- 影の色を濃くしすぎるとチープに見えるので、rgba() で透過度を調整するのが一般的。
### box-shadowまとめ
| 項目     | 内容                                     |
| :------- | :--------------------------------------- |
| 基本構文 | `box-shadow: X方向 Y方向 ぼかし 色;`     |
| 内側の影 | `inset` を先頭に指定                     |
| 複数影   | カンマ区切りで追加可能                   |
| 注意点   | `border-radius` と併用可、色は透過を意識 |

## 変化をなめらかに — transition
構文
```css
transition: [対象プロパティ] [時間] [タイミング関数] [遅延時間];
```
説明<br>
transition は、要素のスタイルが変化するとき（例：hover時）に、<br>
アニメーションのようにゆっくり変化させるためのプロパティです。<br>
「どのプロパティを」「どのくらいの時間で」「どんな速さで」変化させるかを指定します。<br>
| 項目               | 意味                                                 | 例                                                     |
| :----------------- | :--------------------------------------------------- | :----------------------------------------------------- |
| **対象プロパティ** | 変化の対象（例：`color`, `background-color`, `all`） | `background-color`                                     |
| **時間**           | 変化にかける時間                                     | `0.3s`, `1s`                                           |
| **タイミング関数** | 変化の速さの曲線                                     | `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out` |
| **遅延時間**       | 開始までの待機時間（任意）                           | `0.2s`                                                 |
例文（基本）
```css
button {
  background-color: #2196f3;
  color: white;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #0d47a1;
}
```
説明<br>
- 通常時は青（#2196f3）、マウスを乗せると濃い青（#0d47a1）に。
- transition により、色が0.3秒かけてなめらかに変化する。

応用（複数プロパティ）
```css
.card {
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
  transform: scale(1);
  transition: box-shadow 0.3s, transform 0.3s;
}

.card:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3);
  transform: scale(1.05);
}
```
説明<br>
- hover時に影が濃くなり、少し拡大する。
- 影と拡大の両方に 0.3秒のトランジションを適用。<br>

タイミング関数（速度カーブ）
| 値            | 効果                                             |
| :------------ | :----------------------------------------------- |
| `linear`      | 一定速度で変化                                   |
| `ease`        | ゆるやかに始まり、ゆるやかに終わる（デフォルト） |
| `ease-in`     | ゆっくり始まり、速く終わる                       |
| `ease-out`    | 速く始まり、ゆっくり終わる                       |
| `ease-in-out` | ゆっくり→速く→ゆっくり                           |

**注意点**
- transition は**変化が起きるイベント（例：hover, focus, activeなど）**と組み合わせて使う。
- 適用対象は「数値的に変化できるプロパティ」（例：color, opacity, transform）。<br>
`→ display のようにオン・オフだけのプロパティには適用されない。`
- transition: all 0.3s; と書くとすべての変化に適用できるが、パフォーマンスを考えると対象プロパティを絞る方が望ましい。

### transitionまとめ
| 項目               | 内容                                                     |
| :----------------- | :------------------------------------------------------- |
| 基本構文           | `transition: プロパティ 時間 タイミング関数 遅延;`       |
| よく使う組み合わせ | `background-color`, `opacity`, `transform`, `box-shadow` |
| 複数指定           | カンマ区切りで並べる                                     |
| 注意点             | 数値的に変化できるプロパティにのみ有効                   |

