# SetDocumentSaveToNames Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetDocumentSaveToNames`

Sets the paths and filenames of the documents for Pack and Go.
Sets the paths and filenames of the documents for Pack and Go.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDocumentSaveToNames( _
   ByVal PathNameList As System.Object _
) As System.Boolean
```

```

Dim instance As IPackAndGo
Dim PathNameList As System.Object
Dim value As System.Boolean
 
value = instance.SetDocumentSaveToNames(PathNameList)
```

```

System.bool SetDocumentSaveToNames( 
   System.object PathNameList
)
```

```

System.bool SetDocumentSaveToNames( 
   System.Object^ PathNameList
) 
```

#### Parameters

*PathNameList*
:   Array of paths and filenames to which to save the model's documents

#### Return Value

True if the paths and filenames are set, false if not

Remarks

The number, order, and type of documents to save must match the array returned by [IPackAndGo::GetDocumentNames](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentNames.md). You cannot change the filename of a document if the document is a virtual component. Duplicate files are not allowed.

To remove a file from Pack and Go, specify an empty string for that file's element in the PathNameList array. To override the paths and filenames set by this method, use [IPackAndGo::SetSaveToName](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~SetSaveToName.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.md)  
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.md)  
[IPackAndGo::GetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~GetDocumentSaveToNames.md)  
[IPackAndGo::ISetDocumentSaveToNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~ISetDocumentSaveToNames.md)  
[IPackAndGo::FlattenToSingleFolder Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~FlattenToSingleFolder.md)
