<?php $post = $this->db->query("SELECT * FROM posts WHERE id='$this->id'")->assoc(); ?>

<div class="separator"></div>
<section class="postEdit">
    <h1>Відредагувати новину</h1>
    <form action="?Admin/editPost/<?=$this->id?>" method="post">
        <p><label>Заголовок</label><br>
            <input name="title" class="postHeader" type="text" value="<?=$post["title"]?>">
        </p>
        <p><label>Зміст</label><br>
            <textarea name="post" class="postBody">
                <?=$post['post']?>
            </textarea><p>
        <input type="submit" value="Готово">
    </form>
</section>
<div class="separator"></div>