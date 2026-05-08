# QuantityOverride Property (IBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions~QuantityOverride`

Gets and sets whether to override the BOM item quantity.
Gets and sets whether to override the BOM item quantity.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property QuantityOverride As System.Boolean
```

```

Dim instance As IBalloonOptions
Dim value As System.Boolean
 
instance.QuantityOverride = value
 
value = instance.QuantityOverride
```

```

System.bool QuantityOverride {get; set;}
```

```

property System.bool QuantityOverride {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the BOM item quantity, false to not

Remarks

See the SOLIDWORKS Help for additional details about balloons.

Example

See [IBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions.md)  
[IBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBalloonOptions_members.md)
