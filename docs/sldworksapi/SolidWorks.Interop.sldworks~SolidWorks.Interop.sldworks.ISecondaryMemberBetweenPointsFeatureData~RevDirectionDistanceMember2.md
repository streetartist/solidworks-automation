# RevDirectionDistanceMember2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~RevDirectionDistanceMember2`

Gets and sets whether to reverse the direction of the offset for the second member of the primary structure system member pair.
Gets and sets whether to reverse the direction of the offset for the second member of the primary structure system member pair.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RevDirectionDistanceMember2 As System.Boolean
```

```

Dim instance As ISecondaryMemberBetweenPointsFeatureData
Dim value As System.Boolean
 
instance.RevDirectionDistanceMember2 = value
 
value = instance.RevDirectionDistanceMember2
```

```

System.bool RevDirectionDistanceMember2 {get; set;}
```

```

property System.bool RevDirectionDistanceMember2 {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to reverse the direction of the offset from the end of the second member, false to not

Remarks

This property is valid only if [ISecondaryMemberBetweenPointsFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData~SecondaryMemberOffsetType.md) is set to [swSecondaryMemberBetweenPointsDistanceFromEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberBetweenPointsDistanceFromEndType_e.html).swSecondaryMemberBetweenPointsDistanceFromEndType\_Distance.

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberBetweenPointsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md)  
[ISecondaryMemberBetweenPointsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData_members.md)
