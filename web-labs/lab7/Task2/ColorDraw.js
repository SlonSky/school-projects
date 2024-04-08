/**
 * Created by F5 on 26.10.2015.
 */

for(var i = 0; i < 10; i++){
    document.write("<tr>");
    for(var j = 0; j < 10; j++){
        var red = Math.round(185.0*Math.random());
        var green = Math.round(185.0*Math.random());
        var blue = Math.round(185.0*Math.random());
        var color = red.toString(16)+green.toString(16)+blue.toString(16);
        document.write("<td bgcolor="+color+">"+color+"</td>");
    }
    document.write("</tr>");
}