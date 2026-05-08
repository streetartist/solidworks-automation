# SlotWidth Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~SlotWidth`

Gets and sets the width of this corner relief slot.
Gets and sets the width of this corner relief slot.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SlotWidth As System.Double
```

```

Dim instance As ISMCornerReliefData
Dim value As System.Double
 
instance.SlotWidth = value
 
value = instance.SlotWidth
```

```

System.double SlotWidth {get; set;}
```

```

property System.double SlotWidth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Corner relief slot width (see **Remarks**)

Remarks

This property is valid only if [ISMCornerReliefData::ReliefType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~ReliefType.md) is set to one of the following [swCornerReliefType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swCornerReliefType_e.html) members. If...:

- swCornerCircularRelief, then this property returns a radial slot width value.
- swCornerObroundRelief, then this property returns a linear slot width value.

Example

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.md)  
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.md)
