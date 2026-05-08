# PropagatingEdges Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~PropagatingEdges`

Gets or sets the propagating edges for this surface-extend feature.
Gets or sets the propagating edges for this surface-extend feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagatingEdges As System.Object
```

```

Dim instance As ISurfaceExtendFeatureData
Dim value As System.Object
 
instance.PropagatingEdges = value
 
value = instance.PropagatingEdges
```

```

System.object PropagatingEdges {get; set;}
```

```

property System.Object^ PropagatingEdges {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of propagating [edges](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceExtendFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData.md)  
[ISurfaceExtendFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData_members.md)  
[ISurfaceExtendFeatureData::GetPropagatingEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~GetPropagatingEdgesCount.md)  
[ISurfaceExtendFeatureData::IGetPropagatingEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~IGetPropagatingEdges.md)  
[ISurfaceExtendFeatureData::ISetPropagatingEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceExtendFeatureData~ISetPropagatingEdges.md)
