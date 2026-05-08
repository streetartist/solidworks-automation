# PitchOverride Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~PitchOverride`

Gets or sets whether to override the pitch of the thread helix of this thread feature.
Gets or sets whether to override the pitch of the thread helix of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PitchOverride As System.Boolean
```

```

Dim instance As IThreadFeatureData
Dim value As System.Boolean
 
instance.PitchOverride = value
 
value = instance.PitchOverride
```

```

System.bool PitchOverride {get; set;}
```

```

property System.bool PitchOverride {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to override the pitch, false to not (default)

Remarks

If this property is set to true, use [IThreadFeatureData::Pitch](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Pitch.md) to set the pitch of the thread helix.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
