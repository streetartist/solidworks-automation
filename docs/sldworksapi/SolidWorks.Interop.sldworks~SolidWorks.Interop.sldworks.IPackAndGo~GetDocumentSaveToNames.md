# GetDocumentSaveToNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames`

Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::SetDocumentSaveToNames.
Gets the paths and filenames to which to save the model's documents for Pack and Go set by [IPackAndGo::SetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetDocumentSaveToNames( _
   ByRef PathNameList As System.Object, _
   ByRef DocumentStatusList As System.Object _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim PathNameList As System.Object
Dim DocumentStatusList As System.Object
Dim value As System.Boolean
 
value = instance.GetDocumentSaveToNames(PathNameList, DocumentStatusList)
```

```

System.bool GetDocumentSaveToNames( 
   out System.object PathNameList,
   out System.object DocumentStatusList
)
```

```

System.bool GetDocumentSaveToNames( 
   [Out] System.Object^ PathNameList,
   [Out] System.Object^ DocumentStatusList
) 
```

#### Parameters

*PathNameList*
:   Array of strings containing the path and filenames to which to save the model's documents (see **Remarks**)

*DocumentStatusList*
:   Array containing the types of documents as defined in [swPackAndGoDocumentStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPackAndGoDocumentStatus_e.html)

#### Return Value

True if the paths and filenames of the model's documents are returned, false if not

Remarks

The order and number of documents must match the order of the array returned by [IPackAndGo::GetDocumentNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.md). If a [prefix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddPrefix.md) or [suffix](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~AddSuffix.md) is set, then the filenames include it. You can set both a prefix and suffix for the filenames.

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
[IPackAndGo::IGetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.md)  
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md)
