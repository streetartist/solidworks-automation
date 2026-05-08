# IGetDocumentSaveToNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames`

Gets the paths and filenames to which to save the model's documents for Pack and Go set by IPackAndGo::ISetDocumentSaveToNames.
Gets the paths and filenames to which to save the model's documents for Pack and Go set by [IPackAndGo::ISetDocumentSaveToNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDocumentSaveToNames( _
   ByVal NameCount As System.Integer, _
   ByRef NameList As System.String, _
   ByRef StatusList As System.Integer _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim NameCount As System.Integer
Dim NameList As System.String
Dim StatusList As System.Integer
Dim value As System.Boolean
 
value = instance.IGetDocumentSaveToNames(NameCount, NameList, StatusList)
```

```

System.bool IGetDocumentSaveToNames( 
   System.int NameCount,
   out System.string NameList,
   out System.int StatusList
)
```

```

System.bool IGetDocumentSaveToNames( 
   System.int NameCount,
   [Out] System.String^ NameList,
   [Out] System.int StatusList
) 
```

#### Parameters

*NameCount*
:   Number of documents comprising the model

*NameList*
:   - in-process, unmanaged C++: Pointer to an array of strings containing the paths and filenames of the model's documents
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

*StatusList*
:   Array containing the types of documents as defined in [swPackAndGoDocumentStatus\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPackAndGoDocumentStatus_e.html)

#### Return Value

True if the paths and filenames of the model's documents are returned, false if not

Remarks

Before calling this method, call [IPackAndGo::GetDocumentNamesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNamesCount.md) to get the value of NameCount.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md)  
[IPackAndGo::GetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames.md)
