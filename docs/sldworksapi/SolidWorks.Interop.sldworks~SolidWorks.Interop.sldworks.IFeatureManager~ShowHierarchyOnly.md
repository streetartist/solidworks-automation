# ShowHierarchyOnly Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowHierarchyOnly`

Gets or sets whether to show only the hierarchy in the FeatureManager design tree.
Gets or sets whether to show only the hierarchy in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ShowHierarchyOnly As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.ShowHierarchyOnly = value
 
value = instance.ShowHierarchyOnly
```

```

System.bool ShowHierarchyOnly {get; set;}
```

```

property System.bool ShowHierarchyOnly {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to only show the hierarchy in the FeatureManager design tree, false to not (see **Remarks**)

Remarks

Setting IFeatureManager::ShowHierarchyOnly to true sets [IFeatureManager::ShowFeatureDetails](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDetails.md) to false, and vice versa.

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
