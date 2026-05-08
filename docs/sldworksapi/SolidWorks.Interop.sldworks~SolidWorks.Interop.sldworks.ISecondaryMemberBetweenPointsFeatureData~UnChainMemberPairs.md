# UnChainMemberPairs Property (ISecondaryMemberBetweenPointsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~UnChainMemberPairs`

Gets and sets whether to chain member pairs to create this secondary structure system member.
Gets and sets whether to chain member pairs to create this secondary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UnChainMemberPairs As System.Boolean
```

```

Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Boolean
 
instance.UnChainMemberPairs = value
 
value = instance.UnChainMemberPairs
```

```

System.bool UnChainMemberPairs {get; set;}
```

```

property System.bool UnChainMemberPairs {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to pair each member passed in [ISecondaryMemberBetweenPointsFeatureData::SetMemberPairs](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SetMemberPairs.md) to the previous member passed, false to pair consecutive members only

Remarks

If this property is set to true, each primary member passed to ISecondaryMemberBetweenPointsFeatureData::SetMemberPairs pairs with the previous primary member to create a new member pair.

For the list of members A,B,C,D,E,F:

If this property is set to true, then 5 member pairs are created:

A -- B

B -- C

C -- D

D -- E

E -- F

If this property is set to false, then only 3 member pairs are created:

A -- B

C -- D

E -- F

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md)  
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.md)
