# DatumLinkedModifierValue1 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifierValue1`

Gets the value of the modifier of the first linked datum of this Gtol frame datum.
Gets the value of the modifier of the first linked datum of this Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DatumLinkedModifierValue1 As System.Double
```

```

Dim instance As IPMIGtolFrameDatum
Dim value As System.Double
 
instance.DatumLinkedModifierValue1 = value
 
value = instance.DatumLinkedModifierValue1
```

```

System.double DatumLinkedModifierValue1 {get; set;}
```

```

property System.double DatumLinkedModifierValue1 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Value of the [first linked datum modifier](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinkedModifier1.md)

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.md)  
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.md)
