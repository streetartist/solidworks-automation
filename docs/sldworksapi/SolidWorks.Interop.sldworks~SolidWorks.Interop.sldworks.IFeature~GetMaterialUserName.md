# GetMaterialUserName Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialUserName`

Gets the material name for this feature, which is visible to the user.
Gets the material name for this feature, which is visible to the user.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMaterialUserName() As System.String
```

```

Dim instance As IFeature
Dim value As System.String
 
value = instance.GetMaterialUserName()
```

```

System.string GetMaterialUserName()
```

```

System.String^ GetMaterialUserName(); 
```

#### Return Value

Material user name property on this feature

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialIdName.md)  
[IFeature::SetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialIdName.md)  
[IFeature::SetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialUserName.md)
