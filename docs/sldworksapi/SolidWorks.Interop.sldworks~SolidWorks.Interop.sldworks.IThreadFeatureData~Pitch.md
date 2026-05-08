# Pitch Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Pitch`

Gets or sets the pitch of the thread helix of this thread feature.
Gets or sets the pitch of the thread helix of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Pitch As System.Double
```

```

Dim instance As IThreadFeatureData
Dim value As System.Double
 
instance.Pitch = value
 
value = instance.Pitch
```

```

System.double Pitch {get; set;}
```

```

property System.double Pitch {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

0.0 < Pitch of the helix; default is determined by interrogating the selected configuration's profile sketch

Remarks

Specify either a value or an equation that starts with an equal sign (=).

This property is valid only if [IThreadFeatureData::PitchOverride](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~PitchOverride.md) is set to true.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)  
[IThreadFeatureData::MultipleStart Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~MultipleStart.md)
