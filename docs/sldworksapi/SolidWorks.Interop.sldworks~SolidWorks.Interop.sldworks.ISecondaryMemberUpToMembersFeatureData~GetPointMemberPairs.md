# GetPointMemberPairs Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetPointMemberPairs`

Gets the point-member pair(s) used to create one or more secondary structure system up-to members.
Gets the point-member pair(s) used to create one or more secondary structure system up-to members.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetPointMemberPairs( _
   ByRef Points As System.Object, _
   ByRef Members As System.Object, _
   ByRef PointTypes As System.Object _
) 
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Points As System.Object
Dim Members As System.Object
Dim PointTypes As System.Object
 
instance.GetPointMemberPairs(Points, Members, PointTypes)
```

```

void GetPointMemberPairs( 
   out System.object Points,
   out System.object Members,
   out System.object PointTypes
)
```

```

void GetPointMemberPairs( 
   [Out] System.Object^ Points,
   [Out] System.Object^ Members,
   [Out] System.Object^ PointTypes
) 
```

#### Parameters

*Points*
:   Array of [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md)es or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)s

*Members*
:   Array of [IStructureSystemMemberFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStructureSystemMemberFeatureData.md)s

*PointTypes*
:   Array of Points types as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

Remarks

Points and Members arrays are ordered to create point-member pairs.

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.md) is set to [swSecondaryMemberUpToMembersMemberPointParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters\_PointMemberPair.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md)  
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.md)
