# IsFutureVersion Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IsFutureVersion`

Gets whether this document is for a future version of SOLIDWORKS.
Gets whether this document is for a future version of SOLIDWORKS.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IsFutureVersion() As System.Boolean
```

```

Dim instance As IModelDocExtension
Dim value As System.Boolean
 
value = instance.IsFutureVersion()
```

```

System.bool IsFutureVersion()
```

```

System.bool IsFutureVersion(); 
```

#### Return Value

True if the document is for a future version of SOLIDWORKS, false if not

Remarks

As of 2012 SP5, loading future file versions is supported, and [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) no longer throws a [swFileLoadError\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swFileLoadError_e.html).swFutureVersion error.

Use IModelDocExtension::IsFutureVersion to determine:

- how to obtain the correct version history of a document. If a future version document is loaded in an older version of SOLIDWORKS, [IModelDoc2::VersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~VersionHistory.md) and [IModelDoc2::IVersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IVersionHistory.md) return the version history of the part template, not the version history of the future version document. To get the version history of a future version document, use [ISldWorks::VersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~VersionHistory.md) or [ISldWorks::IVersionHistory](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IVersionHistory.md) to get the version history from its file.
- whether a component is for a future version of SOLIDWORKS and should be hidden in the user interface of older versions. Although they can be loaded, future version components may not be actionable in older versions of SOLIDWORKS.

Example

[Get Version History of Future Version Document (VBA)](Get_Version_History_of_Future_Version_Document_Example_VB.htm)  
[Get Version History of Future Version Document (VB.NET)](Get_Version_History_of_Future_Version_Document_Example_VBNET.htm)  
[Get Version History of Future Version Document (C#)](Get_Version_History_of_Future_Version_Document_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
