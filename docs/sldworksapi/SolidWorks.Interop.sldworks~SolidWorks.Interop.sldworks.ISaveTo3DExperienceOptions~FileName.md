# FileName Property (ISaveTo3DExperienceOptions)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions~FileName`

Gets or sets the specified file name when saving a document in SOLIDWORKS Connected.
Gets or sets the specified file name when saving a document in [SOLIDWORKS Connected](sldworksapiprogguide.chm::/Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FileName As System.String
```

```

Dim instance As ISaveTo3DExperienceOptions
Dim value As System.String
 
instance.FileName = value
 
value = instance.FileName
```

```

System.string FileName {get; set;}
```

```

property System.String^ FileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

File name

Example

See the [IPLMObjectSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPLMObjectSpecification.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISaveTo3DExperienceOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions.md)  
[ISaveTo3DExperienceOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions_members.md)
