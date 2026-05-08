# FromScale Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~FromScale`

Gets or sets the custom "from" scale factor for the current drawing sheet.
Gets or sets the custom "from" scale factor for the current drawing sheet.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FromScale As System.Double
```

```

Dim instance As IPrintSpecification
Dim value As System.Double
 
instance.FromScale = value
 
value = instance.FromScale
```

```

System.double FromScale {get; set;}
```

```

property System.double FromScale {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

"From" scale factor in the From:To scale

Remarks

This property is valid only if [IPrintSpecification::ScaleMethod](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ScaleMethod.md) is set to [swPrintSelectionScaleFactor\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrintSelectionScaleFactor_e.html).swPrintSelection.

For details about applying a scale factor to the current drawing sheet, see the **Print Specification** Help topic in the SOLIDWORKS Help.

Example

See the [IPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)  
[IPrintSpecification::ToScale Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ToScale.md)
