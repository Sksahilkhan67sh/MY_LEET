from typing import List

class Solution:
    def earliestFinishTime(
        self,
        landStartTime: List[int],
        landDuration: List[int],
        waterStartTime: List[int],
        waterDuration: List[int]
    ) -> int:



        min_land_end = min(
            s + d
            for s, d in zip(landStartTime, landDuration)
        )



        min_water_end = min(
            s + d
            for s, d in zip(waterStartTime, waterDuration)
        )

        ans = float('inf')

        # Land -> Water
        for s, d in zip(waterStartTime, waterDuration):
            ans = min(ans, max(min_land_end, s) + d)

        # Water -> Land
        for s, d in zip(landStartTime, landDuration):
            ans = min(ans, max(min_water_end, s) + d)

        return ans