# FollowAssemblyOrder2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder2`

Gets or sets whether the order of the item numbers in the BOM follows the order in which the assembly appears in the FeatureManager design tree.
Gets or sets whether the order of the item numbers in the BOM follows the order in which the assembly appears in the FeatureManager design tree.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FollowAssemblyOrder2 As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
instance.FollowAssemblyOrder2 = value
 
value = instance.FollowAssemblyOrder2
```

```

System.bool FollowAssemblyOrder2 {get; set;}
```

```

property System.bool FollowAssemblyOrder2 {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True for the item numbers in the BOM to follow the order in which the assembly appears in the FeatureManager design tree, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)  
[IBomFeature::KeepCurrentItemNumbers Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~KeepCurrentItemNumbers.md)
