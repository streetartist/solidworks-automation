# PropagateToTangentFaces Property (ISurfaceRadiateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~PropagateToTangentFaces`

Gets or sets whether to propagate the tangent faces of this surface radiate feature.
Gets or sets whether to propagate the tangent faces of this surface radiate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PropagateToTangentFaces As System.Boolean
```

```

Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Boolean
 
instance.PropagateToTangentFaces = value
 
value = instance.PropagateToTangentFaces
```

```

System.bool PropagateToTangentFaces {get; set;}
```

```

property System.bool PropagateToTangentFaces {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True continues the surface to tangent faces, false does not continue the surface

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Example

See the [ISurfaceRadiateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISurfaceRadiateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData.md)  
[ISurfaceRadiateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData_members.md)
