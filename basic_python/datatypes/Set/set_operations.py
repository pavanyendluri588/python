#union of two sets
#union  of two set will be calculated by using the pipe(|) operator.union means all the elements in the two sets
set1 = {"Monday","Tuesday","Wednesday","Thursday","Sunday"}    
set2 = {"Friday","Saturday","Sunday","Monday","tuesday"}
#method-1
print("union of set1,set2 (set1|set2):",set1|set2)
#method-2
print("union of set1,set2 (set1.union(set2))",set1.union(set2))
print("====================================================================================================")
#intersection of two sets
#intersection of two sets  will be calculated by using the and(&) operator.intersection means all the common elements in the two sets

#method-1
print("intersection of set1,set2 (set1&set2):",set1&set2)
#method-2
print("intersection of set1,set2 (set1.intersection(set2))",set1.intersection(set2)) 

#intersection_update() function this fi=unction will remove all the items from the orginal set that are not present in both the sets 
#example for intersection_update()
a = {"Devansh", "bob", "castle"}    
b = {"castle", "dude", "emyway"}    
c = {"fuson", "gaurav", "castle"}
print("before using intersection_update (a):",a)
a.intersection_update(b,c)
print("after using intersection_update with b,c  and orginal set a  (a):",a)
print("====================================================================================================")

print("set operations\n1.union\n2.intersection\n3.difference\n4.complement\n5.semmetric difference")
"""
1.union="all elements which are in combining all elemrnts of two sets and"
2.intersection="common elements of two sets"
3.difference="elements in a which are not common of other set"
4.complement= the elements except in set a
5.symmetric difference=the elements which are not commom in both sets
"""
print("========================================================")
print("union() operation:")
"""
it will combine the both sets
                  +                 +
                +  +              +   +
              +      +          +       +
            +          +      +           +
          +              +  +               +
        +                  +                  +
      +                  +   +                  +
    +                  +       +                  +
  +                  +           +                  +
+                  +               +                  +
  +                  +           +                  +
    +                  +       +                  +
      +                  +   +                  +
        +                  +                  +
          +              +    +             +
            +          +        +         +
              +      +            +     +
                +  +                + +
                  +                   
"""
str="""
///////////////////////////////////////////////////////////////////////
//                    +                 +                            //
//                  +  +              +   +                          //
//                +      +          +       +                        //
//              +          +      +           +                      //
//            +              +  +               +                    //
//          +                  +                  +                  //
//        +                  +   +                  +                //
//      +                  +       +                  +              //
//    +                  +           +                  +            //
//  +                  +               +                  +          //
//    +                  +           +                  +            // 
//      +                  +       +                  +              //
//        +                  +   +                  +                //
//          +                  +                  +                  //
//            +              +    +             +                    //
//              +          +        +         +                      //
//                +      +            +     +                        //
//                  +  +                + +                          //
//                    +                                              //
///////////////////////////////////////////////////////////////////////
"""
print(str)



















new-








