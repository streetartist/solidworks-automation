# SetPointMemberPairs Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~SetPointMemberPairs`

Sets the point-member pair(s) used to create one or more secondary structure system up-to members.
Sets the point-member pair(s) used to create one or more secondary structure system up-to members.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetPointMemberPairs( _
   ByVal Points As System.Object, _
   ByVal Members As System.Object _
) As System.Boolean
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Points As System.Object
Dim Members As System.Object
Dim value As System.Boolean
 
value = instance.SetPointMemberPairs(Points, Members)
```

```

System.bool SetPointMemberPairs( 
   System.object Points,
   System.object Members
)
```

```

System.bool SetPointMemberPairs( 
   System.Object^ Points,
   System.Object^ Members
) 
```

#### Parameters

*Points*
:   Array of [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)es or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)s

*Members*
:   Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md)s

Remarks

Points and Members arrays must be ordered to create point-member pairs.

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.md) is set to [swSecondaryMemberUpToMembersMemberPointParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters\_PointMemberPair.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md)  
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.md)
