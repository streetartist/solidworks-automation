# TrimEndFace Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimEndFace`

Gets or sets whether to align the thread to the end face of this thread feaure.
Gets or sets whether to align the thread to the end face of this thread feaure.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TrimEndFace As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.TrimEndFace = value
 
value = instance.TrimEndFace
```

```

System.bool TrimEndFace {get; set;}
```

```

property System.bool TrimEndFace {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to align the thread to the end face, false to not (default)

Remarks

This property is valid only if the thread profile extends beyond the trimming face.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)  
[IThreadFeatureData::TrimStartFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimStartFace.md)  
[IThreadFeatureData::MultipleStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.md)  
[IThreadFeatureData::RightHanded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~RightHanded.md)
