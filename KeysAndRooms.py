#https://leetcode.com/explore/learn/card/queue-stack/239/conclusion/1391/
# According to run 78.08% time and 40.71% space

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys_to_try = [0]
        visited_rooms = set()
        used_keys = set()
        while keys_to_try:
            current_key = keys_to_try.pop(0)
            if not current_key in visited_rooms:
                visited_rooms.add(current_key)
                used_keys.add(current_key)
                for key in rooms[current_key]:
                    not key in visited_rooms and keys_to_try.append(key)
        for i in range(len(rooms)):
            if not i in used_keys:
                return False
        return True
