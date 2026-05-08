# Depth Property (ISimpleHoleFeatureData2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~Depth`

Gets or sets the depth of this simple hole feature.
Gets or sets the depth of this simple hole feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Depth As System.Double
```

```

Dim instance As ISimpleHoleFeatureData2
Dim value As System.Double
 
instance.Depth = value
 
value = instance.Depth
```

```

System.double Depth {get; set;}
```

```

property System.double Depth {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Hole depth

Remarks

This property only supports getting the depth of a blind hole. To get the depth of holes with other types of end conditions, you could:

- use [IExtrudeFeatureData2::GetDepth](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetDepth.md) to get the length of the extrusion.
- analyze the curves and edges of the hole to get the depth or thickness of it at a specific point.
- use [ISimpleHoleFeatureData2::SurfaceOffset](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2~SurfaceOffset.md) for a hole with a depth that is offset from the surface.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISimpleHoleFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2.md)  
[ISimpleHoleFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleHoleFeatureData2_members.md)
