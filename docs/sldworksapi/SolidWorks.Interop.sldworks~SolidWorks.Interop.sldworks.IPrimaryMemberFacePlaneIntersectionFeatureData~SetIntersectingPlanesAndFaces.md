# SetIntersectingPlanesAndFaces Method (IPrimaryMemberFacePlaneIntersectionFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~SetIntersectingPlanesAndFaces`

Sets the planes, surfaces, and faces that intersect with parameter faces of this structure system member.
Sets the planes, surfaces, and faces that intersect with parameter faces of this structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetIntersectingPlanesAndFaces( _
   ByVal RefList As System.Object _
) As System.Boolean
```

```

Dim instance As IPrimaryMemberFacePlaneIntersectionFeatureData
Dim RefList As System.Object
Dim value As System.Boolean
 
value = instance.SetIntersectingPlanesAndFaces(RefList)
```

```

System.bool SetIntersectingPlanesAndFaces( 
   System.object RefList
)
```

```

System.bool SetIntersectingPlanesAndFaces( 
   System.Object^ RefList
) 
```

#### Parameters

*RefList*
:   Array of [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)s, [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)s, and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s that intersect with parameter faces

#### Return Value

True if intersecting objects successfully set, false if not

Remarks

Entities passed should intersect with at least one entity returned by [IPrimaryMemberFacePlaneIntersectionFeatureData::GetParameterFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData~GetParameterFaces.md).

At edit time, you can set only one intersecting entity.

Example

See the [IPrimaryMemberFacePlaneIntersectionFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrimaryMemberFacePlaneIntersectionFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData.md)  
[IPrimaryMemberFacePlaneIntersectionFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrimaryMemberFacePlaneIntersectionFeatureData_members.md)
