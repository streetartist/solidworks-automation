# BodyPattern Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~BodyPattern`

Gets or sets whether to base this curve-driven pattern feature on bodies or features and faces.
Gets or sets whether to base this curve-driven pattern feature on bodies or features and faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BodyPattern As System.Boolean
```

```

Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean
 
instance.BodyPattern = value
 
value = instance.BodyPattern
```

```

System.bool BodyPattern {get; set;}
```

```

property System.bool BodyPattern {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True for bodies, false for features and faces

Remarks

If this property is:

- True, use [ICurveDrivenPatternFeatureData::PatternBodyArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternBodyArray.md) to specify the seed bodies to pattern.
- False, use [ICurveDrivenPatternFeatureData::PatternFaceArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFaceArray.md) or [ICurveDrivenPatternFeatureData::PatternFeatureArray](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternFeatureArray.md) to specify the face or feature seeds to pattern.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[ICurveDrivenPatternFeatureData::PatternElement Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~PatternElement.md)  
[ICurveDrivenPatternFeatureData::IGetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternBodyArray.md)  
[ICurveDrivenPatternFeatureData::IGetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternFaceArray.md)  
[ICurveDrivenPatternFeatureData::IGetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~IGetPatternFeatureArray.md)  
[ICurveDrivenPatternFeatureData::ISetPatternBodyArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternBodyArray.md)  
[ICurveDrivenPatternFeatureData::ISetPatternFaceArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternFaceArray.md)  
[ICurveDrivenPatternFeatureData::ISetPatternFeatureArray Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~ISetPatternFeatureArray.md)
