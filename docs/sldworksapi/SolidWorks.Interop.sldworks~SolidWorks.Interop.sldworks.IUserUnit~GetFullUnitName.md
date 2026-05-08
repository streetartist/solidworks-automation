# GetFullUnitName Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~GetFullUnitName`

Gets the full name of the unit.
Gets the full name of the unit.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFullUnitName( _
   ByVal Plural As System.Boolean _
) As System.String
```

```

Dim instance As IUserUnit
Dim Plural As System.Boolean
Dim value As System.String
 
value = instance.GetFullUnitName(Plural)
```

```

System.string GetFullUnitName( 
   System.bool Plural
)
```

```

System.String^ GetFullUnitName( 
   System.bool Plural
) 
```

#### Parameters

*Plural*
:   True if the name of the unit is plural, false if not

#### Return Value

Full name of the unit

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)
