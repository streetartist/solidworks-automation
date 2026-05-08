# FeatureManager Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~FeatureManager`

Gets the IFeatureManager object, which allows access to the FeatureManager design tree.
Gets the [IFeatureManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md) object, which allows access to the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property FeatureManager As FeatureManager
```

```

Dim instance As IModelDoc2
Dim value As FeatureManager
 
value = instance.FeatureManager
```

```

FeatureManager FeatureManager {get;}
```

```

property FeatureManager^ FeatureManager {
   FeatureManager^ get();
}
```

#### Property Value

[IFeatureManager](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md) object

Example

[Insert Macro Feature (C++)](Insert_Macro_Feature_Example_CPlusPlus_COM.htm)  
[Insert DXF File and Add Dimension (VBA)](Insert_DXF_File_and_Add_Dimension_Example_VB.htm)  
[Insert Folder in FeatureManager Design Tree (VBA)](Insert_Folder_in_FeatureManager_Design_Tree_Example_VB.htm)  
[Insert Reference POints (VBA)](Insert_Reference_Points_Example_VB.htm)  
[Update FeatureManager Design Tree (VBA)](Update_FeatureManager_Design_Tree_Example_VB.htm)  
[Insert MidSurface in Component (C#)](Insert_MidSurface_in_Component_Example_CSharp.htm)  
[Insert MidSurface in Component (VB.NET)](Insert_MidSurface_in_Component_Example_VBNET.htm)  
[Insert MidSurface in Component (VBA)](Insert_MidSurface_in_Component_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
