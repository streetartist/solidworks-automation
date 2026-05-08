# Type Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Type`

Gets or sets the thread profile of this thread feature.
Gets or sets the thread profile of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Type As System.String
```

```

Dim instance As IThreadFeatureData
Dim value As System.String
 
instance.Type = value
 
value = instance.Type
```

```

System.string Type {get; set;}
```

```

property System.String^ Type {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Thread profile (see **Remarks**)

Remarks

This property corresponds to a Type in the Thread PropertyManager.

Types are defined in **\*.sldlfp** files. You can specify this property with or without the sldlfp extension and path. If you specify this property without:

- a path, SOLIDWORKS searches for the file in the folder specified by **Tools > Options > System Options > File Locations > Show folders for Thread Profiles**.
- an extension, SOLIDWORKS assumes the extension is sldlfp.

Example

See the [IThreadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)  
[IThreadFeatureData::Size Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~Size.md)
