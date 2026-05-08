# D2ReverseDirection Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2ReverseDirection`

Gets or sets whether to reverse Direction 2 for this bidirectional curve-driven pattern feature.
Gets or sets whether to reverse Direction 2 for this bidirectional curve-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2ReverseDirection As System.Boolean
```

```

Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean
 
instance.D2ReverseDirection = value
 
value = instance.D2ReverseDirection
```

```

System.bool D2ReverseDirection {get; set;}
```

```

property System.bool D2ReverseDirection {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True reverses Direction 2, false does not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[ICurveDrivenPatternFeatureData::D1ReverseDirection Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D1ReverseDirection.md)  
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.md)
