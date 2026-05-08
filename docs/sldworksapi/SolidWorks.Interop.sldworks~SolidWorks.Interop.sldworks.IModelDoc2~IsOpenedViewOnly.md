# IsOpenedViewOnly Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedViewOnly`

Gets whether a SOLIDWORKS document is open in view-only mode.
Gets whether a SOLIDWORKS document is open in view-only mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsOpenedViewOnly() As System.Boolean
```

```

Dim instance As IModelDoc2
Dim value As System.Boolean
 
value = instance.IsOpenedViewOnly()
```

```

System.bool IsOpenedViewOnly()
```

```

System.bool IsOpenedViewOnly(); 
```

#### Return Value

True if document is in a view-only state, false if not

Remarks

Files are loaded using multi-threading. When a file is loading, the graphics are displayed immediately and the end-user is able to perform certain view zooming and panning functions. Until all data and references are loaded, the file is in view-only mode.

A file can be in view-only mode if the end-user chose to load the file for viewing purposes. You application should check for view-only mode to determine how to proceed.

NOTE: When a file is in view-only mode, many API queries return NULL or empty data.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IsOpenedReadOnly Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsOpenedReadOnly.md)  
[IModelDoc2::SetReadOnlyState Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SetReadOnlyState.md)
