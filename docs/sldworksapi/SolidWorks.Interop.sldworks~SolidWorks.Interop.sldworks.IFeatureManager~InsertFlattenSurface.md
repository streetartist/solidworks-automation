# InsertFlattenSurface Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlattenSurface`

Obsolete. Superseded by IFeatureManager::InsertFlattenSurface2.
Obsolete. Superseded by [IFeatureManager::InsertFlattenSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertFlattenSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertFlattenSurface( _
   ByVal AccuracyFactor As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim AccuracyFactor As System.Integer
Dim value As Feature
 
value = instance.InsertFlattenSurface(AccuracyFactor)
```

```

Feature InsertFlattenSurface( 
   System.int AccuracyFactor
)
```

```

Feature^ InsertFlattenSurface( 
   System.int AccuracyFactor
) 
```

#### Parameters

*AccuracyFactor*
:   10 >= Accuracy of flattened triangle mesh >= 1; 1 is highest accuracy

#### Return Value

Surface-flatten [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

| Before calling this method, select... | By calling [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark... |
| --- | --- |
| Faces or surfaces to flatten | 1 |
| Anchor point from which to flatten | 16 |
| Edges to guide the shape and length of the flattened surface | 2 |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISurfaceFlattenFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceFlattenFeatureData.md)
