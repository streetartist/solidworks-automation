# Size Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Size`

Gets or sets the size of the thread of this thread feature.
Gets or sets the size of the thread of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Size As System.String
```

```

Dim instance As IThreadFeatureData
Dim value As System.String
 
instance.Size = value
 
value = instance.Size
```

```

System.string Size {get; set;}
```

```

property System.String^ Size {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Thread size (see **Remarks**)

Remarks

This property corresponds to a Size selected in the Thread PropertyManager for a selected [IThreadFeatureData::Type](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Type.md).

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
