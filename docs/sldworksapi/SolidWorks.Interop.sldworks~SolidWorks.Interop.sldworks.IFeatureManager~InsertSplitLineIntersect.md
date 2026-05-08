# InsertSplitLineIntersect Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect`

Creates split lines using the selected intersecting tool and target entities.
Creates split lines using the selected intersecting tool and target entities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertSplitLineIntersect( _
   ByVal CompleteOption As System.Integer _
) As Feature
```

```

Dim instance As IFeatureManager
Dim CompleteOption As System.Integer
Dim value As Feature
 
value = instance.InsertSplitLineIntersect(CompleteOption)
```

```

Feature InsertSplitLineIntersect( 
   System.int CompleteOption
)
```

```

Feature^ InsertSplitLineIntersect( 
   System.int CompleteOption
) 
```

#### Parameters

*CompleteOption*
:   - 1 = Linear
    - 7 = Natural
    - 9 = Split all and linear
    - 15 = Split all and natural

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.md)  
[IModelDoc2::InsertSplitLineProject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineProject.md)  
[IModelDoc2::InsertSplitLineSil Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.md)
