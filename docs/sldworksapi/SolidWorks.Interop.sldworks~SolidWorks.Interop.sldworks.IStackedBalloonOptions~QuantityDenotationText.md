# QuantityDenotationText Property (IStackedBalloonOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStackedBalloonOptions~QuantityDenotationText`

Gets and sets the label of BOM item quantities.
Gets and sets the label of BOM item quantities.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property QuantityDenotationText As System.String
```

```

Dim instance As IStackedBalloonOptions
Dim value As System.String
 
instance.QuantityDenotationText = value
 
value = instance.QuantityDenotationText
```

```

System.string QuantityDenotationText {get; set;}
```

```

property System.String^ QuantityDenotationText {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Label of BOM item quantities

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
