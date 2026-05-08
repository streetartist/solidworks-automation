# PatternFaceArray Property (ITablePatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~PatternFaceArray`

Gets or sets the patterned faces for this table-driven pattern feature.
Gets or sets the patterned faces for this table-driven pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PatternFaceArray As System.Object
```

```

Dim instance As ITablePatternFeatureData
Dim value As System.Object
 
instance.PatternFaceArray = value
 
value = instance.PatternFaceArray
```

```

System.object PatternFaceArray {get; set;}
```

```

property System.Object^ PatternFaceArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of patterned [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ITablePatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData.md)  
[ITablePatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData_members.md)  
[ITablePatternFeatureData::GetPatternFaceCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~GetPatternFaceCount.md)  
[ITablePatternFeatureData::IGetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~IGetPatternFaceArray.md)  
[ITablePatternFeatureData::ISetPatternFaceArray Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITablePatternFeatureData~ISetPatternFaceArray.md)
