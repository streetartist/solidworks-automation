# GetFromPoint Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~GetFromPoint`

Gets the point from which to extend this secondary structure system up-to member.
Gets the point from which to extend this secondary structure system up-to member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub GetFromPoint( _
   ByRef Point As System.Object, _
   ByRef PointType As System.Integer _
) 
```

```

Dim instance As ISecondaryMemberUpToMembersFeatureData
Dim Point As System.Object
Dim PointType As System.Integer
 
instance.GetFromPoint(Point, PointType)
```

```

void GetFromPoint( 
   out System.object Point,
   out System.int PointType
)
```

```

void GetFromPoint( 
   [Out] System.Object^ Point,
   [Out] System.int PointType
) 
```

#### Parameters

*Point*
:   [IVertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) or [ISketchPoint](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPoint.md)

*PointType*
:   Type of Point as defined by [swSelectType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

Remarks

This method is valid only if [ISecondaryMemberUpToMembersFeatureData::MemberPointParametersType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData~MemberPointParametersType.md) is set to [swSecondaryMemberUpToMembersMemberPointParameters\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSecondaryMemberUpToMembersMemberPointParameters_e.html).swSecondaryMemberUpToMembersMemberPointParameters\_FromPoint.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberUpToMembersFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData.md)  
[ISecondaryMemberUpToMembersFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberUpToMembersFeatureData_members.md)
