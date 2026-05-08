# CoordinateSystem Property (IScaleFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData~CoordinateSystem`

Gets or sets the coordinate system of the scale feature.
Gets or sets the coordinate system of the scale feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CoordinateSystem As System.Object
```

```

Dim instance As IScaleFeatureData
Dim value As System.Object
 
instance.CoordinateSystem = value
 
value = instance.CoordinateSystem
```

```

System.object CoordinateSystem {get; set;}
```

```

property System.Object^ CoordinateSystem {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pointer to the coordinate system [feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Example

See [IScaleFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IScaleFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData.md)  
[IScaleFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IScaleFeatureData_members.md)
