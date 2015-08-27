#Defensive programming examples (27/08/2015)

def test_range_overlap():
    assert range_overlap([(-3.0, 5.0), (0.0, 4.5), (-1.5, 2.0)]) == (0.0, 2.0)
    assert range_overlap([ (2.0, 3.0), (2.0, 4.0) ]) == (2.0, 3.0)
    assert range_overlap([ (0.0, 1.0), (0.0, 2.0), (-1.0, 1.0) ]) == (0.0, 1.0)


# But what if there is no overlap? What if they just touch?

# In[4]:

def test_range_overlap_no_overlap():
    assert range_overlap([ (0.0, 1.0), (5.0, 6.0) ]) == None
    assert range_overlap([ (0.0, 1.0), (1.0, 2.0) ]) == None


# What about the case of a single range?

# In[5]:

def test_range_overlap_one_range():
        assert range_overlap([ (0.0, 1.0) ]) == (0.0, 1.0)


# The write a solution - one possible one is below.

# In[1]:

# In[ ]:

def pairs_overlap(rangeA, rangeB):
    # Check if A starts after B ends and 
    # A ends before B starts. If both are 
    # false, there is an overlap.
    # We are assuming (0.0 1.0) and
    # (1.0 2.0) do not overlap. If these should
    # overlap swap >= for > and <= for <.
    overlap = not ((rangeA[0] >= rangeB[1]) or
                   (rangeA[1] <= rangeB[0]))
    
    return overlap

def find_overlap(rangeA, rangeB):
    # Return the overlap between range 
    # A and B
    if pairs_overlap(rangeA, rangeB):
        low = max(rangeA[0], rangeB[0])
        high = min(rangeA[1], rangeB[1])
        return (low, high)
    else:
        return None

def range_overlap(ranges):
    # Return common overlap among a set of 
    # [low, high] ranges.

    if len(ranges) == 1:
        # Special case of one range - 
        # overlaps with itself
        return(ranges[0])
    elif len(ranges) == 2:
        # Just return from find_overlap
        return find_overlap(ranges[0], ranges[1])
    else:
        # Range of A, B, C is the 
        # range of range(B,C) with
        # A, etc. Do this by recursion...
        overlap = find_overlap(ranges[-1], ranges[-2]) 
        if overlap is not None:
            # Chop off the end of ranges and 
            # replace with the overlap
            ranges = ranges[:-2]
            ranges.append(overlap)
            # Now run again, with the smaller list.
            return range_overlap(ranges)
        else:
            return None




if __name__ ==  "__main__":
    import sys

    start = int(sys.argv[1])
    end = int(sys.argv[2])

    print range_overlap([(start,end)])

