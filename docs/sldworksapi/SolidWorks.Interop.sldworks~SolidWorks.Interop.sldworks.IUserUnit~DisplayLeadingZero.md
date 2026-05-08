# DisplayLeadingZero Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit~DisplayLeadingZero`

Gets whether to display leading zeroes.
Gets whether to display leading zeroes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DisplayLeadingZero As System.Boolean
```

```

Dim instance As IUserUnit
Dim value As System.Boolean
 
instance.DisplayLeadingZero = value
 
value = instance.DisplayLeadingZero
```

```

System.bool DisplayLeadingZero {get; set;}
```

```

property System.bool DisplayLeadingZero {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to display the leading zero, false to not

Example

See the [IUserUnit](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IUserUnit Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit.md)  
[IUserUnit Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IUserUnit_members.md)
