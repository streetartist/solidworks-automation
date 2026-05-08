# SetMaterialIdName Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialIdName`

Sets the material name for this feature.
Sets the material name for this feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMaterialIdName( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IFeature
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SetMaterialIdName(Name)
```

```

System.bool SetMaterialIdName( 
   System.string Name
)
```

```

System.bool SetMaterialIdName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Material name for this feature

#### Return Value

True if the material name was set successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialIdName.md)  
[IFeature::GetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialUserName.md)  
[IFeature::SetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialUserName.md)
