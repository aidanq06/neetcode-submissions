class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # two pointers approach
        # current pointer
        # roaming pointer

        temperatureList = []

        for current in range(len(temperatures)):
            if current+1 > len(temperatures)-1: # essentially 
            # if current index + 1 is greater than the length, then we can't create it. 
                temperatureList.append(0)
                continue
            roamingRight = current
            while temperatures[roamingRight] <= temperatures[current]:
                # while the roaming variable is NOT warmer than the current pointer
                
                #reaches edge
                if roamingRight+1 > len(temperatures)-1:
                    temperatureList.append(0)
                    break
                else:
                    roamingRight+=1
            if len(temperatureList) != current+1:
                temperatureList.append(roamingRight-current)
        return temperatureList
                