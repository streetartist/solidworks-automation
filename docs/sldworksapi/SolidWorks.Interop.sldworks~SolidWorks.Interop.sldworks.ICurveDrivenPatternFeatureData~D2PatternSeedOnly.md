# D2PatternSeedOnly Property (ICurveDrivenPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~D2PatternSeedOnly`

Gets or sets whether to replicate the seed pattern only in Direction 2, without replicating the curve pattern created under Direction 1.
Gets or sets whether to replicate the seed pattern only in Direction 2, without replicating the curve pattern created under Direction 1.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property D2PatternSeedOnly As System.Boolean
```

```

Dim instance As ICurveDrivenPatternFeatureData
Dim value As System.Boolean
 
instance.D2PatternSeedOnly = value
 
value = instance.D2PatternSeedOnly
```

```

System.bool D2PatternSeedOnly {get; set;}
```

```

property System.bool D2PatternSeedOnly {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True patterns the seed feature only in Direction 2

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICurveDrivenPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData.md)  
[ICurveDrivenPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData_members.md)  
[ICurveDrivenPatternFeatureData::Dir2Specified Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICurveDrivenPatternFeatureData~Dir2Specified.md)
