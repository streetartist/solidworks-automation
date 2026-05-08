# FollowAssemblyOrder Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder`

Obsolete. Superseded by IBomFeature::FollowAssemblyOrder2.
Obsolete. Superseded by [IBomFeature::FollowAssemblyOrder2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~FollowAssemblyOrder2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function FollowAssemblyOrder() As System.Boolean
```

```

Dim instance As IBomFeature
Dim value As System.Boolean
 
value = instance.FollowAssemblyOrder()
```

```

System.bool FollowAssemblyOrder()
```

```

System.bool FollowAssemblyOrder(); 
```

#### Return Value

True for the items numbers in the BOM to follow the order in which the assembly appears in the FeatureManager design tree, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.md)  
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.md)
