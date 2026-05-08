# GeometryPattern Property (ISketchPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~GeometryPattern`

Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature.
Gets or sets whether to create the pattern using only the geometry (faces and edges) of the feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property GeometryPattern As System.Boolean
```

```

Dim instance As ISketchPatternFeatureData
Dim value As System.Boolean
 
instance.GeometryPattern = value
 
value = instance.GeometryPattern
```

```

System.bool GeometryPattern {get; set;}
```

```

property System.bool GeometryPattern {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to create the pattern using only the geometry of the feature, false to pattern the entire feature

Remarks

This property is valid only if [ISketchPatternFeatureData::BodyPattern](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~BodyPattern.md) is false.

If this property is set to true, you can call [ISketchPatternFeatureData::SetFeatureScope](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData~SetFeatureScope.md).

For more information, see the **Sketch Driven Patterns** topic in the SOLIDWORKS Help.

Example

See the [ISketchPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISketchPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData.md)  
[ISketchPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchPatternFeatureData_members.md)
