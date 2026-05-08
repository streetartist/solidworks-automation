# FormToolConfiguration Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~FormToolConfiguration`

Gets or sets the configuration of this forming tool's part to insert.
Gets or sets the configuration of this forming tool's part to insert.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FormToolConfiguration As System.String
```

```

Dim instance As ILibraryFormToolFeatureData
Dim value As System.String
 
instance.FormToolConfiguration = value
 
value = instance.FormToolConfiguration
```

```

System.string FormToolConfiguration {get; set;}
```

```

property System.String^ FormToolConfiguration {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Forming tool configuration name

Example

See the [ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md)  
[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.md)
