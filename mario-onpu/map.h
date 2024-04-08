#ifndef MAP_H_INCLUDED
#define MAP_H_INCLUDED
#include <SFML/Graphics.hpp>

#define H 19 // sizeY
#define W 138 // sizeX

using namespace sf;


char TileMap[H][W] =
    {
        "                                                                                                                                         ",
         "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo",
        "                                                                                                                                         ",
        "                                                                                                                                         ",
        "s                               G                                                                                         G              ",
        "s          a                                       a                                                                                     ",
        "s                                                                       a                A                   G                           ",
        "s                        A              a                     A                G                                     A                   ",
        "s  A                                                                                                  A                       a          ",
        "s                               ?2?k           G                                             a                                           ",
        "s                                            3                                                                                           ",
        "s                                                                                                              b         p               ",
        "s                                                                                                             bb             s           ",
        "s                              k??kkk       ?k??k               ?4?k                k?kk1                    bbb             s           ",
        "s                                                       b                                                   bbbb             s           ",
        "s                                         H            bb                       b      H                   bbbbb             s           ",
        "s     C         h             c  e            e g     bbb         C e          bb  e               ce     bbbbbb   g         Q  h  C     ",
        "ffffffffffffffffffff  fffffffffffffffffffffffffffffffffff    ffffffffff   fffffffffffffffffff  ffffffffffffffffffffffffffffffffffffffffff",
        "ffffffffffffffffffffoofffffffffffffffffffffffffffffffffffooooffffffffffooofffffffffffffffffffooffffffffffffffffffffffffffffffffffffffffff"
    };/*
    else if(level == 2)
    TileMap[H][W] =
    {
        "                                                                                                                                         ",
        "                                                                                                                                         ",
        "                                                                                                                                         ",
        "                                                                                                                                         ",
        "k                               G                                                                                                        ",
        "k          a                                       a                                                                                     ",
        "k                                                                       a                A                   G                           ",
        "k                        A              a                     A                G                                     A                   ",
        "k  A                                                                                                  A                       a          ",
        "k                               ?1?k           G                                             a                                           ",
        "k                                                                                                                                        ",
        "k                                                                                                              b         p               ",
        "k                                                                                                             bb             s           ",
        "k                            kk?k kkk        k?k                                    k3kk                     bbb             s           ",
        "k                                                       b                                                   bbbb             s           ",
        "k                                         H            bb                       b      H                   bbbbb             s           ",
        "k     C         h             c  e            e g     bbb         C e          bb  e               ce     bbbbbb   g         s  h  C     ",
        "ffffffffffffffffffff  fffffffffffffffffffffffffffffffffff    ffffffffff   fffffffffffffffffff  ffffffffffffffffffffffffffffffffffffffffff",
        "ffffffffffffffffffffoofffffffffffffffffffffffffffffffffffooooffffffffffooofffffffffffffffffffooffffffffffffffffffffffffffffffffffffffffff"
    };
}
*/



    void DrawMap(float Light, Sprite tile, RenderWindow& window)
    {
        for(int i = 0; i < H; i++)
            for(int j = 0; j < W; j++) // map drawing
        {
            if(TileMap[i][j] == 'f') // floor
               tile.setTextureRect(IntRect(96, 112, 16, 16));
            if(TileMap[i][j] == 'b') // stone
               tile.setTextureRect(IntRect(112, 112, 16, 16));
            if(TileMap[i][j] == '?' || TileMap[i][j] == '1' || TileMap[i][j] == '2'
               || TileMap[i][j] == '3' || TileMap[i][j] == '4') // present - coin/mushrom
                tile.setTextureRect(IntRect(128, 112 + 16*int(Light), 16, 16));
            if(TileMap[i][j] == 'k') // brick
                tile.setTextureRect(IntRect(144, 112, 16, 16));

            if(TileMap[i][j] == 'c') // cluster1
                tile.setTextureRect(IntRect(50, 58, 45, 32));
            if(TileMap[i][j] == 'C') // cluster2
                tile.setTextureRect(IntRect(4, 106, 69, 45));
            if(TileMap[i][j] == 'g') // cluster3
                tile.setTextureRect(IntRect(160, 122, 96, 20));
            if(TileMap[i][j] == 'h') // hill1
                tile.setTextureRect(IntRect(0, 140, 50, 20));
            if(TileMap[i][j] == 'H') // hill2
                tile.setTextureRect(IntRect(146, 222, 76, 33));
            if(TileMap[i][j] == 'a') // cloud1
                tile.setTextureRect(IntRect(0, 224, 96, 32));
            if(TileMap[i][j] == 'A') // cloud2
                tile.setTextureRect(IntRect(96, 224, 48, 32));
            if(TileMap[i][j] == 'G') // cloud3
                tile.setTextureRect(IntRect(96, 160, 96, 32));

            if(TileMap[i][j] == 'p') // castle
                tile.setTextureRect(IntRect(96, 6, 107, 107));
            if(TileMap[i][j] == ' ' || TileMap[i][j] == '\0' || TileMap[i][j] == 's'
                || TileMap[i][j] == 'o' || TileMap[i][j] == 'e' || TileMap[i][j] == 'g' || TileMap[i][j] == 'Q')
                continue;
            tile.setPosition(j*16, i*16);
            window.draw(tile);
        }
    }



#endif // MAP_H_INCLUDED
