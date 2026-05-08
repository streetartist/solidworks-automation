# RevDirectionLengthRatioMember Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~RevDirectionLengthRatioMember`

Gets or sets whether to flip the direction of the length ratio offset of this secondary structure system up-to member.
Gets or sets whether to flip the direction of the length ratio offset of this secondary structure system up-to member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property RevDirectionLengthRatioMember As System.Boolean
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim value As System.Boolean
 
instance.RevDirectionLengthRatioMember = value
 
value = instance.RevDirectionLengthRatioMember
```

```

System.bool RevDirectionLengthRatioMember {get; set;}
```

```

property System.bool RevDirectionLengthRatioMember {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the direction of the offset, false to not

Remarks

This property is valid only if [ISecondaryMemberUpToMembersFeatureData::SecondaryMemberOffsetType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SecondaryMemberOffsetType.md) is set to [swSecondaryMemberUpToMembersDistanceFromEndType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersDistanceFromEndType_e.html).swSecondaryMemberUpToMembersDistanceFromEndType\_LengthRatio.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md)  
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.md)
