# DirectionReference Property (ISurfaceRadiateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~DirectionReference`

Gets or sets the radiate direction setting for this surface radiate feature.
Gets or sets the radiate direction setting for this surface radiate feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DirectionReference As System.Object
```

```

Dim instance As ISurfaceRadiateFeatureData
Dim value As System.Object
 
instance.DirectionReference = value
 
value = instance.DirectionReference
```

```

System.object DirectionReference {get; set;}
```

```

property System.Object^ DirectionReference {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Face, reference plane, or reference surface indicating radiate direction

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
[ISurfaceRadiateFeatureData::Flip Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceRadiateFeatureData~Flip.md)
