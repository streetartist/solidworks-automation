# DatumLinkedModifier1 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifier1`

Gets the modifier of the first linked datum of this Gtol frame datum.
Gets the modifier of the first linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DatumLinkedModifier1 As System.Integer
```

```

Dim instance As IPMIGtolFrameDatum
Dim value As System.Integer
 
instance.DatumLinkedModifier1 = value
 
value = instance.DatumLinkedModifier1
```

```

System.int DatumLinkedModifier1 {get; set;}
```

```

property System.int DatumLinkedModifier1 {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

[First linked datum](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked1.md) material modifier as defined in [swMaterialModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swMaterialModifier_e.html)

Remarks

Use [IPMIGtolFrameDatum::DatumLinkedModifierValue1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifierValue1.md) to get this linked datum's modifier value, if one exists.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.md)  
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.md)
