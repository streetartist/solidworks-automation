# DrillPointAngle Property (IStraightTapElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngle`

Gets or sets the drill point angle of this straight tap hole element.
Gets or sets the drill point angle of this straight tap hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DrillPointAngle As System.Double
```

```

Dim instance As IStraightTapElementData
Dim value As System.Double
 
instance.DrillPointAngle = value
 
value = instance.DrillPointAngle
```

```

System.double DrillPointAngle {get; set;}
```

```

property System.double DrillPointAngle {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Drill point angle

Remarks

This property is valid only if [IStraightTapElementData::EndShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~EndShape.md) is set to [swEndShape\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndShape_e.html).swEndShape\_DrillPoint and [IStraightTapElementData::DrillPointAngleOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngleOverride.md) is set to true.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md)  
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.md)
