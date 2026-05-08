# AddFilletedCorners Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~AddFilletedCorners`

Gets and sets whether to fillet the corner relief corners.
Gets and sets whether to fillet the corner relief corners.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AddFilletedCorners As System.Boolean
```

```

Dim instance As ISMCornerReliefData
Dim value As System.Boolean
 
instance.AddFilletedCorners = value
 
value = instance.AddFilletedCorners
```

```

System.bool AddFilletedCorners {get; set;}
```

```

property System.bool AddFilletedCorners {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to fillet the corner relief corners, false to not

Remarks

This property is valid only if [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.md) is set to [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html).swCornerRectangularRelief.

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)  
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.md)  
[ISMCornerReliefData::CornerFilletDiameter Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~CornerFilletDiameter.md)
