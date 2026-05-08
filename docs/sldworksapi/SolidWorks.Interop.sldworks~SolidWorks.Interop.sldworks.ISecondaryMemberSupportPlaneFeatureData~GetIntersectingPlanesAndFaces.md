# GetIntersectingPlanesAndFaces Method (ISecondaryMemberSupportPlaneFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~GetIntersectingPlanesAndFaces`

Gets the planar entities that intersect the primary structure system member pairs used to create this secondary structure system member.
Gets the planar entities that intersect the primary structure system member pairs used to create this secondary structure system member.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetIntersectingPlanesAndFaces() As System.Object
```

```

Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim value As System.Object
 
value = instance.GetIntersectingPlanesAndFaces()
```

```

System.object GetIntersectingPlanesAndFaces()
```

```

System.Object^ GetIntersectingPlanesAndFaces(); 
```

#### Return Value

Array of [IRefPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPlane.md)s, [ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md)s, and/or [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.md)  
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.md)
