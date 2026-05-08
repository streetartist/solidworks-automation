# GetMenuStrings Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMenuStrings`

Gets the name of the parent menu of the specified menu command.
Gets the name of the parent menu of the specified menu command.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetMenuStrings( _
   ByVal CommandID As System.Integer, _
   ByVal DocumentType As System.Integer, _
   ByRef ParentMenuName As System.String _
) As System.String
```

```

Dim instance As ISldWorks
Dim CommandID As System.Integer
Dim DocumentType As System.Integer
Dim ParentMenuName As System.String
Dim value As System.String
 
value = instance.GetMenuStrings(CommandID, DocumentType, ParentMenuName)
```

```

System.string GetMenuStrings( 
   System.int CommandID,
   System.int DocumentType,
   out System.string ParentMenuName
)
```

```

System.String^ GetMenuStrings( 
   System.int CommandID,
   System.int DocumentType,
   [Out] System.String^ ParentMenuName
) 
```

#### Parameters

*CommandID*
:   Command ID of the command whose parent menu's name you want

*DocumentType*
:   Document types in which this command exists as defined in [swDocumentTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html)

*ParentMenuName*
:   Name of the parent menu of the specified menu command

#### Return Value

Menu string

Remarks

Use this method with methods that require you to supply the name of the menu, such as [ISldWorks::RemoveMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RemoveMenu.md), [IFrame::RenameMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RenameMenu.md) and [IFrame::RemoveMenu](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~RemoveMenu.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
