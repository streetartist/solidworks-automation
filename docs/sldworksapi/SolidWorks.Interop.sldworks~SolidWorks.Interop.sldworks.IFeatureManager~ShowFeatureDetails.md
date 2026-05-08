# ShowFeatureDetails Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDetails`

Gets or sets whether to show the feature details in the FeatureManager design tree.
Gets or sets whether to show the feature details in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowFeatureDetails As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.ShowFeatureDetails = value
 
value = instance.ShowFeatureDetails
```

```

System.bool ShowFeatureDetails {get; set;}
```

```

property System.bool ShowFeatureDetails {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to show the feature details in the FeatureManager design tree, false to hide them (see **Remarks**)

Remarks

Setting IFeatureManager::ShowFeatureDetails to true sets [IFeatureManager::ShowHierarchyOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowHierarchyOnly.md) to false, and vice versa.

This property affects the FeatureManager design tree view of the current configuration of an assembly. It does not affect other configurations.

Example

[Get and Set FeatureManager Design Tree Display (C#)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_CSharp.htm)  
[Get and Set FeatureManager Design Tree Display (VB.NET)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VBNET.htm)  
[Get and Set FeatureManager Design Tree Display (VBA)](Get_and_Set_FeatureManager_Design_Tree_Display_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::ViewDependencies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewDependencies.md)  
[IFeatureManager::ViewFeatures Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewFeatures.md)  
[IFeatureManager::ShowDisplayStateNames Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowDisplayStateNames.md)
