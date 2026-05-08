# TransitionDistance Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~TransitionDistance`

Gets or sets the distance to set between adjacent edges for this parting surface feature.
Gets or sets the distance to set between adjacent edges for this parting surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TransitionDistance As System.Double
```

```

Dim instance As IPartingSurfaceFeatureData
Dim value As System.Double
 
instance.TransitionDistance = value
 
value = instance.TransitionDistance
```

```

System.double TransitionDistance {get; set;}
```

```

property System.double TransitionDistance {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Distance

Remarks

This property is only available when [IPartingSurfaceFeatureData::TransitionType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData~TransitionType.md) is set to swPartingSurfaceSmoothngType\_e.swPartingSurfaceSmooth.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartingSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData.md)  
[IPartingSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartingSurfaceFeatureData_members.md)
