# TolerancePerUnitValue2 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue2`

Gets the tolerance 2 per unit area in this PMI Gtol frame box.
Gets the tolerance 2 per unit area in this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TolerancePerUnitValue2 As System.Double
```

```

Dim instance As IPMIGtolBoxData
Dim value As System.Double
 
instance.TolerancePerUnitValue2 = value
 
value = instance.TolerancePerUnitValue2
```

```

System.double TolerancePerUnitValue2 {get; set;}
```

```

property System.double TolerancePerUnitValue2 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Tolerance 2 per unit area

Remarks

This property is valid only if:

- [IPMIFrameData::GeometricCharacteristic](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GeometricCharacteristic.md) returns [swGeometricCharacteristic\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGeometricCharacteristic_e.html)
  - swGeometricCharacteristic\_Flatness
  - swGeometricCharacteristic\_Straightness
- [IPMIGtolBoxData::TolerancePerUnitType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitType.md) returns [swPMITolPerUnitAreaType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMITolPerUnitAreaType_e.html).swPMITolPerUnitType\_Rectangular.

If IPMIGtolBoxData::TolerancePerUnitType returns swPMITolPerUnitAreaType\_e.swPMITolPerUnitType\_Rectangular, use this property and [IPMIGtolBoxData::TolerancePerUnitValue1](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue1.md) to calculate the unit area value. Then divide [IPMIGtolBoxData::TolValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolValue.md) by the unit area value to get the tolerance per unit area value.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)  
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.md)  
[IPMIGtolBoxData::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit.md)
