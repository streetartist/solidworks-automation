# TolerancePerUnitValue1 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue1`

Gets the tolerance 1 per unit area value in this PMI Gtol frame box.
Gets the tolerance 1 per unit area value in this PMI Gtol frame box.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TolerancePerUnitValue1 As System.Double
```

```

Dim instance As IPMIGtolBoxData
Dim value As System.Double
 
instance.TolerancePerUnitValue1 = value
 
value = instance.TolerancePerUnitValue1
```

```

System.double TolerancePerUnitValue1 {get; set;}
```

```

property System.double TolerancePerUnitValue1 {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Tolerance 1 per unit area

Remarks

This property is valid only if [IPMIFrameData::GeometricCharacteristic](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIFrameData~GeometricCharacteristic.md) returns [swGeometricCharacteristic\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swGeometricCharacteristic_e.html):

- swGeometricCharacteristic\_Flatness
- swGeometricCharacteristic\_Straightness

Use this property to calculate the unit square or circular area. If [IPMIGtolBoxData::TolerancePerUnitType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitType.md) returns [swPMITolPerUnitAreaType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPMITolPerUnitAreaType_e.html).swPMITolPerUnitType\_Rectangular, use this property and [IPMIGtolBoxData::TolerancePerUnitValue2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolerancePerUnitValue2.md) to calculate the unit area value. Then divide [IPMIGtolBoxData::TolValue](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~TolValue.md) by the unit area value to get the tolerance per unit area value.

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolBoxData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData.md)  
[IPMIGtolBoxData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData_members.md)  
[IPMIGtolBoxData::Unit Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolBoxData~Unit.md)
