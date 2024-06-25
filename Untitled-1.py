# reverse a list in-place without using any extra list or slicing

def reverse_list(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        # swap the elements at left and right pointers
        nums[left], nums[right] = nums[right], nums[left]

        # Move the pointer to the center
        left += 1
        right -= 1

#Example usage
nums = [1, 2, 3, 4, 5]
reverse_list(nums)

# it'll print the numbers reverse order
print("reversed list: ",nums)