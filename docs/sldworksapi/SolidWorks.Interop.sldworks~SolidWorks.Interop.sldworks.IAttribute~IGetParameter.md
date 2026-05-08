# IGetParameter Method (IAttribute)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~IGetParameter`

Gets the specified parameter on this attribute.
Gets the specified parameter on this attribute.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetParameter( _
   ByVal NameIn As System.String _
) As Parameter
```

```

Dim instance As IAttribute
Dim NameIn As System.String
Dim value As Parameter
 
value = instance.IGetParameter(NameIn)
```

```

Parameter IGetParameter( 
   System.string NameIn
)
```

```

Parameter^ IGetParameter( 
   System.String^ NameIn
) 
```

#### Parameters

*NameIn*
:   Name of the parameter

#### Return Value

[IParameter](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAttribute Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute.md)  
[IAttribute Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute_members.md)  
[IAttribute::GetParameter Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAttribute~GetParameter.md)
