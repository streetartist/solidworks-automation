# FormToolPath Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~FormToolPath`

Gets or sets the pathname of this forming tool's part in the Design Library.
Gets or sets the pathname of this forming tool's part in the Design Library.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property FormToolPath As System.String
```

```

Dim instance As ILibraryFormToolFeatureData
Dim value As System.String
 
instance.FormToolPath = value
 
value = instance.FormToolPath
```

```

System.string FormToolPath {get; set;}
```

```

property System.String^ FormToolPath {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Design library forming tool part pathname

Remarks

When LibraryFormToolFeatureData is modified and this property changes to another forming tool, then the forming tool feature name changes to reflect the new forming tool name.

Example

See the [ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md)  
[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.md)
