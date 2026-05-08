# ConvertToUserUnit Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToUserUnit`

Converts the input value to document units.
Converts the input value to document units.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ConvertToUserUnit( _
   ByVal ValueIn As System.Double, _
   ByVal ShowUsernames As System.Boolean, _
   ByVal NameInEnglish As System.Boolean _
) As System.String
```

```

Dim instance As IUserUnit
Dim ValueIn As System.Double
Dim ShowUsernames As System.Boolean
Dim NameInEnglish As System.Boolean
Dim value As System.String
 
value = instance.ConvertToUserUnit(ValueIn, ShowUsernames, NameInEnglish)
```

```

System.string ConvertToUserUnit( 
   System.double ValueIn,
   System.bool ShowUsernames,
   System.bool NameInEnglish
)
```

```

System.String^ ConvertToUserUnit( 
   System.double ValueIn,
   System.bool ShowUsernames,
   System.bool NameInEnglish
) 
```

#### Parameters

*ValueIn*
:   Value to convert

*ShowUsernames*
:   True to show the user names, false to not

*NameInEnglish*
:   True to return the name in English, false to not

#### Return Value

Conversion to a string

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)  
[IUserUnit::ConvertDoubleToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertDoubleToSystemValue.md)  
[IUserUnit::ConvertToSystemValue Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~ConvertToSystemValue.md)
