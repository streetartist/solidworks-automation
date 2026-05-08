# MirrorProfile Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorProfile`

Gets or sets whether to flip the profile of the thread helix about its horizontal or vertical axis in this thread feature.
Gets or sets whether to flip the profile of the thread helix about its horizontal or vertical axis in this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property MirrorProfile As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.MirrorProfile = value
 
value = instance.MirrorProfile
```

```

System.bool MirrorProfile {get; set;}
```

```

property System.bool MirrorProfile {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to flip the profile of the thread helix about its horizontal or vertical axis, false to not (default)

Remarks

If this property is set to true, use [IThreadFeatureData::MirrorType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MirrorType.md) to specify the axis about which to flip the thread helix profile.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
