# AddCornerReliefCorner Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefCorner`

Adds the bend corner of two selected faces of a sheet metal body to the set of corners to which to apply a corner relief.
Adds the bend corner of two selected faces of a sheet metal body to the set of corners to which to apply a corner relief.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddCornerReliefCorner() As System.Integer
```

```

Dim instance As IFeatureManager
Dim value As System.Integer
 
value = instance.AddCornerReliefCorner()
```

```

System.int AddCornerReliefCorner()
```

```

System.int AddCornerReliefCorner(); 
```

#### Return Value

Index of corner to which to apply the corner relief; used by [IFeatureManager::AddCornerReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefType.md)

Remarks

To create a corner relief feature:

1. Call [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md) with Mark = 0 and Append = true to select the sheet metal body in which to create a corner relief feature.
2. Call IModelDocExtension::SelectByID2 with Mark = 4 and Append = true to select two faces that form a bend corner.
3. Call this method to add the corner to the corner relief feature.
4. Call [IFeatureManager::AddCornerReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~AddCornerReliefType.md) to specify the corner relief for the corner.
5. Repeat steps 2 - 4 to add another corner to the corner relief feature.
6. Call [IFeatureManager::FinishCornerRelief](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~FinishCornerRelief.md).

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
