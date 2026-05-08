# CornerFilletDiameter Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~CornerFilletDiameter`

Gets and sets the diameter of the filleted corner.
Gets and sets the diameter of the filleted corner.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CornerFilletDiameter As System.Double
```

```

Dim instance As ISMCornerReliefData
Dim value As System.Double
 
instance.CornerFilletDiameter = value
 
value = instance.CornerFilletDiameter
```

```

System.double CornerFilletDiameter {get; set;}
```

```

property System.double CornerFilletDiameter {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Diameter

Remarks

This property is valid only if:

- [ISMCornerReliefData::AddFilletedCorners](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~AddFilletedCorners.md) is true,

    - And -

- [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.md) is set to [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).swCornerRectangularRelief.

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)  
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.md)
