# ToleranceZoneModifier Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~ToleranceZoneModifier`

Gets the tolerance zone modifier in this PMI Gtol frame box.
Gets the tolerance zone modifier in this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ToleranceZoneModifier As System.Integer
```

```

Dim instance As IPMIGtolBoxData
Dim value As System.Integer
 
instance.ToleranceZoneModifier = value
 
value = instance.ToleranceZoneModifier
```

```

System.int ToleranceZoneModifier {get; set;}
```

```

property System.int ToleranceZoneModifier {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Tolerance zone modifier as defined in [swToleranceZoneModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swToleranceZoneModifier_e.html)

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)  
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.md)
