# D2Direction Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2Direction`

Gets or sets Direction 2 of this bidirectional curve-driven pattern feature.
Gets or sets Direction 2 of this bidirectional curve-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2Direction As System.Object
```

```

Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Object
 
instance.D2Direction = value
 
value = instance.D2Direction
```

```

System.object D2Direction {get; set;}
```

```

property System.Object^ D2Direction {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Pattern direction entity

Remarks

The pattern direction can be a curve, edge, sketch entity, or a sketch. You must pre-select the Direction 2 entity using selection Mark = 2 before creating the feature definition. Use this property only when editing the pattern feature.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this property.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[ICurveDrivenPatternFeatureData::D1Direction Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1Direction.md)  
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.md)
