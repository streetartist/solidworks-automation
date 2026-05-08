# ISetDocumentSaveToNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames`

Sets the paths and filenames of the documents to save in Pack and Go.
Sets the paths and filenames of the documents to save in Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ISetDocumentSaveToNames( _
   ByVal NameCount As System.Integer, _
   ByRef NameList As System.String _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim NameCount As System.Integer
Dim NameList As System.String
Dim value As System.Boolean
 
value = instance.ISetDocumentSaveToNames(NameCount, NameList)
```

```

System.bool ISetDocumentSaveToNames( 
   System.int NameCount,
   ref System.string NameList
)
```

```

System.bool ISetDocumentSaveToNames( 
   System.int NameCount,
   System.String^% NameList
) 
```

#### Parameters

*NameCount*
:   Number of documents comprising the model

*NameList*
:   - in-process, unmanaged C++: Pointer to an array of strings containing the paths and filenames to which to save the model's documents
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

True if the paths and filenames are set, false if not

Remarks

The number, order, and type of documents must match the array returned by [IPackAndGo::IGetDocumentNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentNames.md). You cannot change the filename of a document if the document is a virtual component. Duplicate files are not allowed.

To remove a file from Pack and Go, specify an empty string for that file's element in the NameList array. To override the paths and filenames set by this method, use [IPackAndGo::SetSaveToName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::IGetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IGetDocumentSaveToNames.md)  
[IPackAndGo::SetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames.md)
