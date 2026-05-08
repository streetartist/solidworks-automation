# GetDocumentNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames`

Gets the original paths and filenames of all of the model's documents for Pack and Go.
Gets the original paths and filenames of all of the model's documents for Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDocumentNames( _
   ByRef DocumentNames As System.Object _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim DocumentNames As System.Object
Dim value As System.Boolean
 
value = instance.GetDocumentNames(DocumentNames)
```

```

System.bool GetDocumentNames( 
   out System.object DocumentNames
)
```

```

System.bool GetDocumentNames( 
   [Out] System.Object^ DocumentNames
) 
```

#### Parameters

*DocumentNames*
:   Array of strings of the original paths and filenames of all of the model's documents

#### Return Value

True if the original paths and filenames of all of the model's documents are returned, false if not

Remarks

To get the drawing documents of the model, set [IPackAndGo::IncludeDrawings](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeDrawings.md) to true; otherwise, the paths and filenames of the model's drawing documents are not returned.

Example

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)  
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)  
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::GetDocumentNamesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.md)  
[IPackAndGo::IGetDocumentNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.md)
