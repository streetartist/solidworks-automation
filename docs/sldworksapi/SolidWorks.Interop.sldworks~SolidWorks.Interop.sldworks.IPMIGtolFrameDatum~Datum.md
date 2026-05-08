# Datum Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~Datum`

Gets the Gtol frame datum.
Gets the Gtol frame datum.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Datum As System.String
```

```

Dim instance As IPMIGtolFrameDatum
Dim value As System.String
 
instance.Datum = value
 
value = instance.Datum
```

```

System.string Datum {get; set;}
```

```

property System.String^ Datum {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Gtol frame datum

Remarks

In the Geometric Tolerance Properties dialog, you can specify up to two datums linked to the Primary, Secondary, and Tertiary datums. Click the drop-down selector next to each datum field to pop up a linked datum dialog where you can specify the linked datums and their material modifiers.

This property gets the primary, secondary, or tertiary datum. Use [IPMIGtolFrameDatum::DatumLinked1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked1.md) and [IPMIGtolFrameDatum::DatumLinked2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum~DatumLinked2.md) to get the datums linked to this datum.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolFrameDatum Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum.md)  
[IPMIGtolFrameDatum Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolFrameDatum_members.md)
