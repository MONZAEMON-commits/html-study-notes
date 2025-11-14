# 04_flexbox(Flexbox(フレックスボックス)について)
Flexbox は、「要素を横・縦に柔軟に並べる」ためのCSSレイアウト手法です。<br>
現代のWeb制作では、ヘッダー・フッター・カード・ボタン配置など、<br>
9割のレイアウトがFlexで構築できます。<br>
構文
```css
display: flex;
```
Flexboxを有効化するには、<br>
**親要素(コンテナ)に display: flex; を指定します。<br>
その中の子要素(アイテム)**が、自動的にフレックスレイアウトで並びます。<br>

説明<br>
Flexbox(Flexible Box Layout)は、<br>
要素を**横方向(row)や縦方向(column)**に<br>
柔軟に配置・整列・伸縮させるためのレイアウト方法です。<br>
特徴は以下のとおり👇<br>
| 特徴                         | 説明                                                     |
| :--------------------------- | :------------------------------------------------------- |
| ✅ **柔軟な並び**             | 子要素の幅や数に合わせて自動調整される                   |
| ✅ **中央寄せが簡単**         | `justify-content` + `align-items` の組み合わせで実現可能 |
| ✅ **スペース配分が自在**     | 均等配置・余白の自動分配などが容易                       |
| ✅ **レスポンシブ対応に強い** | 画面幅に応じて自然に要素が折り返せる                     |

基本構成<br>
Flexboxは**親要素(コンテナ)と子要素(アイテム)**に分かれます。<br>

## **親要素で使う主なプロパティ**
| プロパティ        | 内容                       | 例                                      |
| :---------------- | :------------------------- | :-------------------------------------- |
| `display: flex;`  | Flexboxを有効化            | `display: flex;`                        |
| `flex-direction`  | 並びの方向を決める         | `row`(横並び) / `column`(縦並び)        |
| `justify-content` | メイン軸(横or縦)の整列方法 | `flex-start`, `center`, `space-between` |
| `align-items`     | 交差軸(縦or横)の整列方法   | `flex-start`, `center`, `flex-end`      |
| `flex-wrap`       | 折り返しの有無を設定       | `nowrap`, `wrap`                        |
| `gap`             | 要素間のすき間を設定       | `gap: 10px;`                            |

## **子要素で使う主なプロパティ**
| プロパティ    | 内容                 | 例                    |
| :------------ | :------------------- | :-------------------- |
| `flex-grow`   | 空きスペースの拡大率 | `flex-grow: 1;`       |
| `flex-shrink` | 要素の縮小率         | `flex-shrink: 0;`     |
| `flex-basis`  | 要素の基準サイズ     | `flex-basis: 200px;`  |
| `order`       | 並び順を変更         | `order: 2;`           |
| `align-self`  | 個別に整列位置を変更 | `align-self: center;` |

## Flexbox：親要素のプロパティ
例文 (親要素の設定)
```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.item {
  background: lightblue;
  padding: 10px;
}
```
説明<br>
- .container が Flexコンテナ。
- 中の .item 要素が横並びで配置される。
- 横方向に均等配置し、縦方向の中央に整列される。<br>

例文2(親要素の設定)
```css
.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}
```
説明<br>
- 要素を縦方向(column)に並べる。<br>
- 左寄せで縦に積み上げる配置。<br>

**注意点**
- display: flex; は 親要素に指定する。子に指定しても何も起きない。
- ブロック要素・インライン要素の区別は無視され、すべての子要素が「フレックスアイテム」として扱われる。
- justify-content は「並びの方向(メイン軸)」に影響する。<br>
`→ row なら横、column なら縦方向に整列。`
- align-items はメイン軸と**直交する方向(交差軸)**に影響する。

## **親要素の制御についてまとめ**
| 項目           | 内容                                                      |
| :------------- | :-------------------------------------------------------- |
| 目的           | 要素を柔軟に並べ・整列させる                              |
| 設定対象       | 親要素(子要素が影響を受ける)                              |
| 主なプロパティ | `flex-direction`, `justify-content`, `align-items`, `gap` |
| 特徴           | 中央寄せ・均等配置・折り返しが簡単                        |
| 注意点         | 親に指定する・旧仕様(float)より新しい                     |

## flex-direction（並び方向を決める）
構文
```css
flex-direction: row | row-reverse | column | column-reverse;
```
説明<br>
Flexbox の「子要素がどの方向へ並ぶか」を決めるプロパティ。<br>
並び方向が変わると、 justify-content（主軸揃え） と align-items（交差軸揃え）が入れ替わるため、<br>
Flexbox の最も基本となる設定。<br>

| 値               | 並び方向        | 主軸         | 交差軸 | 主な用途                         |
| ---------------- | --------------- | ------------ | ------ | -------------------------------- |
| `row`            | 左→右（横並び） | 横向き       | 縦向き | デフォルトのメニュー・ボタン等   |
| `column`         | 上→下（縦並び） | 縦向き       | 横向き | スマホレイアウト・縦に積むカード |
| `row-reverse`    | 右→左           | 横（逆方向） | 縦     | 特殊UI（右から並べたい場合）     |
| `column-reverse` | 下→上           | 縦（逆方向） | 横     | チャットUIなど                   |

例文
```css
.container {
  display: flex;
  flex-direction: column;
  gap: 10px;
}
```
説明:子要素が縦方向に並び、上下に 10px の間隔をつける。
**注意点**
- justify-content と align-items の「軸」が flex-direction によって変わる<br>
`→ row の justify-content は横揃え / column の justify-content は縦揃え`
- 逆方向（-reverse）は CSS アニメーションと相性が悪い場合がある
- column を使うと高さ依存のレイアウトが崩れやすくなることがある

## justify-content と align-items(Flexbox の整列)について
構文
```css
/* 親要素に指定 */
.container {
  display: flex;
  justify-content: 値;
  align-items: 値;
}
```
説明<br>
Flexbox では、要素の整列方向が「軸(axis)」で決まります👇<br>
| 軸の種類                | 向き                              | 関連プロパティ    |
| :---------------------- | :-------------------------------- | :---------------- |
| **メイン軸(main axis)** | `flex-direction` の方向(横が基本) | `justify-content` |
| **交差軸(cross axis)**  | メイン軸に直交する方向(縦)        | `align-items`     |

つまり：<br>
- 横方向(main axis)に整列 → justify-content
- 縦方向(cross axis)に整列 → align-items<br>
例文(親要素の設定)

```css
/* 親要素：横方向に中央寄せ */
.container {
  display: flex;
  justify-content: center;  /* 横方向(メイン軸)の中央揃え */
  align-items: center;      /* 縦方向(交差軸)の中央揃え */
  height: 200px;            /* 中央位置を確認しやすくする */
  background-color: #eef;
}
```
説明<br>
- .container は Flex の「親要素」。
- 子要素 .item は自動で横並びになる。
- 横も縦も完全中央揃え。

使用例(HTML構造)
```html
<div class="container">
  <div class="item">A</div>
  <div class="item">B</div>
  <div class="item">C</div>
</div>
```
結果：<br>
A・B・Cが 横一列で中央に配置される。<br>
### **justify-content の値(横方向)**
| 値              | 説明                     | 配置イメージ  |
| :-------------- | :----------------------- | :-----------: |
| `flex-start`    | 左寄せ(デフォルト)       |    ⬅️ A B C    |
| `center`        | 中央寄せ                 |  ⬅️　A B C　➡️  |
| `flex-end`      | 右寄せ                   |    A B C ➡️    |
| `space-between` | 両端揃え(間は均等)       |    A　B　C    |
| `space-around`  | 各要素の前後に等しい余白 | ⬅️ A ⬅️ B ⬅️ C ➡️ |
| `space-evenly`  | 全ての間隔を均等に       |   A ⬅️ B ⬅️ C   |

### **align-items の値(縦方向)**
| 値           | 説明                                     |      配置イメージ(縦)      |
| :----------- | :--------------------------------------- | :------------------------: |
| `flex-start` | 上寄せ                                   |          ⬆️ A B C           |
| `center`     | 縦方向中央揃え                           |          ↕️ A B C           |
| `flex-end`   | 下寄せ                                   |          ⬇️ A B C           |
| `stretch`    | 高さを親要素に合わせて伸ばす(デフォルト) | A B C が親いっぱいに伸びる |
| `baseline`   | テキストのベースラインで揃える           |   文字列の下線位置を基準   |

**応用例(親要素＋複合指定)**
```css
.container {
  display: flex;
  justify-content: space-between; /* 横は両端揃え */
  align-items: flex-start;        /* 縦は上揃え */
  gap: 10px;                      /* 要素間の間隔 */
}
```
説明<br>
- 横方向は左右の端に子要素を配置。
- 縦方向は上揃え。
- gap で間隔を簡単に設定できる。

**注意点**
- justify-content と align-items は親要素(コンテナ)に指定する。
- 両方を使うことで2軸方向の整列が可能。
- align-items: stretch; はデフォルト動作なので、高さを指定していないと自動で引き伸ばされる。
- gap は旧ブラウザで未対応だったが、現在は主要ブラウザ全てで対応済み。

## justify-content と align-itemsまとめ
| プロパティ        | 方向             | 主な値                                | よく使う目的 |
| :---------------- | :--------------- | :------------------------------------ | :----------- |
| `justify-content` | 横方向(メイン軸) | `center`, `space-between`, `flex-end` | 横方向の配置 |
| `align-items`     | 縦方向(交差軸)   | `center`, `flex-start`, `flex-end`    | 縦方向の整列 |

## flex-wrap（折り返し）
構文
```css
flex-wrap: nowrap | wrap | wrap-reverse;
```
説明<br>
Flexbox はデフォルトでは「1行に詰め込む」仕様。<br>
要素が溢れても折り返さないため、<br>
レイアウトが崩れることがある。<br>
flex-wrap を使うと**複数行レイアウト（折り返し）**が可能になる。

| 値             | 説明                                          |
| -------------- | --------------------------------------------- |
| `nowrap`       | 折り返さない（デフォルト）                    |
| `wrap`         | 左→右、上→下 の順で折り返す                   |
| `wrap-reverse` | 左→右、下→上 の順で折り返す（上下が逆になる） |

例文
```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}
```
**注意点**
- 要素が多いカードレイアウトなどで必須の設定。
- wrap を使う場合は gap とセットで使うと整列が安定する。
- wrap と justify-content の組み合わせで整列が変わるので要注意。


## flex-flow（ショートハンド）
構文
```css
flex-flow: <flex-direction> <flex-wrap>;
```
説明<br>
flex-direction と flex-wrap を一括指定するショートハンド。<br>
書く量を減らして可読性も上がる。<br>

例文
```css
.container {
  display: flex;
  flex-flow: row wrap;
}

```
**注意点**
- 順序は direction → wrap の順。
- 片方だけ省略はできるが、省略時はデフォルト値になるので注意。

## gap（要素の間隔）
構文
```css
gap: 値;
```
説明<br>
Flexbox の子要素同士の すき間 を設定する。<br>
これだけで margin を使わずに均等間隔が作れるため、<br>
現在の CSS ではほぼ必須のプロパティ。<br>

例文
```css
.container {
  display: flex;
  gap: 20px;
}
```
**注意点**
- padding や margin よりもレイアウトが安定する。
- column-gap / row-gap も使える。
- Grid でも gap は同じように使える（互換性あり）。

## align-content（複数行の縦方向整列）
構文
```css
align-content: stretch | flex-start | center | flex-end | space-between | space-around | space-evenly;
```
説明<br>
flex-wrap: wrap; が有効なときのみ使える<br>
複数行の縦方向（交差軸）の整列。<br>
※ 1行しかないときはまったく効かない。<br>

| 値            | 説明                                 |
| ------------- | ------------------------------------ |
| stretch       | 行を縦方向に引き伸ばす（デフォルト） |
| flex-start    | 上に寄せる                           |
| center        | 中央寄せ                             |
| flex-end      | 下に寄せる                           |
| space-between | 行と行の間を等間隔                   |
| space-around  | 行の上下にも半分のスペース           |
| space-evenly  | 全方向を完全に均等                   |

例文
```css
.container {
  display: flex;
  flex-wrap: wrap;
  align-content: center;
  height: 300px;
}
```
**注意点**
- 要素が複数行にならないと絶対に効かない。
- align-items と混同しない（align-items は「行の中の要素」）。
- 行をまとめて整列するイメージで使う

## Flexbox：子要素のプロパティ
構文
```css
/* 子要素に指定 */
.item {
  flex-grow: 値;
  flex-shrink: 値;
  flex-basis: 値;
  order: 値;
  align-self: 値;
}
```
これらのプロパティは、<br>
親要素に display: flex; が設定されているときだけ有効になります。<br>
説明<br>
Flexbox の子要素(＝フレックスアイテム)は、<br>
親要素が決めた整列方向に沿って、サイズ配分・並び順・位置を調整できます。<br>
| プロパティ    | 概要                     | 主な用途                    |
| :------------ | :----------------------- | :-------------------------- |
| `flex-grow`   | 空きスペースの「伸び率」 | 均等割りや比率配置          |
| `flex-shrink` | 幅が狭いときの「縮み率」 | レスポンシブ対応            |
| `flex-basis`  | 要素の基準サイズ         | 初期幅(px, %, autoなど)指定 |
| `order`       | 並び順の変更             | 配置の入れ替え              |
| `align-self`  | 特定の子要素だけ位置変更 | 個別の縦位置調整など        |

例文(子要素の設定)
```css
/* 親要素 */
.container {
  display: flex;
  justify-content: space-between;
}

/* 子要素 */
.item {
  background-color: lightblue;
  padding: 10px;
}

/* 子要素の個別設定 */
.item1 {
  flex-grow: 1; /* 空きスペースを均等に広げる */
}

.item2 {
  flex-grow: 2; /* item1 の2倍の幅を取る */
}

.item3 {
  flex-basis: 150px; /* 初期幅を150pxにする */
}
```
説明<br>
- .container は親(Flexコンテナ)。
- .item1, .item2, .item3 は子要素。
- flex-grow で空きスペースを分配、flex-basis で初期サイズを設定。<br>
## Flexbox：子要素の各プロパティ詳細
### flex-grow(空きスペースの伸び率)
| 値              | 意味                               |
| :-------------- | :--------------------------------- |
| `0`(デフォルト) | 空きスペースを拡大しない           |
| `1`             | 残りの空間を均等に分配             |
| `2` 以上        | 値の比率で分配(例：1,2 → 1:2 の比) |
例文
```css
.item1 { flex-grow: 1; }
.item2 { flex-grow: 2; }
```
`→ .item2 は .item1 の2倍の幅になる。`
### flex-shrink(縮小率)
| 値              | 意味                     |
| :-------------- | :----------------------- |
| `0`             | 親が狭くなっても縮まない |
| `1`(デフォルト) | 自動で縮む               |
| `2` 以上        | 他の要素より早く縮む     |
例文
```css
.item1 { flex-shrink: 0; } /* 幅を固定したい要素に使う */
```
### flex-basis(基準サイズ)
| 値                 | 意味                   |
| :----------------- | :--------------------- |
| `auto`(デフォルト) | 内容やwidthに合わせる  |
| `px`, `%` など     | 固定の基準サイズを指定 |
例文
```css
.item {
  flex-basis: 200px;
}
```
`→ それぞれの要素がまず200pxで配置され、空きスペースがあれば flex-grow の比率で伸びる。`
### order(並び順)
| 値              | 意味                     |
| :-------------- | :----------------------- |
| `0`(デフォルト) | 通常のHTML順             |
| 正の数          | 数字が大きいほど後に配置 |
| 負の数          | 数字が小さいほど前に配置 |
例文
```css
.item3 { order: -1; } /* item3を先頭に表示 */
```
### align-self(個別の縦位置調整)
| 値                                               | 意味                      |
| :----------------------------------------------- | :------------------------ |
| `auto`(デフォルト)                               | 親の `align-items` を継承 |
| `flex-start` / `center` / `flex-end` / `stretch` | 個別調整                  |
例文
```css
.item3 {
  align-self: flex-end; /* この要素だけ下寄せ */
}
```
### flex(ショートハンド)
flex は、以下3つのプロパティをまとめて書けるショートハンドです。
```css
flex: [flex-grow] [flex-shrink] [flex-basis];
```
**よく使われる省略パターン**
| 書き方        | 展開後の意味      | よく使う場面                 |
| :------------ | :---------------- | :--------------------------- |
| `flex: 1;`    | `flex: 1 1 0%;`   | すべての子要素を均等に伸ばす |
| `flex: auto;` | `flex: 1 1 auto;` | 内容を基準にしつつ、伸縮可   |
| `flex: none;` | `flex: 0 0 auto;` | サイズ固定(伸び縮みしない)   |
**注意点**
- 親に display: flex; がないと効果なし。
- flex は3つを同時に書けるけど、1つでも省略すると既定値が自動で補われる。
- 実務ではほとんどの場合 flex: 1; または flex: auto; の2種類で十分。

### Flexbox：子要素の各プロパティまとめ
| プロパティ    | 対象   | 内容                                 |
| :------------ | :----- | :----------------------------------- |
| `flex-grow`   | 子要素 | 空きスペースの拡大比率               |
| `flex-shrink` | 子要素 | 縮小時の比率                         |
| `flex-basis`  | 子要素 | 初期幅(基準サイズ)                   |
| `order`       | 子要素 | 並び順の変更                         |
| `align-self`  | 子要素 | 個別の縦位置調整                     |
| `flex`        | 子要素 | grow / shrink / basis をまとめて指定 |

## Flexbox 応用編(複数行,中央揃え,等間隔配置) 

構文(親要素に指定)
```css
.container {
  display: flex;
  flex-wrap: wrap;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  gap: 10px;
}
```
説明<br>
Flexboxの応用では、<br>
子要素の数やサイズが変わっても自動的に整列を保つように設定します。<br>
代表的なパターンは以下の5つ👇<br>
| パターン           | 主なプロパティ                                  | 用途例                     |
| :----------------- | :---------------------------------------------- | :------------------------- |
| **中央揃え**       | `justify-content: center; align-items: center;` | ページ中央にボックスを配置 |
| **均等配置**       | `justify-content: space-between;`               | メニュー項目などの均等割り |
| **複数行折り返し** | `flex-wrap: wrap;`                              | カードや画像が多いとき     |
| **縦並び**         | `flex-direction: column;`                       | フォームや縦ナビ           |
| **間隔調整**       | `gap: 値;`                                      | 要素同士のスペース確保     |

例文(親要素の設定)<br>
### 横方向の中央揃え
```css
.container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 200px;
  background: #eef;
}
```
説明<br>
- 中央に子要素を1つまたは複数配置。
- 親要素の中央にきれいに揃う。

### 均等配置（ナビメニューなど）
```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background: #dde;
  padding: 10px;
}
```
説明<br>
- 子要素を左右端に配置し、間を均等に空ける。
- ヘッダーナビゲーションなどでよく使用。

### 複数行に折り返し
```css
.container {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.item {
  width: 100px;
  height: 100px;
  background: lightgreen;
}
```
説明<br>
- 子要素が親の幅を超えると自動的に改行して次の行に配置。
- グリッド風のレイアウトが簡単に作れる。

### 縦方向に並べる
```css
.container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 5px;
}
```
説明<br>
- flex-direction: column; にすると、要素が縦に積み上がる。
- 縦メニューやフォームなどに便利。

### 要素間に一定のすき間を作る
```css
.container {
  display: flex;
  gap: 20px;
}
```
説明<br>
- gap で、すべての子要素の間に同じ間隔を作る。
- margin を個別に設定するよりシンプル。

**注意点**
- gap は 親要素に指定する（margin とは異なる）。
- flex-wrap: wrap; を使うとき、親の幅を超えた要素は自動で改行される。
- flex-direction: column; にすると、justify-content と align-items の意味が縦横で逆転する点に注意。<br>
 `（justify-content が縦方向、align-items が横方向になる）`

### Flexbox 応用編(複数行,中央揃え,等間隔配置) まとめ
| プロパティ        | 内容                 | よく使う場面             |
| :---------------- | :------------------- | :----------------------- |
| `flex-wrap`       | 折り返し制御         | カード・画像一覧         |
| `flex-direction`  | 並びの方向（横or縦） | ナビゲーション・フォーム |
| `justify-content` | メイン軸の整列       | 左右中央・均等配置       |
| `align-items`     | 交差軸の整列         | 縦方向中央など           |
| `gap`             | 要素間の間隔         | 均一な余白配置           |

## Flexbox 子要素の注意点（実務でよくある落とし穴）
**注意点**
- **flex-basis は width より優先される**<br>
`flex-basis: auto; のとき width が使われるが、`<br>
`数値で指定すると width を上書きする。`

- **flex-shrink のデフォルト 1 は危険**<br>
`狭い画面で勝手に縮むので、固定したい要素には`<br>
`flex-shrink: 0; をつける必要がある。`

- **order はあくまで見た目だけ**
`DOM（HTML の順番）は変わらないため、`<br>
`スクリーンリーダーや SEO には影響しない。`<br>

- **align-self は親の align-items を上書きする**<br>
`子単体の位置だけ変えたい場合にだけ使う。`

- **flex: 1; は “均等幅” の意味で使われがちだが、正確には flex: 1 1 0%**<br>
`初期幅が 0 なので、「余白だけで均等割り」になる。`<br>

- **margin: auto; は子要素1つだけの中央寄せが可能**<br>
`Flexbox では margin が “軸方向にも” 効く特殊な仕様。`<br>

| 落とし穴                 | 原因                          | 対策                           |
| ------------------------ | ----------------------------- | ------------------------------ |
| 要素が勝手に縮む         | `flex-shrink: 1` がデフォルト | shrink: 0 を設定               |
| 幅が思い通りにならない   | flex-basis が width を上書き  | width を使うときは basis: auto |
| 子要素の順番が変わらない | order は視覚だけ操作          | HTML 順序は変更不可            |
| 中央揃えできない         | align-items だけで足りない    | margin: auto を併用            |

