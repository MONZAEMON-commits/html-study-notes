# 05_html_css_link_and_reset(HTMLとCSSの連携について)
## cssのリンクについて
## linkタグについて
`<link>` タグとは？<br>
`<link>` は、HTML と外部リソース（CSS / アイコン / フォントなど）を結びつけるためのタグ。<br>
基本的に `<head>` の中に書く。<br>

構文<br>
```css
<link rel="stylesheet" href="style.css">
```
説明<br>
`<link>` タグは、
`HTML が必要とする外部ファイルを読み込むためのタグ。`<br>
主に使われる用途は次のとおり👇<br>
## link使用例
**外部CSSを読み込む**
```html
<link rel="stylesheet" href="style.css">
```
**Google Fonts を読み込む**
```html
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP&display=swap">
```
**サイトアイコン（ファビコン）の設定**
```html
<link rel="icon" href="favicon.ico">
```
**レスポンシブ用CSSを読み込む**
```html
<link rel="stylesheet" href="mobile.css" media="screen and (max-width: 600px)">
```
補足：レスポンシブってなに？→同じCSSで全端末に画面幅を最適表示するための仕組み<br>
つまり`@media`を使うcssを分けて作成した場合に使用したりするという事。小規模開発ではstyle.cssに纏めちゃう。<br>

## 属性一覧（実務で使うのはここ）
| 属性名    | 意味                              | 例                                      |
| --------- | --------------------------------- | --------------------------------------- |
| **rel**   | リソースとの関係（必須）          | `stylesheet`, `icon`, `preconnect`      |
| **href**  | 読み込むファイルのURL（必須）     | `style.css`                             |
| **type**  | MIMEタイプ（CSSの場合は省略でOK） | `text/css`                              |
| **media** | どの画面サイズ用に適用するか      | `media="screen and (max-width: 768px)"` |
| **sizes** | アイコンのサイズ                  | `sizes="32x32"`                         |


## リセットCSSについて
**リセットCSSとは？**
目的<br>
ブラウザには デフォルトのCSS（標準スタイル） があるため、<br>
- 余白（margin, padding）が勝手についている
- 表示がブラウザごとに微妙に違う
- ボタンや見出しの大きさが統一されない<br>
…という問題が発生します。
これを ゼロ（reset） にして、
「すべてのブラウザで同じスタートラインに立たせる」のが リセットCSS。

## リセットCSSの種類
**大きく分けると2つ👇**
### Reset.css（完全にゼロに戻すタイプ）
例：Eric Meyer’s Reset
- すべての余白・装飾を 完全にリセット
- 何もかも0になるので、自分で全部再指定が必要
- デザイン自由だが、初心者には少し手間

### Normalize.css（自然な初期値を整えるタイプ）
- 完全に0にはしない
- ブラウザごとの表示差を均一にする
- 実務では現在ほぼこちらが主流

### ***結論：迷ったら Normalize.css でOK***
理由<br>
- 実務で98%使われる
- UIが自然に保たれる
- 毎回自分で全部書き直す必要がない
- バグ（変な初期値の違い）を防げる

## 最小限のリセットCSS（実務でよく使う軽量版）
```css
/* ▼ リセットCSS（実務向けの最小構成） ▼ */
/*→ レイアウトが崩れない“世界標準”。*/
*,
*::before,
*::after {
  box-sizing: border-box;
}
/* 全要素の余白をリセットして、自由に設定できるように。 */
html, body, h1, h2, h3, h4, h5, h6,
p, ul, ol, li, figure, blockquote {
  margin: 0;
  padding: 0;
}
/* → <ul> <ol> の黒丸や数字を消す。 */
ul, ol {
  list-style: none;
}
/* → リンクの青色や下線を消す（後で自分で整える）。 */
a {
  text-decoration: none;
  color: inherit;
}
/* → 画像が勝手に横はみ出ししないようにする。 */
img {
  max-width: 100%;
  display: block;
}
/* 文章を読みやすくするための“最低限の行間設定” */
body {
  line-height: 1.5;
}
```
