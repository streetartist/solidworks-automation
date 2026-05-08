# Diameter Property (IPMIDatumTarget)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Diameter`

Gets the PMI datum target diameter.
Gets the PMI datum target diameter.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Diameter As System.Double
```

```

Dim instance As IPMIDatumTarget
Dim value As System.Double
 
instance.Diameter = value
 
value = instance.Diameter
```

```

System.double Diameter {get; set;}
```

```

property System.double Diameter {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Datum target diameter

Remarks

This property is valid only if [IPMIDatumTarget::AreaStyle](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~AreaStyle.md) is set to [swPMIDatumTargetAreaStyle\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIDatumTargetAreaStyle_e.html).swPMIDatumTargetAreaStyle\_X or swPMIDatumTargetAreaStyle\_Circular.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIDatumTarget Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget.md)  
[IPMIDatumTarget Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget_members.md)  
[IPMIDatumTarget::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIDatumTarget~Unit.md)
