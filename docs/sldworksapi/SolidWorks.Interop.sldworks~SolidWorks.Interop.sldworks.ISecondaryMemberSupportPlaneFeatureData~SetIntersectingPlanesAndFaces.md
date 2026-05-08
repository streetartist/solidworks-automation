# SetIntersectingPlanesAndFaces Method (ISecondaryMemberSupportPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~SetIntersectingPlanesAndFaces`

Sets the planar entities that intersect the primary structure system member pairs used to create this secondary structure system member.
Sets the planar entities that intersect the primary structure system member pairs used to create this secondary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetIntersectingPlanesAndFaces( _
   ByVal RefArray As System.Object _
) As System.Boolean
```

```

Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim RefArray As System.Object
Dim value As System.Boolean
 
value = instance.SetIntersectingPlanesAndFaces(RefArray)
```

```

System.bool SetIntersectingPlanesAndFaces( 
   System.object RefArray
)
```

```

System.bool SetIntersectingPlanesAndFaces( 
   System.Object^ RefArray
) 
```

#### Parameters

*RefArray*
:   Array of [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)s, [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)s, and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s

#### Return Value

True if intersecting planes and faces successfully set, false if not

Remarks

During editing, RefArray can hold only one entity.

Example

See the [ISecondaryMemberBetweenPointsFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberBetweenPointsFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.md)  
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.md)
