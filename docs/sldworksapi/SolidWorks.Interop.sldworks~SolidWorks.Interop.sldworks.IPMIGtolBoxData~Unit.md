# Unit Property (IPMIGtolBoxData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit`

Gets the units of tolerance for this PMI Gtol frame box.
Gets the units of tolerance for this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Unit As System.Integer
```

```

Dim instance As IPMIGtolBoxData
Dim value As System.Integer
 
instance.Unit = value
 
value = instance.Unit
```

```

System.int Unit {get; set;}
```

```

property System.int Unit {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Units of tolerance as defined in [swPMIUnit\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMIUnit_e.html)

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)  
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.md)  
[IPMIGtolBoxData::TolerancePerUnitValue1 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue1.md)  
**IPMIGtolBoxData::TolerancePerUnitValue1Precision Property ()**  
[IPMIGtolBoxData::TolerancePerUnitValue2 Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue2.md)  
**IPMIGtolBoxData::TolerancePerUnitValue2Precision Property ()**  
[IPMIGtolBoxData::TolValue Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolValue.md)  
**IPMIGtolBoxData::TolValuePrecision Property ()**  
[IPMIGtolBoxData::GetTolTypeValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~GetTolTypeValues.md)  
**IPMIGtolBoxData::GetTolTypeValuesPrecision Method ()**
