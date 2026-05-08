# NumberOfStarts Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~NumberOfStarts`

Gets or sets the number of times the thread is created in an evenly-spaced pattern around the hole or shaft of this thread feature.
Gets or sets the number of times the thread is created in an evenly-spaced pattern around the hole or shaft of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NumberOfStarts As System.Integer
```

```

Dim instance As IThreadFeatureData
Dim value As System.Integer
 
instance.NumberOfStarts = value
 
value = instance.NumberOfStarts
```

```

System.int NumberOfStarts {get; set;}
```

```

property System.int NumberOfStarts {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

2 (default) <= Number of times the thread is started <= 1000

Remarks

This property is valid only if [IThreadFeatureData::MultipleStart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.md) is set to true.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
