# SetStringValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetStringValue`

Obsolete. Superseded by IParameter::SetStringValue2.
Obsolete. Superseded by [IParameter::SetStringValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter~SetStringValue2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetStringValue( _
   ByVal StringValue As System.String _
) As System.Boolean
```

```

Dim instance As IParameter
Dim StringValue As System.String
Dim value As System.Boolean
 
value = instance.SetStringValue(StringValue)
```

```

System.bool SetStringValue( 
   System.string StringValue
)
```

```

System.bool SetStringValue( 
   System.String^ StringValue
) 
```

#### Parameters

*StringValue*

#### Return Value

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IParameter Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter.md)  
[IParameter Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParameter_members.md)
