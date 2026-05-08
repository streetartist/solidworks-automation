# InsertUntrimSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface`

Obsolete. Superseded by IFeatureManager::InsertUntrimSurface2.
Obsolete. Superseded by [IFeatureManager::InsertUntrimSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertUntrimSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertUntrimSurface( _
   ByVal FaceUntrimType As System.Integer, _
   ByVal EdgeUntrimType As System.Integer, _
   ByVal Distance As System.Double, _
   ByVal BMerge As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim FaceUntrimType As System.Integer
Dim EdgeUntrimType As System.Integer
Dim Distance As System.Double
Dim BMerge As System.Boolean
Dim value As Feature
 
value = instance.InsertUntrimSurface(FaceUntrimType, EdgeUntrimType, Distance, BMerge)
```

```

Feature InsertUntrimSurface( 
   System.int FaceUntrimType,
   System.int EdgeUntrimType,
   System.double Distance,
   System.bool BMerge
)
```

```

Feature^ InsertUntrimSurface( 
   System.int FaceUntrimType,
   System.int EdgeUntrimType,
   System.double Distance,
   System.bool BMerge
) 
```

#### Parameters

*FaceUntrimType*
:   Untrim face as defined in [swFaceUntrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFaceUntrimType_e.html)

*EdgeUntrimType*
:   Untrim edge as defined in [swEdgeUntrimType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swEdgeUntrimType_e.html)

*Distance*
:   Distance by which to untrim surface

*BMerge*
:   True to create a surface extension that merges with the original surface, false to create a new, separate surface body

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

You must preselect the face or the edges you want to untrim.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.md)
