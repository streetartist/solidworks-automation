# SymbolStyle Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~SymbolStyle`

Gets the symbol style of this PMI datum target.
Gets the symbol style of this PMI datum target.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SymbolStyle As System.Integer
```

```

Dim instance As IPMIDatumTarget
Dim value As System.Integer
 
instance.SymbolStyle = value
 
value = instance.SymbolStyle
```

```

System.int SymbolStyle {get; set;}
```

```

property System.int SymbolStyle {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Symbol style as defined in [swPMIDatumTargetSymbolStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumTargetSymbolStyle_e.html)

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.md)  
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.md)
