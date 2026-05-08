# SetMaterialUserName Method (IFeature)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialUserName`

Sets the material user name for this feature, which is visible to the user.
Sets the material user name for this feature, which is visible to the user.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetMaterialUserName( _
   ByVal Name As System.String _
) As System.Boolean
```

```

Dim instance As IFeature
Dim Name As System.String
Dim value As System.Boolean
 
value = instance.SetMaterialUserName(Name)
```

```

System.bool SetMaterialUserName( 
   System.string Name
)
```

```

System.bool SetMaterialUserName( 
   System.String^ Name
) 
```

#### Parameters

*Name*
:   Material user name property for this feature

#### Return Value

True if the material user name was set successfully, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)  
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.md)  
[IFeature::GetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialUserName.md)  
[IFeature::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetMaterialIdName.md)  
[IFeature::SetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~SetMaterialIdName.md)
