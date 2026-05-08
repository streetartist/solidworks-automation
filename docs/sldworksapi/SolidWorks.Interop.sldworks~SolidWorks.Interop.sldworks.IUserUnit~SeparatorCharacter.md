# SeparatorCharacter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~SeparatorCharacter`

Gets the decimal separator character.
Gets the decimal separator character.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SeparatorCharacter As System.String
```

```

Dim instance As IUserUnit
Dim value As System.String
 
instance.SeparatorCharacter = value
 
value = instance.SeparatorCharacter
```

```

System.string SeparatorCharacter {get; set;}
```

```

property System.String^ SeparatorCharacter {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Character passed as a string to represent the decimal separator

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)
