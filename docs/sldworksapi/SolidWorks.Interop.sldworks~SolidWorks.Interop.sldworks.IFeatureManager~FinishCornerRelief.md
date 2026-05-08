# FinishCornerRelief Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishCornerRelief`

Creates a sheet metal corner relief feature.
Creates a sheet metal corner relief feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FinishCornerRelief() As Feature
```

```

Dim instance As IFeatureManager
Dim value As Feature
 
value = instance.FinishCornerRelief()
```

```

Feature FinishCornerRelief()
```

```

Feature^ FinishCornerRelief(); 
```

#### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

Before calling this method, call:

1. [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 0 and Append = true to select the sheet metal body in which to create a corner relief feature.
2. IModelDocExtension::SelectByID2 with Mark = 4 and Append = true to select two faces that form a bend corner.
3. Call [IFeatureManager::AddCornerReliefCorner](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefCorner.md) to add the corner to the corner relief feature.
4. Call [IFeatureManager::AddCornerReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefType.md) to specify the corner relief for the corner.
5. Repeat steps 2 - 4 to add another corner to the corner relief feature.

Example

[Create Corner Relief Feature (C#)](Create_Corner_Relief_Feature_Example_CSharp.htm)  
[Create Corner Relief Feature (VBA)](Create_Corner_Relief_Feature_Example_VB.htm)  
[Create Corner Relief Feature (VB.NET)](Create_Corner_Relief_Feature_Example_VBNET.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFlatPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFlatPatternFeatureData.md)
