# Sketch Property (IProjectionCurveFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Sketch`

Gets or sets the sketch to project in this projection curve feature.
Gets or sets the sketch to project in this projection curve feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Sketch As System.Object
```

```

Dim instance As IProjectionCurveFeatureData
Dim value As System.Object
 
instance.Sketch = value
 
value = instance.Sketch
```

```

System.object Sketch {get; set;}
```

```

property System.Object^ Sketch {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[ISketch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.md)

Remarks

You cannot use this property to get or set the target sketch for sketch-on-sketch projection curve features. You can only pre-select the target sketch before creating the feature. See the [IProjectionCurveFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md) Remarks.

Use [IFeature::GetSpecificFeature2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetSpecificFeature2.md) to get the ISketch object from the selected [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.md) object.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IProjectionCurveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData.md)  
[IProjectionCurveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData_members.md)  
[IProjectionCurveFeatureData::Reverse Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProjectionCurveFeatureData~Reverse.md)
