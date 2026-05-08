# InsertMoldPartingLine Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldPartingLine`

Inserts a mold parting line feature.
Inserts a mold parting line feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertMoldPartingLine( _
   ByVal BFlipDir As System.Boolean _
) As Feature
```

```

Dim instance As IFeatureManager
Dim BFlipDir As System.Boolean
Dim value As Feature
 
value = instance.InsertMoldPartingLine(BFlipDir)
```

```

Feature InsertMoldPartingLine( 
   System.bool BFlipDir
)
```

```

Feature^ InsertMoldPartingLine( 
   System.bool BFlipDir
) 
```

#### Parameters

*BFlipDir*
:   True to flip the direction of the pull, false to not

#### Return Value

Pointer to the [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object

Remarks

Before calling this method, you must select the direction of pull and the edges for the parting line by calling [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with the following Marks:

| Selection | Mark |
| --- | --- |
| Direction of pull | 1 |
| Parting line edges | 4 |

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IPartingLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingLineFeatureData.md)  
[IFeatureManager::InsertMoldCoreCavitySolids Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.md)  
[IFeatureManager::InsertMoldShutOffSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldShutOffSurface.md)  
[IFeatureManager::InsertMoldCoreCavitySolids Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertMoldCoreCavitySolids.md)
