# GetAlternateFace Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetAlternateFace`

Gets an alternate face to use as the boundary face for the curvature control of the patch.
Gets an alternate face to use as the boundary face for the curvature control of the patch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAlternateFace() As Face2
```

```

Dim instance As IFillSurfaceFeatureData
Dim value As Face2
 
value = instance.GetAlternateFace()
```

```

Face2 GetAlternateFace()
```

```

Face2^ GetAlternateFace(); 
```

#### Return Value

Pointer to the alternate face, the [IFace2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md) object

Remarks

This method is valid only when the contact type is tangent and edges are used to define the patch boundary. If an edge has two faces, then this method returns the face with which the resultant feature geometry is tangent.

Use [IFillSurfaceFeatureData::GetCurvatureControl](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData~GetCurvatureControl.md) to determine the contact type.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData.md)  
[IFillSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillSurfaceFeatureData_members.md)
