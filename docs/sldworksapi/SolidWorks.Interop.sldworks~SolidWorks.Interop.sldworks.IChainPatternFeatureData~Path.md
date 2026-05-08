# Path Property (IChainPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~Path`

Gets or sets the path for this chain pattern feature.
Gets or sets the path for this chain pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Path As System.Object
```

```

Dim instance As IChainPatternFeatureData
Dim value As System.Object
 
instance.Path = value
 
value = instance.Path
```

```

System.object Path {get; set;}
```

```

property System.Object^ Path {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Path:

- 2D or 3D [sketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md) containing an open or closed loop,
- Line in a sketch, or
- Model [edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IChainPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData.md)  
[IChainPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData_members.md)  
[IChainPatternFeatureData::ReverseDirection Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~ReverseDirection.md)  
[IChainPatternFeatureData::PathPlaneReference Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IChainPatternFeatureData~PathPlaneReference.md)
