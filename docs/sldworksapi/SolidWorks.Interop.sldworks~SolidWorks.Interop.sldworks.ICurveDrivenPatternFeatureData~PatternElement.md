# PatternElement Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternElement`

Gets or sets the type of entities to base this curve-driven pattern feature.
Gets or sets the type of entities to base this curve-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternElement As System.Integer
```

```

Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Integer
 
instance.PatternElement = value
 
value = instance.PatternElement
```

```

System.int PatternElement {get; set;}
```

```

property System.int PatternElement {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of entities to base this curve-driven pattern feature as defined in [swPatternElementSelection\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swPatternElementSelection_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[ICurveDrivenPatternFeatureData::BodyPattern Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern.md)
