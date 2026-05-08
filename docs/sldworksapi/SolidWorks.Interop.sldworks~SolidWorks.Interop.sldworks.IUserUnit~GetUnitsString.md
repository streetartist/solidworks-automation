# GetUnitsString Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~GetUnitsString`

Gets the string that describes the unit.
Gets the string that describes the unit.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetUnitsString( _
   ByVal InEnglish As System.Boolean _
) As System.String
```

```

Dim instance As IUserUnit
Dim InEnglish As System.Boolean
Dim value As System.String
 
value = instance.GetUnitsString(InEnglish)
```

```

System.string GetUnitsString( 
   System.bool InEnglish
)
```

```

System.String^ GetUnitsString( 
   System.bool InEnglish
) 
```

#### Parameters

*InEnglish*
:   True to return the string in English, false to not

#### Return Value

String describing the unit

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)
