# SetMaterialIdName Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialIdName`

Sets the material name for this component.
Sets the material name for this component.

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

Dim instance As IComponent2
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
:   Material name

#### Return Value

True if the material name was set, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetMaterialIdName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialIdName.md)  
[IComponent2::SetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetMaterialUserName.md)  
[IComponent2::GetMaterialUserName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMaterialUserName.md)
