# EnableFeatureTree Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTree`

Gets or sets whether or not to update the FeatureManager design tree.
Gets or sets whether or not to update the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EnableFeatureTree As System.Boolean
```

```

Dim instance As IFeatureManager
Dim value As System.Boolean
 
instance.EnableFeatureTree = value
 
value = instance.EnableFeatureTree
```

```

System.bool EnableFeatureTree {get; set;}
```

```

property System.bool EnableFeatureTree {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to update FeatureManager design tree, false to not

Remarks

Use this property to temporarily enable or disable the FeatureManager design tree while an add-in is running a series of operations. Temporarily disabling the FeatureManager design tree should increase performance. However, while the FeatureManager design tree is disabled and not being updated, it may become out of date with what is actually in the model.

 

If an interactive user attempts to interact with the FeatureManager design tree while it is in this out-of-date state, problems could occur. Normally, this should not happen because the add-in should only be disabling the FeatureManager design tree update temporarily and then enabling it immediately after the series of operations completes. However, if there is any possibility that the interactive user could interact with the FeatureManager design tree while it is an out-of-date state, then also use [IFeatureManager::EnableFeatureTreeWindow](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EnableFeatureTreeWindow.md), which prohibits any user interaction with the FeatureManager design tree because the control itself is disabled.

Example

[Only Show Selected Components (VBA)](Only_Show_Selected_Components_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.md)  
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.md)  
[IFeatureManager::UpdateFeatureTree Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~UpdateFeatureTree.md)
