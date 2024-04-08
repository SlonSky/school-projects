package com.company;

import com.company.classes.EntityA;
import com.company.classes.EntityB;

import java.util.LinkedList;

/**
 * Created by Slon on 01.03.2016.
 */
public class Physics {
    public static boolean Collision(EntityA eA, EntityB entB){
            if(eA.getBounds().intersects(entB.getBounds())){
                return true;
            }
        return false;
    }

    public static boolean Collision(EntityB eB,EntityA entA){
            if(eB.getBounds().intersects(entA.getBounds())) {
                return true;
            }
        return false;
    }
}
