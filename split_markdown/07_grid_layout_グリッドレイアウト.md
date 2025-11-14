# 07_grid_layout_グリッドレイアウト（導入）
## Grid Layout とは？
**Grid（グリッドレイアウト）** とは、<br>
「2次元（縦 × 横）のマス目構造で要素を配置できるレイアウトシステム」 のことです。<br>
Flexbox が 1次元（横一列 or 縦一列） に強いのに対して、<br>
Grid は 行（row）と列（column）の両方を同時に扱うのが最大の特徴です。<br>

**Flex と Grid の決定的な違い**
| 項目           | Flexbox                                  | Grid                                     |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| レイアウト構造 | 1次元（横 or 縦）                        | 2次元（縦 × 横）                         |
| 要素の位置決定 | 流れ（並ぶ順番）に依存                   | 行・列を指定して配置できる               |
| 得意分野       | ナビゲーション、ボタン列、コンテンツ並び | ページ全体の構造、複数カラム、カード一覧 |
| gap の扱い     | 行方向のみ（wrapした場合は両方）         | 行・列どちらも gap 指定が直感的          |

- Flex は “流れのあるUI” 向け
- Grid は “構造をつくるUI” 向け<br>
という意識で使い分けると分かりやすい。

## Grid の基本構成
Grid を使うには、まず 親要素に display: grid; を指定する ところから始まる。
```css
.container {
  display: grid;
}
```
そして Grid を構成するのは以下の2つ：<br>
**1. 列（columns）**<br>
横方向の分割。<br>
例：3つのカラム → grid-template-columns<br>

**2. 行（rows）**
縦方向の分割。<br>
例：2つの行 → grid-template-rows<br>

この 行・列のサイズ指定 が、Grid レイアウトの基礎そのもの。

## **Grid が直感的と言われる理由**
Grid には、レイアウトを作りやすくする特有の概念がたくさんある：<br>
- fr（残り空間を「比率」で割る）
- repeat()（パターンの反復）
- auto-fit / auto-fill（自動で埋める）
- 行・列方向の gap
- 明示的グリッド / 暗黙的グリッド（implicit grid）<br>

`これらを押さえると、複雑なレイアウトがコード数行で実現できるようになる。`

# 07_grid_layout_グリッドレイアウト（基本構文）
## Grid の基本構文（columns / rows / gap）
**基本構文とは？**
Grid レイアウトは、親要素に display: grid; を設定し、<br>
行（rows）と列（columns）をどのように区切るかでレイアウトを作る。<br>
```css
.container {
  display: grid;
  grid-template-columns: 200px 200px 200px;
  grid-template-rows: 100px 100px;
}
```
### grid-template-columns（列の定義）
**grid-template-columns（列幅を定義するプロパティ）**<br>
説明<br>
`grid-template-columns` は **Grid レイアウトにおける「列（Column）」の幅を定義するプロパティ**。<br>
値をスペース区切りで並べることで、何列構成か・各列がどれくらいの幅かを決める。<br>

構文<br>
```css
grid-template-columns: 値 値 値 ...;
```

**属性一覧（使用できる主な値）**
| 値         | 説明                                     | 基準                           | 主な用途                               |
| :--------- | :--------------------------------------- | :----------------------------- | :------------------------------------- |
| `px`       | 固定幅（ピクセル指定）                   | 親要素の幅                     | 固定レイアウト、カード幅を揃える       |
| `%`        | パーセンテージで指定                     | 親要素の幅                     | 比率での列幅調整                       |
| `fr`       | 空きスペースを比率で分配する             | 親要素（残り幅）               | 可変レイアウト、等分カラム             |
| `auto`     | 中身（コンテンツ）の幅に合わせて自動調整 | コンテンツの最適幅             | テキスト量による自然な調整             |
| `minmax()` | 指定した最小〜最大の幅で伸縮             | 設定した範囲                   | レスポンシブ対応、幅の下限・上限設定   |
| `repeat()` | 列幅のパターンを繰り返す                 | 指定した回数（または自動計算） | 規則的な複数カラム（例：3列・4列など） |

例文<br>
`grid-template-columns` の代表的な例の実際の描画は  
**[サンプル（grid-columns-demo.html）]**(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-columns/grid-columns-demo.html) を参照。

**このデモでは次のパターンをまとめて確認できる：**
- 1fr 1fr 1fr（3列を等分）<br>
`→ 横幅を均等に3分割する基本パターン。`
- 200px 1fr（固定幅＋可変幅）<br>
`→ サイドバー＋メインの典型レイアウト。`
- 150px 150px 150px（固定3列）<br>
`→ 幅を揃えたいカード一覧などに使用。`
- auto 1fr（自然幅＋可変幅）<br>
`→ ラベル＋テキスト入力などで自然に幅が決まる。`
- minmax(150px, 1fr) 1fr（最小〜最大範囲で伸縮）<br>
`→ 小さい画面では潰れず、大きい画面では余裕をもって伸びる。`
- repeat(3, 1fr)（等分3列の省略形）<br>
`→ 同じ指定を簡潔に書ける。`
- repeat(auto-fill, minmax(150px, 1fr))（※のちの節で詳細）<br>
`→ 画面幅に応じて列数が自動的に増減（レスポンシブの基本）。`
- repeat(auto-fit, minmax(150px, 1fr))（※のちの節で詳細）<br>
`→ 空きスペースを埋めるように配置（より柔軟なレスポンシブ）。`

**注意点（よくあるミス）**
- **列数は「値の数」で決まる**
`→ 値が3つなら3列。repeat で生成する場合はその回数。`
- **fr は残りスペースの割合**
`→ px や auto を先に引いた後の残りを分配する方式。`
- **親幅が決まっていないと fr が働かない**
`→ width: 100% または max-width をよくセットで利用。`
- **auto と fr を混ぜると auto が優先される**
`→ auto が必要幅を取り、残りを fr が受け取る。`

## grid-template-rows（行の定義）
### grid-template-rows（行高の定義）
説明<br>
`grid-template-rows` は **Grid の「行（Row）」の高さを定義するプロパティ**。<br>
値をスペース区切りで並べることで、何行構成か・各行の高さを決める。<Br>
構文<br>
```css
grid-template-rows: 値 値 値 ...;
```
**属性一覧（使用できる主な値）**
| 値         | 説明                               | 基準                | 主な用途                               |
| :--------- | :--------------------------------- | :------------------ | :------------------------------------- |
| `px`       | 行の高さを固定値で指定             | 親要素の高さ        | 固定ヘッダー・フッター                 |
| `%`        | パーセンテージで指定               | 親要素の高さ        | 比率で高さを調整                       |
| `fr`       | 空きスペースを比率で配分（縦方向） | 親要素（残り高さ）  | 可変高さレイアウト                     |
| `auto`     | コンテンツに合わせて高さを自動調整 | コンテンツの高さ    | テキスト量に応じた自然な行配置         |
| `minmax()` | 最小〜最大の範囲で高さを伸縮       | min〜max の指定範囲 | レスポンシブ、高さが潰れないようにする |
| `repeat()` | 同じ行パターンを繰り返す           | 指定回数            | 均一行の複数生成                       |

例文<br>
`grid-template-rows` の代表的な例の実際の描画は  
**[サンプル（grid-rows-demo.html）]**(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-rows/grid-rows-demo.html) を参照。

**このデモでは次のパターンをまとめて確認できる：**
- 80px auto 80px（固定行）
- 1fr 1fr 1fr（等分3行）
- 100px 100px 100px（固定3行）
- auto 1fr（自然高さ＋可変）
- minmax(120px, auto) 1fr

repeat(4, 1fr)
**注意点（Rowsで起こりやすいミス）**
- 親要素の高さがないと fr は働かない<br>
`→ height: 100vh; や height: 100% が必要。`
- auto は “最低限必要な高さ” を取る<br>
`→ テキストが長いと伸びる。`
- minmax の max に auto を使うと伸縮が自然になる<br>
`→ recommended：minmax(100px, auto)。`
- % の基準は親の高さ<br>
`→ 親に高さ指定がないと計算できない。`

## gap（行・列の間隔）
説明<br>
gap は Grid で行（row）・列（column）同士のすき間（間隔）を設定するプロパティ。<br>
Flexbox にも存在するが、Grid では「行×列」の両方向に働くため、<br>
レイアウト全体の見やすさ・均整を整えるうえで非常に重要。<br>
- gap：行と列の両方を同じ値で指定
- row-gap：行だけ
- column-gap：列だけ
- 複数値（例：gap: 20px 40px）で「行 20px、列 40px」という指定も可能

構文
```css
gap: 値;
row-gap: 値;
column-gap: 値;
gap: 行 列;
```
**属性一覧（使用できる主な値）**
| 値       | 説明                         | 主な用途                                 |
| :------- | :--------------------------- | :--------------------------------------- |
| `px`     | 固定のスペースを指定         | 最も一般的。カード・画像・フォームなど。 |
| `rem/em` | フォント基準のスペースを指定 | 文字サイズと連動した余白調整             |
| `%`      | 親要素に対する割合で設定     | レスポンシブだが計算が難しいので非推奨   |
| `0`      | すき間なし                   | 隣接グリッドを隙間なく並べたい場合       |

例文<br>

`grid-gap` の代表的な例の実際の描画は  
**[サンプル（grid-gap-demo.html）]**(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-gap/grid-gao-demo.html) を参照。

**このデモでは次のパターンをまとめて確認できる：**
- gap: 12px;（行・列同じ）
- row-gap: 20px; column-gap: 40px;（行と列で別々）
- gap: 0;（隙間なし）
- gap: 16px 40px;（行 16px / 列 40px）
- 大量要素のカードグリッド（gapあり・なし比較）

**注意点（よくあるミス）**
- **margin と混同しがち**<br>
`→ gap は「Grid 内のセル同士の間隔」`<br>
`→ margin は「要素自身の外側の余白」`<br>
- **gap は親要素に設定する**<br>
`→ 子要素では動作しない。`<br>
- **gap が効くのは Grid（とFlex）だけ**<br>
`→ block 要素の行間には使えない。`<br>
- **行列ごとの gap が必要なら複数値を使う**<br>
`→ gap: 行 列; の形式を覚えておくと便利。`<br>

## fr と repeat()※Grid の “心臓部”
説明<br>
**● fr（fraction：比率による配分）**<br>
**`fr`** は **`Grid の残りスペースを比率で分配する単位`**。<br>
レイアウトの柔軟性を最大限に引き出す Grid の “心臓部” ともいえる概念。<br>
- 1fr 1fr → 残り幅を 1:1 で分割
- 2fr 1fr → 残り幅を 2:1 で分割
- auto や px で確保された幅を引いた「残り」を比率で分ける

`Flex の flex-grow と似ているが、Grid は面全体で割り付けるため精度が高い。`

## ● repeat()（繰り返し生成）
説明<br>
**`repeat()`** は **`同じパターンを複数回繰り返す記述を簡潔に書く関数`**。<br>
例：
```css
repeat(3, 1fr)
/* ↑ と ↓ は同じ意味 */
1fr 1fr 1fr
```
**主に以下の2つの用途で使う：**<br>
- 固定回数の繰り返し（例：repeat(4, 1fr)）
- auto-fill / auto-fit と併用したレスポンシブ<br>
`（例：repeat(auto-fit, minmax(150px, 1fr))）`

構文
```css
/* fr */
grid-template-columns: 1fr 2fr 1fr;

/* repeat */
grid-template-columns: repeat(3, 1fr);

/* auto-fill / auto-fit による応用 */
grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
```
**属性（fr / repeat の挙動の特徴）**
| 機能                | 説明                                       | 主な用途                          |
| :------------------ | :----------------------------------------- | :-------------------------------- |
| `fr`                | 残りスペースを比率で分配                   | 等分・比率分割・自動伸縮          |
| `auto`              | 内容量に応じて必要最小限の幅を確保         | ラベル＋本文、自然幅の表現        |
| `px / % `           | 固定・比率ベースの絶対指定                 | 枠を揃えたいとき                  |
| `repeat(n, 値)`     | 指定した値を n 回繰り返す                  | 等分カラム、均一なカード一覧      |
| `repeat(auto-fill)` | 可能な限り列を詰めて生成する（空セル含む） | レスポンシブカード（Pinterest風） |
| `repeat(auto-fit)`  | 空きを吸収してセルが伸びる（隙間が埋まる） | 伸びるレスポンシブレイアウト      |

例文<br>
`grid-gap` の代表的な例の実際の描画は  
**[サンプル（grid-gap-demo.html）]**(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-gap/grid-gao-demo.html) を参照。

**このデモでは次のパターンをまとめて確認できる：**
- 1fr 1fr 1fr（等分）
- 2fr 1fr（比率レイアウト）
- 1fr 2fr 1fr（センター強調レイアウト）
- repeat(3, 1fr)（3等分）
- repeat(4, 150px)（固定4列）
- repeat(3, auto)（自然幅の繰り返し）
- repeat(5, minmax(100px, 1fr))（柔軟カラム）
- repeat(auto-fill, minmax(150px, 1fr))（グリッド自動生成・空セルあり）
- repeat(auto-fit, minmax(150px, 1fr))（空きを吸収して伸びる）<br>

**注意点（fr / repeat の落とし穴）**
- **fr は必ず“残りスペース”が対象**<br>
`→ px や auto で確保された幅は fr に割り当てられない。`<br>

- **auto + fr は auto が優先**<br>
`→ まず auto が必要分だけ確保 → 余りを fr に配分。`<br>
- **auto-fill と auto-fit の違いは“空き枠が残るかどうか”**<br>
  - `fill → 空セルを残す（枠が詰まって見える）`
  - `fit → セルが伸びて空きを埋める`
- **minmax と fr を組み合わせると強力だが挙動が複雑**<br>
`→ デモで視覚的に理解するのが一番。`<br>

## auto-fill と auto-fit（レスポンシブカラムの自動生成）
説明<br>
`auto-fill` と `auto-fit` は、<br>
**`画面幅に応じてカラム数を自動で増減させる仕組み`** を作るためのキープロパティ。
- どちらも repeat() と組み合わせて使用する
- どちらも minmax() と併用するのが基本
- どちらも「レスポンシブカード」を作るときに多用される<br>
見た目は似るが、決定的な違いは **`“空きスペースの扱い”`** にある。

**● auto-fill（空セルを残すタイプ）**<br>
**可能な限りカラムを詰めて生成するが、空き枠もそのまま残す。**<br>
- 余ったスペースがあっても、セルは伸びない
- 空セルが存在するため 「詰まった格子」 のような見た目になる
- Pinterest や画像一覧のような、枠がきっちり揃うタイプに向く

**● auto-fit（空きを吸収するタイプ）**<br>
**余ったスペースを吸収し、セルが伸びてフィットする。**<br>
- 空セルが“潰れる（幅0扱い）” → 実質的に見えなくなる
- セルが横に伸び、隙間が埋まってフラットに揃う
- グリッド全体がきれいにフィットするため、カードレイアウト向き

構文<br>
```css
/* auto-fill：空セルを含めて詰める */
grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));

/* auto-fit：空セルを潰してフィットさせる */
grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
```
**属性一覧（特徴まとめ）**
| 概念        | 説明                                           | 主な用途                             |
| ----------- | ---------------------------------------------- | ------------------------------------ |
| `auto-fill` | 空セルを含めてできる限り詰める（枠が残る）     | Pinterest 風の一覧、詰まったグリッド |
| `auto-fit`  | 空セルを潰して要素を伸ばし、余白を埋める       | カードレイアウト、自然なレスポンシブ |
| `minmax()`  | 最小～最大の幅を確保しつつ柔軟に伸縮           | 小さい画面で潰れない設計に必須       |
| `1fr`       | 余ったスペースを割り当てる（auto-fit と相性◎） | レスポンシブでバランスよく配置       |

例文
`auto-fill` / `auto-fit` の代表的な例の実際の描画は
**[サンプル（grid-autofill-fit-demo.html）]**(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-autofill-fit/grid-autofill-fit-demo.html) を参照。

**このデモでは次のパターンをまとめて確認できる：**
- repeat(auto-fill, minmax(150px, 1fr))（空セルあり）
- repeat(auto-fit, minmax(150px, 1fr))（空き吸収でフラット化）
- カードの数を少なくしたときの挙動比較
- ウィンドウ幅を縮めたときの列数の変化比較
- minmax の最小幅を変更したときの変化<br>
`（例：minmax(200px, 1fr)）`

**注意点（よくあるミス）**<br>
- **minmax の最小値が小さすぎると、カードが潰れる**<br>
`→ 150px〜200px が実用的な基準。`<br>
- **auto-fill と auto-fit を“見た目だけ”で判断しないこと**<br>
`→ ウィンドウ幅を広げたときに差が最も明確に出る。`<br>
- **auto-fit はセルが伸びるため、画像比率に注意**<br>
`→ 高さ固定カードとの併用が良い。`<br>
- **auto-fill は「見えない空き枠」が残りやすい**<br>
`→ グリッドの左右に余白が見える場合がある。`<br>


## justify-content / align-content（Grid 全体の揃え）
説明<br>
`justify-content` と `align-content` は、<br>
**`Grid 全体（グリッド領域そのもの）を親要素の中でどう揃えるか`** を指定するプロパティ。
- justify-content → **横方向（行方向）** にグリッド領域を揃える
- align-content → **縦方向（列方向）** にグリッド領域を揃える

ここで操作するのは **各セルではなく“グリッド全体の塊”** である点が重要。<br>
また、これらのプロパティが機能するのは、<br>
- **親要素に余白（空きスペース）があるときだけ**
- グリッドの「行数・列数」が固定されている場合に有効<br>

という制約があるため、挙動の理解にはデモが必須。

構文
```css
/* 横方向（左・右・中央・等間隔など） */
justify-content: start | end | center | stretch | space-between | space-around | space-evenly;

/* 縦方向（上・下・中央・等間隔など） */
align-content: start | end | center | stretch | space-between | space-around | space-evenly;
```
**属性一覧（共通）**
| 値              | 説明                                           | 見た目の特徴               |
| --------------- | ---------------------------------------------- | -------------------------- |
| `start`         | 余白を使って **先頭側に寄せる**                | 左寄せ（横）・上寄せ（縦） |
| `end`           | 余白を使って **終端側に寄せる**                | 右寄せ（横）・下寄せ（縦） |
| `center`        | 余白を使って **中央に配置する**                | 真ん中に寄る               |
| `stretch`       | **余白をすべて使ってグリッド領域を引き伸ばす** | 広がってフィットする       |
| `space-between` | **両端はくっつけて内部だけ等間隔**             | 端がそろい、中だけ等間隔   |
| `space-around`  | 要素の **外側にも均等に余白**                  | ふんわり均等               |
| `space-evenly`  | **全ての間隔が完全に均等**                     | 最も均等な分布             |

例文<br>
`justify-content` / `align-content` の代表的な例の実際の描画は  
**[サンプル（grid-content-demo.html）]**(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-content/grid-content-demo.html) を参照。

このデモでは次のパターンをまとめて確認できる：<br>
- justify-content: start / center / end
- justify-content: space-between / space-around / space-evenly
- align-content: start / center / end
- align-content: space-between / space-around / space-evenly<br>
`※ デモでは「グリッド領域そのものが動く」ことが分かるように`<br>
`親要素の高さ・幅を固定して表示します。`

**注意点（Grid 特有のポイント）**
- **セルの揃え（justify-items / align-items）とは異なる**<br>
`→ 今回のプロパティは “グリッド全体” を動かす。`<br>
- **余白がない状態では何も変わらない**<br>
`→ グリッドの総幅／高さが親要素いっぱいの場合は無効。`<br>
- **stretch がデフォルトになるケースを理解する**<br>
`→ 多くの Grid は stretch で広がるため、中央揃えを期待しても変化がないことがある。`<br>
- **多段の Grid（複数行・複数列）で効果が分かりやすい**<br>
`→ 行数や列数が固定されているレイアウトで明確。`<br>

## justify-items / align-items（セル内部の揃え）
説明<br>
`justify-items` と `align-items` は、<br>
**`Grid の各セル内で子要素をどう揃えるか`** を指定するプロパティ。<br>
- `justify-items` → 横方向（行方向）の揃え
- `align-items` → 縦方向（列方向）の揃え<br>
また、セルごとに個別に揃えを変えたい場合は：
- justify-self
- align-self<br>

を使用する。
これらは「セルの内部」にフォーカスしており、<br>
`justify-content` / `align-content` のような グリッド全体の揃えとは異なる。

**content 系（グリッド全体の揃え）とは目的が異なる**ため注意。<br>
今回扱う items 系はあくまで **セルの中の1つ1つの要素** をどう揃えるかを制御する。<br>

構文<br>
```css
/* セル内部の揃え（横方向） */
justify-items: start | center | end | stretch;

/* セル内部の揃え（縦方向） */
align-items: start | center | end | stretch;

/* 個別セルごとの上書き */
justify-self: start | center | end | stretch;
align-self: start | center | end | stretch;
```
**属性一覧**
| 値        | 説明                                                   | 主な用途                       |
| --------- | ------------------------------------------------------ | ------------------------------ |
| `start`   | セル内の先頭側に寄せる（左寄せ / 上寄せ）              | ラベル類の整列                 |
| `center`  | セル内で中央揃え                                       | アイコン・ボタンのセンタリング |
| `end`     | セル内の終端側に寄せる（右寄せ / 下寄せ）              | 小要素を端に寄せる UI          |
| `stretch` | セルの幅・高さいっぱいに要素を引き伸ばす（デフォルト） | カード・ボックスUIの基本       |

例文<br>
`justify-items` / `align-items` の代表的な例の実際の描画は
[サンプル（grid-items-demo.html）](https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-items/grid-items-demo.html
) を参照。

`このデモでは次のパターンをまとめて確認できる：`<br
- justify-items: start / center / end / stretch
- align-items: start / center / end / stretch
- 横方向 × 縦方向のペア（例：center × center）
- justify-self / align-self による個別セルの上書き

**注意点**
- **content 系（グリッド全体）との違いが最重要**
  - items 系 → セル内部
  - content 系 → グリッド全体
- **stretch は意図しない広がりを生みやすい**<br>
`→ ボタンサイズなどは明示的に center を指定する`<br>
- **セルのサイズ依存で見た目が変わる**<br>
`→ 余白の大きいセルでは差が明確だが、狭いセルでは差が小さく見える`<br>
- **セル個別指定（self）が一番強い優先度**<br>
`→ 特定の位置だけずらしたいときに使用`<br>









## Grid 応用レイアウト（実践パターン）
**1. カードレイアウト（基本）**
- **grid-template-columns: repeat(auto-fill, minmax())**
- カード一覧によく使われる
- レスポンシブの基礎（幅に応じて行数変動）
**2. 2カラム・3カラム レイアウト**
- 固定幅 + 1fr
- サイドバー付きページ構成
- 新聞風3カラム
**3. 完全レスポンシブ化**
- minmax + auto-fit / auto-fill
- ブレークポイントを使わないレスポンシブ
- 画面幅に応じて自然に崩れるグリッド
**4. よくある UI パターン**
- ダッシュボードタイル
- 商品一覧レイアウト
- 管理画面のパネル配置

## カードレイアウト（Grid 応用）
説明<br>
カードレイアウトは、Webサイトの `商品一覧・ブログ一覧・ギャラリー・メディアカード` などで最もよく使われるレイアウト。<br>

`Grid` を使うと：<br>
- カード幅を 最小値〜最大値の範囲で自動調整
- 画面幅に応じて 列数が自然に増減
- メディアクエリなしで レスポンシブ対応<br>
…といった実装が非常に簡単になる。<br>
この節では、最もよく使われる次の構文を扱う：<br>
```css
grid-template-columns: repeat(auto-fill, minmax(○○, 1fr));
```
構文<br>
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 16px;
}
```
説明（深入り）<br>
| 構文                   | 役割                                                       |
| ---------------------- | ---------------------------------------------------------- |
| `repeat(auto-fill, …)` | コンテナ幅に入るだけカードを詰め込む（空き枠も作る）       |
| `repeat(auto-fit, …)`  | カード同士が自動的に広がり、空き枠を埋める                 |
| `minmax(200px, 1fr)`   | カード最小幅 200px を維持しつつ、余白があれば 1fr で伸びる |
| `gap: 16px;`           | カードの間隔を取る                                         |

例文<br>

カードレイアウト（Grid 応用） の代表的な例の実際の描画は
[サンプル（grid-card-demo.html）](https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-card/grid-card-demo.html) を参照。

`このデモでは次のパターンをまとめて確認できる：`<br>
- minmax(200px, 1fr) を使ったカードグリッド
- auto-fill と auto-fit の違い
- 画面幅による列数の増減
- カードの高さ固定／可変の違い

**注意点**<br>
- **カード幅を固定しない**<br>
`→ 固定幅にするとレスポンシブ性が失われる。`<br>
- **auto-fill と auto-fit の違いを理解すること**<br>
  - auto-fill：空き枠が残る<br>
  - auto-fit：カードが自動で伸びて空き枠を埋める<br>
- **minmax の最小値が重要**<br>
`→ 小さすぎるとスマホで崩れる`<br>
`→ 大きすぎると2列維持が困難`<br>
- **カード内のテキスト量が多いと高さが揃わない**<br>
`→ align-items: start を積極的に使う`<br>

## 2カラム・3カラム レイアウト（Grid 応用）
**1. 固定幅 + 可変幅（サイドバー＋メイン）**
```css
grid-template-columns: 240px 1fr;
```
**2. 2カラムの等分**
```css
grid-template-columns: 1fr 1fr;
```
**3. 3カラムレイアウト**
```css
grid-template-columns: 1fr 1fr 1fr;
```
**そして実務でよくある UI 例：**<br>
- サイドバーを固定 & メインを可変
- 3カラムニュース一覧
- 複数パネルの管理画面レイアウト
- 左ナビ固定・右メイン自動拡大<br>

## 2カラム・3カラム レイアウト<br>
説明<br>
Webページのレイアウトで最も頻出するのが `2カラム（左右）` と `3カラム（3分割）` の構成。<br>
Grid を使うと以下のような実装が非常に単純になる：<br>
- 左固定幅＋右可変幅（よくあるサイドバー＋メイン）
- 可変幅 1fr の 2 分割
- 等幅の 3 カラム（ニュース一覧など）
- 固定幅＋等分の組み合わせ など<br>
`grid-template-columns` を使うだけで直感的に定義でき、<br>
`Flex` では扱いにくい **`左右非対称レイアウト`** も簡単に実装できる。<br>

構文<br>
```css
/* 左固定幅 + 右可変 */
grid-template-columns: 240px 1fr;

/* 2カラム（等分） */
grid-template-columns: 1fr 1fr;

/* 3カラム（等分） */
grid-template-columns: 1fr 1fr 1fr;

/* 3カラム（固定 + 等分） */
grid-template-columns: 200px 1fr 1fr;
```

**値の説明**
| 値                   | 説明                                       |
| -------------------- | ------------------------------------------ |
| `px`                 | 完全固定の幅。サイドバー・広告などに使用   |
| `fr`                 | 余白を均等に分配する Grid 特有の単位       |
| `auto`               | コンテンツサイズに合わせて伸縮             |
| `minmax(a, b)`       | 最小 a、最大 b の範囲でカードやパネル配置  |
| `repeat(n, pattern)` | パターンを n 回繰り返す（3カラム等分など） |

例文<br>
`2カラム・3カラム レイアウト` の代表的な例の実際の描画は<br>
[サンプル（grid-layout-columns-demo.html）]
(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-layout-columns/grid-layout-columns-demo.html) を参照。

`このデモでは次のパターンをまとめて確認できる：`<br>
- 左固定幅（240px）＋右可変（1fr）の 2 カラム
- 1fr × 2 の等分レイアウト
- 1fr × 3 の 3 分割カラム
- 固定幅 + 等分の複合 3 カラム

**注意点**<br>
- **複雑なレイアウトは Flex ではなく Grid を優先する**<br>
  - -Grid：縦＋横の2軸レイアウトが得意<br>
  - Flex：横1軸（または縦1軸）の調整が得意<br>
- **サイドバー幅は固定した方が安定する**<br>
`→ 240px 1fr のような構成が実務でよく使われる。`<br>
- **多段レイアウトは repeat を使うと可読性が上がる**<br>
  - repeat(3, 1fr) は 1fr 1fr 1fr と同じ<br>
  - 読みやすく管理しやすい<br>
- **可変幅（fr）は余白全体に比例する単位**<br>
`→ Flex の flex-grow と似ているが Grid 専用。`<br>

## 完全レスポンシブレイアウト（ブレークポイント不要）
説明<br>
Grid は `minmax()` と `auto-fit` を組み合わせることで、<br>
**`メディアクエリなしで完全レスポンシブ`** なレイアウトを実現できる。<br>

この組み合わせは：<br>
- 画面幅に合わせてカード数が増減
- 自動的に折り返し
- 空き枠は自動で埋まる
- スマホ〜PCまで自然に可変<br>

…という非常に強力な仕組みで、<br>
現代の Web レイアウトでは **最も推奨される構成の1つ。**<br>
```css
grid-template-columns: repeat(auto-fit, minmax(○○px, 1fr));
```
構文<br>
```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 20px;
}
```
**値の説明**
| 値                       | 説明                                                     |
| ------------------------ | -------------------------------------------------------- |
| `auto-fit`               | カードが広がって空き枠を埋める（完全レスポンシブに最適） |
| `minmax(最小値, 最大値)` | カードが確保する最小幅と、広がれる最大幅を指定           |
| `1fr`                    | 余白を均等に分配し、カードを最大限に広げる               |
| `gap`                    | カードの間隔（レスポンシブでも一定のまま扱える）         |

例文<br>

完全レスポンシブレイアウト の代表的な例の実際の描画は
[サンプル（grid-responsive-demo.html）]
(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/grid-responsive/grid-responsive-demo.html)

このデモでは次のパターンをまとめて確認できる：<br>
- auto-fit + minmax の基本構成
- カード幅 240px を下限にしたレスポンシブ変化
- スマホ：1列
- タブレット：2列
- PC：3〜4列
- 余白があるときカードが自然に広がる挙動

### 🔍 注意：DevTools（分割ビュー）では Grid のレスポンシブが正しく発動しません<br>
Chrome DevTools の “分割ビュー（Split view）” は、ページを iframe 内で描画するため、<br>
ページ本体の幅が縮まず、 `auto-fit` や `minmax()` を使った Grid のレスポンシブ挙動が働きません。<br>
**正しく動作を確認するには：**<br>
1. デモページをブラウザで直接開く  <br>
2. DevTools のデバイスツールバーを使う<br>  
   （またはブラウザウインドウ自体を縮める）<br>
この方法で、スマホ〜PC まで自然にカラム数が変化する Grid の挙動を確認できます。<br>

**注意点**<br>
- **minmax の最小値が小さすぎると崩れる**<br>
`→ スマホ基準で 180px〜240px が最適。`<br>
- **カード内のテキスト量に応じて高さが揃わない場合がある**<br>
`→ 実務では align-items: start を併用することが多い。`<br>
- **カードの最大値（1fr）は親幅に依存する**<br>
`→ wrapper や余白の設定で最終的な横幅が決まる。`<br>
- **auto-fill は完全レスポンシブには向かない**<br>
`→ 空き枠を残すため、カードが伸びず不自然な隙間ができる。`<br>

## よくある UI パターン（Grid 実務編）
説明<br>
Grid は、単なる“カードの並び”だけでなく、<br>
**実務の UI レイアウト全般に利用できる強力な仕組み**です。<br>
この節では、実際の Web サイトや管理画面でよく使われる<br>
典型的な UI パターンを Grid を使って再現します。<br>
以下の UI はすべて Grid の基礎だけで作ることができ、<br>
Flex では難しい 複数軸のレイアウト制御が直感的に書けます。<br>

この節で扱うパターンは次の 4 種類：<br>
- ダッシュボード風タイル（Widget / Card）
- 商品一覧レイアウト（EC風カード）
- 管理画面の情報パネル（Admin Panel）
- 画像ギャラリー（等間隔グリッド）

**パターン一覧（説明＋構文）**<br>
**`1. ダッシュボード風タイル`**<br>
管理ツールや社内システムでよく使われるタイル状 UI。<br>
`repeat(auto-fit, minmax())` を使うことで、<br>
小さなカードでも画面幅に合わせて自然に折り返す。<br>
```css
grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
```
例文<br>
`dashboard-grid` の代表的な例の実際の描画は<br>
[サンプル（dashboard-grid-demo.html）]<br>
(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/UIpattern/dashboard-grid-demo.html)を参照。<br>

**`2. 商品一覧レイアウト（ECカード）`**<br>
画像つきの縦型カード UI。<br>
PC では複数列、スマホでは 1 列に変化する。<br>
```css
grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
```
例文<br>
`product-grid` の代表的な例の実際の描画は<br>
[サンプル（product-grid-demo.html）]<br>
(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/UIpattern/product-grid-demo.html)を参照。<br>

**`3. 管理画面の情報パネル（Admin Panel）`**
複数の情報カードを<br>
「大きさの違うカード混在」で配置する典型的パターン。<br>
Grid なら複合サイズが自然に配置できる。<br>
```css
grid-template-columns: repeat(3, 1fr);
```
`admin-panel-grid` の代表的な例の実際の描画は<br>
[サンプル（admin-panel-grid-demo.html）]<br>
(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/UIpattern/admin-panel-grid-demo.html)を参照。<br>

**`4. 画像ギャラリー（正方形・縦横揃え）`**<br>
写真一覧・ギャラリー・サムネイルに最適。<br>
`object-fit: cover` を組み合わせることで実務レベルの仕上がりになる。<br>
```css
grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
```
`gallery-grid` の代表的な例の実際の描画は<br>
[サンプル（gallery-grid-demo.html）]<br>
(https://monzaemon-commits.github.io/html-study-notes/split_markdown/sample/UIpattern/gallery-grid-demo.html)を参照。<br>

**注意点**<br>
- **縦横サイズが混在する場合は Grid が強い**<br>
`Flex では縦方向の整列が難しい。`<br>
- **画像ギャラリーは object-fit: cover が必須**<br>
`→ 画像が縦長・横長でもきれいに揃う。`<br>
- **repeat(auto-fit) / minmax の組み合わせは事実上の標準**<br>
`多くの UI パターンで活用できる。`<br>
- **wrapper を固定幅にするとレスポンシブが壊れる**<br>
`→ デモは原則 wrapper なし（A案）で統一する。`<br>