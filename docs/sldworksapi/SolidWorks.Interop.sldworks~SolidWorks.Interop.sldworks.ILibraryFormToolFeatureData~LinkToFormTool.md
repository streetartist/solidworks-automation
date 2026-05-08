# LinkToFormTool Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData~LinkToFormTool`

Gets or sets whether to link this forming tool to its part in the Design Library.
Gets or sets whether to link this forming tool to its part in the Design Library.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property LinkToFormTool As System.Boolean
```

```

Dim instance As ILibraryFormToolFeatureData
Dim value As System.Boolean
 
instance.LinkToFormTool = value
 
value = instance.LinkToFormTool
```

```

System.bool LinkToFormTool {get; set;}
```

```

property System.bool LinkToFormTool {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to link this forming tool to its part in the Design Library, false to not

Example

See the [ILibraryFormToolFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILibraryFormToolFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData.md)  
[ILibraryFormToolFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILibraryFormToolFeatureData_members.md)
