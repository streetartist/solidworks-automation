# MultipleStart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart`

Gets or sets whether the thread has multiple starts in this thread feature.
Gets or sets whether the thread has multiple starts in this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MultipleStart As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.MultipleStart = value
 
value = instance.MultipleStart
```

```

System.bool MultipleStart {get; set;}
```

```

property System.bool MultipleStart {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True if the thread has multiple starts, false if not (default)

Remarks

If this property is set to true, use [IThreadFeatureData::NumberOfStarts](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~NumberOfStarts.md) to set the number of times the thread is created in an evenly-spaced circular pattern around the hole or shaft.

[IThreadFeatureData::Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Pitch.md) must permit multiple starts without causing crossing or self-intersecting threads. For example, the pitch of one thread must be wide enough to allow the nesting of other threads of different pitch.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)  
[IThreadFeatureData::TrimEndFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimEndFace.md)  
[IThreadFeatureData::TrimStartFace Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~TrimStartFace.md)  
[IThreadFeatureData::RightHanded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~RightHanded.md)
