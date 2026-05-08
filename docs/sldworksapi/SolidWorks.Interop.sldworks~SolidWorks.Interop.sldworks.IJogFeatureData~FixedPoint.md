# FixedPoint Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~FixedPoint`

Gets or sets the fixed point x, y, z coordinates for this jog feature.
Gets or sets the fixed point x, y, z coordinates for this jog feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FixedPoint As System.Object
```

```

Dim instance As IJogFeatureData
Dim value As System.Object
 
instance.FixedPoint = value
 
value = instance.FixedPoint
```

```

System.object FixedPoint {get; set;}
```

```

property System.Object^ FixedPoint {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of fixed point coordinates

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IJogFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData.md)  
[IJogFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData_members.md)  
[IJogFeatureData::IGetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~IGetFixedPoint.md)  
[IJogFeatureData::ISetFixedPoint Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IJogFeatureData~ISetFixedPoint.md)
