# PinPosition Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~PinPosition`

Sets the pin position for this detail circle.
Sets the pin position for this detail circle.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PinPosition As System.Boolean
```

```

Dim instance As IDetailCircle
Dim value As System.Boolean
 
instance.PinPosition = value
 
value = instance.PinPosition
```

```

System.bool PinPosition {get; set;}
```

```

property System.bool PinPosition {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to prevent the detail view from moving if the parent view changes size, false to not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.md)  
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.md)
