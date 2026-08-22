/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */

class Solution {
    public int findInMountainArray(int target, MountainArray mount) {
        int n = mount.length();
        int l = 1;
        int r = n - 2;
        int p = 0;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int peak = mount.get(mid);
            int less = mount.get(mid - 1);
            int more = mount.get(mid + 1);

            if (peak == target)
                return mid;

            if (less < peak && peak > more) {
                p = mid;
                break;
            } else if (less < peak && peak < more)
                l = mid + 1;
            else
                r = mid - 1;
        }

        l = 0;
        r = p - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int bich = mount.get(mid);
            if (bich == target)
                return mid;
            else if (bich > target)
                r = mid - 1;
            else
                l = mid + 1;
        }

        l = p + 1;
        r = n - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            int bich = mount.get(mid);
            if (bich == target)
                return mid;
            else if (bich < target)
                r = mid - 1;
            else
                l = mid + 1;
        }

        return -1;
    }
}