# QuantityOverrideValue Property (IStackedBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityOverrideValue`

Gets and sets the override value for BOM item quantities.
Gets and sets the override value for BOM item quantities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property QuantityOverrideValue As System.String
```

```

Dim instance As IStackedBalloonOptions
Dim value As System.String
 
instance.QuantityOverrideValue = value
 
value = instance.QuantityOverrideValue
```

```

System.string QuantityOverrideValue {get; set;}
```

```

property System.String^ QuantityOverrideValue {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

BOM item quantity override value; valid only when [IStackedBalloonOptions::QuantityOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityOverride.md) is true

Remarks

See the SOLIDWORKS Help for additional details about stacked balloons.

Example

See [IStackedBalloonOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStackedBalloonOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions.md)  
[IStackedBalloonOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions_members.md)
