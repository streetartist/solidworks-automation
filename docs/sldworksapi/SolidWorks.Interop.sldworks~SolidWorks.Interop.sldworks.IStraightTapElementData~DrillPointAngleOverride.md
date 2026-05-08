# DrillPointAngleOverride Property (IStraightTapElementData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngleOverride`

Gets or sets whether to override the drill point angle of this straight tap hole element.
Gets or sets whether to override the drill point angle of this straight tap hole element.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DrillPointAngleOverride As System.Boolean
```

```

Dim instance As IStraightTapElementData
Dim value As System.Boolean
 
instance.DrillPointAngleOverride = value
 
value = instance.DrillPointAngleOverride
```

```

System.bool DrillPointAngleOverride {get; set;}
```

```

property System.bool DrillPointAngleOverride {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the drill point angle, false to not

Remarks

This property is valid only if [IStraightTapElementData::EndShape](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~EndShape.md) is set to [swEndShape\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swEndShape_e.html).swEndShape\_DrillPoint.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IStraightTapElementData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData.md)  
[IStraightTapElementData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData_members.md)  
[IStraightTapElementData::DrillPointAngle Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IStraightTapElementData~DrillPointAngle.md)
