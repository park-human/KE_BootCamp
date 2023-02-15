public class Day23 {
    // Diablo v0.3
    public static void main(String[] args){
        Barbarian b1 = new Barbarian();
        Sorceress s1 = new Sorceress();
        Bow windForce = new Bow();
        Axe berserkerAxe = new Axe();
        b1.setWeapon(berserkerAxe);
        s1.setWeapon(windForce); // get Weapon
        s1.performWeapon();
        b1.performWeapon();
        s1.setWeapon(new Axe());
        s1.performWeapon();
        s1.info();
    }
}
