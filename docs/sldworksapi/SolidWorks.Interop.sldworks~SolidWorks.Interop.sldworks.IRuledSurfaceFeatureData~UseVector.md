# UseVector Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~UseVector`

Gets or sets whether or not use a reference vector for this ruled-surface feature.
Gets or sets whether or not use a reference vector for this ruled-surface feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property UseVector As System.Boolean
```

```

Dim instance As IRuledSurfaceFeatureData
Dim value As System.Boolean
 
instance.UseVector = value
 
value = instance.UseVector
```

```

System.bool UseVector {get; set;}
```

```

property System.bool UseVector {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to use a reference vector, false to not

Remarks

This property is only available when [IRuledSurfaceFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~Type.md) is set to  swRuledSurfaceType\_Sweep.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IRuledSurfaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData.md)  
[IRuledSurfaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData_members.md)  
[IRuledSurfaceFeatureData::DirectionVector Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRuledSurfaceFeatureData~DirectionVector.md)
