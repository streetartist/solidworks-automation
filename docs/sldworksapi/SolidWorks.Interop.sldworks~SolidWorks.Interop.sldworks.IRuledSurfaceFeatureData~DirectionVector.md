# DirectionVector Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~DirectionVector`

Gets or sets the reference vector for this ruled-surface feature.
Gets or sets the reference vector for this ruled-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DirectionVector As MathVector
```

```

Dim instance As IRuledSurfaceFeatureData
Dim value As MathVector
 
instance.DirectionVector = value
 
value = instance.DirectionVector
```

```

MathVector DirectionVector {get; set;}
```

```

property MathVector^ DirectionVector {
   MathVector^ get();
   void set (    MathVector^ value);
}
```

#### Property Value

[Reference vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md)

Remarks

This property is only available when [IRuledSurfaceFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~Type.md) is set to swRuledSurfaceType\_Sweep.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.md)  
[IRuledSurfaceFeatureData::UseVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~UseVector.md)
