# Distance Property (IMoveFaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Distance`

Gets or sets the offset distance of this offset or translated Move Face feature.
Gets or sets the offset distance of this offset or translated Move Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Distance As System.Double
```

```

Dim instance As IMoveFaceFeatureData
Dim value As System.Double
 
instance.Distance = value
 
value = instance.Distance
```

```

System.double Distance {get; set;}
```

```

property System.double Distance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Offset distance of this offset or translated Move Face feature (see **Remarks**)

Remarks

To find out whether the Move Face feature was offset or translated, use [IMoveFaceFeatureData::MoveType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~MoveType.md).

If setting the offset distance of a translated Move Face feature that has an [end condition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.md) of **Offset From Surface**, then use [IMoveFaceFeatureData::OffsetDistance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~OffsetDistance.md). For all other end conditions, use IMoveFaceFeatureData::Distance to set the offset distance.

Example

[Translate Move Face Feature (C#)](Translate_Move_Face_Feature_Example_CSharp.htm)  
[Translate Move Face Feature (VB.NET)](Translate_Move_Face_Feature_Example_VBNET.htm)  
[Translate Move Face Feature (VBA)](Translate_Move_Face_Feature_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)
