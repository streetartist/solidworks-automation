# RevDirectionDistanceMember Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~RevDirectionDistanceMember`

Gets or sets whether to flip the direction of the distance offset for this secondary structure system up-to member.
Gets or sets whether to flip the direction of the distance offset for this secondary structure system up-to member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RevDirectionDistanceMember As System.Boolean
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Boolean
 
instance.RevDirectionDistanceMember = value
 
value = instance.RevDirectionDistanceMember
```

```

System.bool RevDirectionDistanceMember {get; set;}
```

```

property System.bool RevDirectionDistanceMember {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the direction of the offset, false to not

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
