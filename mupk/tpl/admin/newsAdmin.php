<section>
    <div class="mainImage"><img class="main" src="images/mainImage.jpg"></div>
    <h1>Головна</h1>
    <div class="text">
        <p>Болградський міжшкільний навчально-виробничий комбінат на протязі 34 років є центром допрофесійної
            та професійної  підготовки старшокласників району.
        </p>
        Професії, яким навчають у Болградському МНВК:
        <ul>
            <li>Водій автотранспортних
                засобів” кат. “В”, “С1”</li>
            <li>Штукатур</li>
            <li>Оператор комп’ютерного набору</li>
            <li>Секретар  керівника</li>
            <li>Агент з організації туризму</li>
        </ul>
        <p>З моменту першого випуску у 1979 році і по 2016 рік в Болградському МНВК пройшли навчання більше 6000
            учнів. Отримали першу професію 80% від загальної кількості учнів.</p>
    </div>
</section>
<div class="separator"></div>
<h1>Новини</h1>
<h3><a style="margin-left: 20%" href="?Admin/addForm">Додати новину</a></h3>
<? foreach($this->posts as $value){?>
    <article>
        <header><h3><?=$value['title']?></h3></header><a href="?Admin/delete/<?=$value['id']?>">видалити</a>|<a href="?Admin/editForm/<?=$value['id']?>">редагувати</a>
        <section>
            <p><?=$value['post']?></p><div class="data"><?=date('d-m-Y', $value['ctime'])?></div>
        </section>
    </article>
<?}?>
<div class="separator"></div>
