# ConvertDoubleToSystemValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertDoubleToSystemValue`

Converts a double value to a document unit value.
Converts a double value to a document unit value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertDoubleToSystemValue( _
   ByVal UserValue As System.Double _
) As System.Double
```

```

Dim instance As IUserUnit
Dim UserValue As System.Double
Dim value As System.Double
 
value = instance.ConvertDoubleToSystemValue(UserValue)
```

```

System.double ConvertDoubleToSystemValue( 
   System.double UserValue
)
```

```

System.double ConvertDoubleToSystemValue( 
   System.double UserValue
) 
```

#### Parameters

*UserValue*
:   Value to convert

#### Return Value

Converted document unit value

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)  
[IUserUnit::ConvertToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToSystemValue.md)  
[IUserUnit::ConvertToUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToUserUnit.md)
