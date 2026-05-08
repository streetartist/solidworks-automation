# DistanceMember Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~DistanceMember`

Gets or sets the distance with which to offset this secondary structure system up-to member.
Gets or sets the distance with which to offset this secondary structure system up-to member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DistanceMember As System.Double
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Double
 
instance.DistanceMember = value
 
value = instance.DistanceMember
```

```

System.double DistanceMember {get; set;}
```

```

property System.double DistanceMember {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance in meters

Remarks

This property is valid only if [ISecondaryMemberUpToMembersFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.md) is set to [swSecondaryMemberUpToMembersDistanceFromEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html).swSecondaryMemberUpToMembersDistanceFromEndType\_Distance.

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md)  
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.md)
