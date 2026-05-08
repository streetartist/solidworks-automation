# ScaleMethod Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification~ScaleMethod`

Gets or sets the page selection option for printing.
Gets or sets the page selection option for printing.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ScaleMethod As System.Integer
```

```

Dim instance As IPrintSpecification
Dim value As System.Integer
 
instance.ScaleMethod = value
 
value = instance.ScaleMethod
```

```

System.int ScaleMethod {get; set;}
```

```

property System.int ScaleMethod {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Page selection option as defined in [swPrintSelectionScaleFactor\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPrintSelectionScaleFactor_e.html)

Remarks

For details about applying a scale factor to the current drawing sheet, see the **Print Specification** Help topic in the SOLIDWORKS Help.

Example

See the [IPrintSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPrintSpecification Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification.md)  
[IPrintSpecification Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPrintSpecification_members.md)
