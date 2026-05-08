# FlipSideToCut Property (IExtrudeFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FlipSideToCut`

Gets or sets whether to flip the side to cut.
Gets or sets whether to flip the side to cut.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FlipSideToCut As System.Boolean
```

```

Dim instance As IExtrudeFeatureData2
Dim value As System.Boolean
 
instance.FlipSideToCut = value
 
value = instance.FlipSideToCut
```

```

System.bool FlipSideToCut {get; set;}
```

```

property System.bool FlipSideToCut {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True flips the side to cut, false does not

Remarks

This property is relevant only for cut features.

If the sketch is open, then the first edge in the array returned by [ISketch::GetContourEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetContourEdges.md) and [ISketch::IGetControuEdges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetContourEdges.md) is cut.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.md)  
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.md)
