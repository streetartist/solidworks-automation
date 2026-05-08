# ViewDependencies Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewDependencies`

Gets or sets whether to view the FeatureManager design tree by its dependencies.
Gets or sets whether to view the FeatureManager design tree by its dependencies.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ViewDependencies As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.ViewDependencies = value
 
value = instance.ViewDependencies
```

```

System.bool ViewDependencies {get; set;}
```

```

property System.bool ViewDependencies {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to view the FeatureManager design tree by its dependencies, false to not (see **Remarks**)

Remarks

Setting IFeatureManager::ViewDependencies to true sets [IFeatureManager::ViewFeatures](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ViewFeatures.md) to false, and vice versa.

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
[IFeatureManager::ShowFeatureDetails Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowFeatureDetails.md)  
[IFeatureManager::ShowHierarchyOnly Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ShowHierarchyOnly.md)
