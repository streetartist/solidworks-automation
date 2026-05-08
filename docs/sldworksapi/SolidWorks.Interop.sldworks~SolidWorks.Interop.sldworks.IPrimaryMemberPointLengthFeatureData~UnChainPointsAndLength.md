# UnChainPointsAndLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~UnChainPointsAndLength`

Gets and sets whether to chain points to create this primary structure system member.
Gets and sets whether to chain points to create this primary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UnChainPointsAndLength As System.Boolean
```

```

Dim instance As IPrimaryMemberPointLengthFeatureData
Dim value As System.Boolean
 
instance.UnChainPointsAndLength = value
 
value = instance.UnChainPointsAndLength
```

```

System.bool UnChainPointsAndLength {get; set;}
```

```

property System.bool UnChainPointsAndLength {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to pair each point passed in [IPrimaryMemberPointLengthFeatureData::SetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~SetPoints.md) to the previous point in the list, false to pair consecutive points only

Remarks

This property is valid only if [IPrimaryMemberPointLengthFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~EndCondition.md) is [swPrimaryMemberPointLengthEndCondition\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPrimaryMemberPointLengthEndCondition_e.html).swPrimaryMemberPointLengthEndCondition\_Point.

If this property is set to true, each point passed to [IPrimaryMemberPointLengthFeatureData::SetPoints](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData~SetPoints.md) pairs with the previous point in the list to create a new member.

For the list of points A,B,C,D,E,F:

If this property is set to true, then 5 members are created:

A -- B

B -- C

C -- D

D -- E

E -- F

If this property is set to false, then only 3 members are created:

A -- B

C -- D

E -- F

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberPointLengthFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData.md)  
[IPrimaryMemberPointLengthFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberPointLengthFeatureData_members.md)
