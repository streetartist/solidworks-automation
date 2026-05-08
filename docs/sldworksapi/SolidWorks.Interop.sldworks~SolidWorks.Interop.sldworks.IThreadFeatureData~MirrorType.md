# MirrorType Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorType`

Gets or sets how to flip the profile of the thread helix of this thread feature.
Gets or sets how to flip the profile of the thread helix of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorType As System.Integer
```

```

Dim instance As IThreadFeatureData
Dim value As System.Integer
 
instance.MirrorType = value
 
value = instance.MirrorType
```

```

System.int MirrorType {get; set;}
```

```

property System.int MirrorType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Mirror profile type as defined in [swThreadMirrorType\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swThreadMirrorType_e.html); default is swThreadMirrorType\_e.swThreadMirrorType\_Horizontally

Remarks

This property is valid only if [IThreadFeatureData::MirrorProfile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorProfile.md) is set to true.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
