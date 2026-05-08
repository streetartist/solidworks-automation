# HasRenamedDocuments Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasRenamedDocuments`

Gets whether the document has renamed files.
Gets whether the document has renamed files.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function HasRenamedDocuments() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.HasRenamedDocuments()
```

```

System.bool HasRenamedDocuments()
```

```

System.bool HasRenamedDocuments(); 
```

#### Return Value

True if the document has renamed files, false if not

Example

[Rename Components and Save Assembly (C#)](Rename_Components_and_Save_Assembly_Example_CSharp.htm)  
[Rename Components and Save Assembly (VB.NET)](Rename_Components_and_Save_Assembly_Example_VBNET.htm)  
[Rename Components and Save Assembly (VBA)](Rename_Components_and_Save_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)  
[IModelDocExtension::RenameDocument Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RenameDocument.md)  
[IRenamedDocumentReferences Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRenamedDocumentReferences.md)
