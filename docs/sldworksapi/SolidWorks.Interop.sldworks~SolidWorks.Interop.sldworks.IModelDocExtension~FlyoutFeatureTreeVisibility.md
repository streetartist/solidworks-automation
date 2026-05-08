# FlyoutFeatureTreeVisibility Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~FlyoutFeatureTreeVisibility`

Gets or sets the state of the flyout FeatureManager design tree.
Gets or sets the state of the flyout FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlyoutFeatureTreeVisibility As System.Integer
```

```

Dim instance As IModelDocExtension
Dim value As System.Integer
 
instance.FlyoutFeatureTreeVisibility = value
 
value = instance.FlyoutFeatureTreeVisibility
```

```

System.int FlyoutFeatureTreeVisibility {get; set;}
```

```

property System.int FlyoutFeatureTreeVisibility {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

State of the flyout FeatureManager design tree as defined in [swFeatureTreeState\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFeatureTreeState_e.html)

Example

[Get and Set the State of the Flyout FeatureManager Design Tree (VBA)](Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_VB.htm)  
[Get and Set the State of the Flyout FeatureManager Design Tree (VB.NET)](Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_VBNET.htm)  
[Get and Set the State of the Flyout FeatureManager Design Tree (C#)](Get_and_Set_State_of_Flyout_FeatureManager_Design_Tree_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
