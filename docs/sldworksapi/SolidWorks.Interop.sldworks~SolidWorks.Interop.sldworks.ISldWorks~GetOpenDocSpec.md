# GetOpenDocSpec Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocSpec`

Gets the specifications to use when opening a model document.
Gets the specifications to use when opening a model document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetOpenDocSpec( _
   ByVal FileName As System.String _
) As System.Object
```

```

Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object
 
value = instance.GetOpenDocSpec(FileName)
```

```

System.object GetOpenDocSpec( 
   System.string FileName
)
```

```

System.Object^ GetOpenDocSpec( 
   System.String^ FileName
) 
```

#### Parameters

*FileName*
:   Path and file name of the document to open

#### Return Value

[Document specification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md)

Example

[Hide All Edges in Drawing View (VBA)](Hide_All_Edges_in_Drawing_View_Example_VB.htm)  
[Open Drawing Document Read-only (VBA)](Open_Drawing_Document_Read-only_Example_VB.htm)  
[Get Whether Components Are Loaded (C#)](Get_Whether_Components_Are_Loaded_Example_CSharp.htm)  
[Get Whether Components Are Loaded (VB.NET)](Get_Whether_Components_Are_Loaded_Example_VBNET.htm)  
[Get Whether Components Are Loaded (VBA)](Get_Whether_Components_Are_Loaded_Example_VB.htm)  
[Open Assembly Document (C#)](Open_Assembly_Document_Example_CSharp.htm)  
[Open Assembly Document (VB.NET)](Open_Assembly_Document_Example_VBNET.htm)  
[Open Assembly Document (VBA)](Open_Assembly_Document_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
