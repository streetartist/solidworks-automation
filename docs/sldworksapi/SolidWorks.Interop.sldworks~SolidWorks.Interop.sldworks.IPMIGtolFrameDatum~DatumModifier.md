# DatumModifier Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumModifier`

Gets the material modifier of this Gtol frame datum.
Gets the material modifier of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DatumModifier As System.Integer
```

```

Dim instance As IPMIGtolFrameDatum
Dim value As System.Integer
 
instance.DatumModifier = value
 
value = instance.DatumModifier
```

```

System.int DatumModifier {get; set;}
```

```

property System.int DatumModifier {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

[Datum](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~Datum.md) material modifier as defined in [swMaterialModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMaterialModifier_e.html)

Remarks

Use [IPMIGtolFrameDatum::DatumModifierValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumModifierValue.md) to get this datum modifier's value, if one exists.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.md)  
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.md)
