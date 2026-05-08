# ConvertToSystemValue Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToSystemValue`

Converts a text string to a document unit value.
Converts a text string to a document unit value.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertToSystemValue( _
   ByVal UnitText As System.String, _
   ByRef ComputedValue As System.Double _
) As System.Boolean
```

```

Dim instance As IUserUnit
Dim UnitText As System.String
Dim ComputedValue As System.Double
Dim value As System.Boolean
 
value = instance.ConvertToSystemValue(UnitText, ComputedValue)
```

```

System.bool ConvertToSystemValue( 
   System.string UnitText,
   out System.double ComputedValue
)
```

```

System.bool ConvertToSystemValue( 
   System.String^ UnitText,
   [Out] System.double ComputedValue
) 
```

#### Parameters

*UnitText*
:   Value to convert

*ComputedValue*
:   Converted value in document units

#### Return Value

True if successful, false if not

Remarks

This takes the value directly from a textbox control and passes it in to convert to a double value.

This imitates the behavior of when working in the SOLIDWORKS user interface and passing a value like "10 / 2" into one of the values on a dialog box.

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)  
[IUserUnit::ConvertDoubleToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertDoubleToSystemValue.md)  
[IUserUnit::ConvertToUserUnit Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToUserUnit.md)
