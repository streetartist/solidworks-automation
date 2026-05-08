# OffsetDistance Property (IMoveFaceFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~OffsetDistance`

Gets or sets the offset distance of this translated Move Face feature that has an end condition of Offset From Surface.
Gets or sets the offset distance of this translated Move Face feature that has an end condition of **Offset From Surface**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property OffsetDistance As System.Double
```

```

Dim instance As IMoveFaceFeatureData
Dim value As System.Double
 
instance.OffsetDistance = value
 
value = instance.OffsetDistance
```

```

System.double OffsetDistance {get; set;}
```

```

property System.double OffsetDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Offset distance of this translated Move Face feature that has an end condition of **Offset From Surface** (see **Remarks**)

Remarks

For all other end conditions, use [IMoveFaceFeatureData::Distance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~Distance.md) to get or set the offset distance of a translated Move Face feature.

To find out the type of:

- Move Face feature, use [IMoveFaceFeatureData::MoveType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~MoveType.md).
- end condition, use [IMoveFaceFeatureData::EndCondition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~EndCondition.md).

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
