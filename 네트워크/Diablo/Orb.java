package Diablo;

public class Orb implements WeaponBehavior {
    @Override
    public void useWeapon() {
        System.out.println("오브를 사용해 마법 공격!");
    }
}
